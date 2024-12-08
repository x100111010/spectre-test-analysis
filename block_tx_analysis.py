from collections import defaultdict
import glob
import json
import statistics
from datetime import datetime, timezone


# Constants
SPENT_OUTPUTS = True

# Load data, prep for analysis
blocks = {}
for file_path in glob.glob("./data/block.json"):
    with open(file_path, "r") as file:
        data = json.load(file)["blocks"]
        blocks.update(data)

with open("./data/spent-outputs.json", "r") as f:
    spent_outputs = json.load(f)["outputs"]

print(f"Blocks Loaded: {len(blocks)}")
print(f"Spent Outputs Loaded: {len(spent_outputs)}")

# Initialize sets and lists for analysis
chainblocks = set()
non_chainblocks = set()
merged_blues = set()
merged_reds = set()

blocks_per_daa = defaultdict(int)
block_timestamps = []
chainblock_timestamps = []

coinbase_txs = 0
coinbase_outputs = []

accepted_txs = set()  # Regular, non-coinbase transactions
outputs_spent = []  # Spent outputs
outputs_created = []  # Created outputs
fees = []

sending_addrs = set()
receiving_addrs = set()

blocks_per_day = defaultdict(
    lambda: {"total": 0, "chainblocks": 0, "non_chainblocks": 0, "blues": 0, "reds": 0}
)

# Pre-process data
for hash, block in blocks.items():
    block_timestamps.append(int(block["header"]["timestamp"]))

if block_timestamps:
    earliest_time = min(block_timestamps)
    latest_time = max(block_timestamps)
else:
    print("No timestamps found in blocks!")
    exit(1)


def start_of_day(ts):
    return ts - (ts % (24 * 60 * 60 * 1000))


for hash, block in blocks.items():
    timestamp = int(block["header"]["timestamp"])
    day_start = start_of_day(timestamp)

    blocks_per_day[day_start]["total"] += 1

    if block["verboseData"].get("isChainBlock"):
        blocks_per_day[day_start]["chainblocks"] += 1
    else:
        blocks_per_day[day_start]["non_chainblocks"] += 1

    # Directly count merged blues and reds for blocks within this time range
    blocks_per_day[day_start]["blues"] += len(
        block["verboseData"].get("mergeSetBluesHashes", [])
    )
    blocks_per_day[day_start]["reds"] += len(
        block["verboseData"].get("mergeSetRedsHashes", [])
    )

for hash, block in blocks.items():
    blocks_per_daa[block["header"]["daaScore"]] += 1

    # Chainblock vs. non-chainblock
    if block["verboseData"].get("isChainBlock"):
        chainblocks.add(hash)
        chainblock_timestamps.append(int(block["header"]["timestamp"]))
    else:
        non_chainblocks.add(hash)

    # Blue mergeset
    for bh in block["verboseData"].get("mergeSetBluesHashes", []):
        merged_blues.add(bh)

    # Red mergeset
    for bh in block["verboseData"].get("mergeSetRedsHashes", []):
        merged_reds.add(bh)

    # Process transactions
    for tx in block["transactions"]:
        tx_id = tx["verboseData"]["transactionId"]

        # Skip if tx is not accepted
        if not tx.get("accepted"):
            continue

        # Skip if tx has already been processed
        if tx_id in accepted_txs:
            continue
        accepted_txs.add(tx_id)

        # Process coinbase transactions
        if tx["subnetworkId"] == "0100000000000000000000000000000000000000":
            coinbase_txs += 1
            for output in tx["outputs"]:
                coinbase_outputs.append(int(output["amount"]))
            continue

        # Process "regular" transactions
        total_output_amount = 0
        for output in tx["outputs"]:
            outputs_created.append(int(output["amount"]))
            total_output_amount += int(output["amount"])

            receiving_addrs.add(output["verboseData"]["scriptPublicKeyAddress"])

        if SPENT_OUTPUTS:
            total_input_amount = 0
            skip_block = False  # indicate whether to skip the block
            for input in tx["inputs"]:
                prev_outpoint_tx_id = input["previousOutpoint"]["transactionId"]
                prev_outpoint_index = input["previousOutpoint"].get("index", 0)

                key = f"{prev_outpoint_tx_id}-{prev_outpoint_index}"
                if key not in spent_outputs:
                    print(
                        f"Warning: Key {key} not found in spent outputs. Skipping block."
                    )
                    skip_block = True
                    break  # Stop processing this block if key is missing

                input_amount = spent_outputs[key]["amount"]
                outputs_spent.append(input_amount)
                total_input_amount += input_amount

                sending_addr = spent_outputs[key]["address"]
                sending_addrs.add(sending_addr)

            if skip_block:
                continue

            tx_fee = total_input_amount - total_output_amount
            fees.append(tx_fee)


# Define utility for printing statistics
def list_stats(title, data_list, ptotal=True, to_spr=True):
    data_list.sort()

    total = sum(data_list)
    mean = sum(data_list) / len(data_list)
    median = statistics.median(data_list)
    minimum = min(data_list)
    maximum = max(data_list)

    f = 100_000_000 if to_spr else 1

    print(title)
    if ptotal:
        print(f"Total: {total / f:,}")
    print(f"Mean: {mean / f:,}")
    print(f"Median: {median / f:,}")
    print(f"Min: {minimum / f:,}")
    print(f"Max: {maximum / f:,}")


# Print results
print("--- COUNTS")
print(f"Chainblocks: {len(chainblocks):,}")
print(f"Non-chainblocks: {len(non_chainblocks):,}")
print(f"Merged blues: {len(merged_blues):,}")
print(f"Merged reds: {len(merged_reds):,}\n")

print("--- Daily BLOCK Analysis ---")
for day_start, counts in sorted(blocks_per_day.items()):
    day_str = datetime.fromtimestamp(day_start // 1000, tz=timezone.utc).strftime(
        "%Y-%m-%d"
    )
    print(f"Date: {day_str}")
    print(f"Total blocks: {counts['total']}")
    print(f"Chainblocks: {counts['chainblocks']}")
    print(f"Non-chainblocks: {counts['non_chainblocks']}")
    print(f"Merged blues: {counts['blues']}")
    print(f"Merged reds: {counts['reds']}")
    print()

print(f"Coinbase transactions: {coinbase_txs:,}")
print(f"Coinbase outputs: {len(coinbase_outputs):,}\n")

print(f"Accepted transactions (not incl. coinbase): {len(accepted_txs):,}")
print(f"Outputs spent: {len(outputs_spent):,}")
print(f"Outputs created: {len(outputs_created):,}\n")

print(f"Fees: {len(fees):,} (qty of fees should = accepted txs - coinbase txs)\n")
print(f"Unique sending addresses: {len(sending_addrs):,}")
print(f"Unique receiving addresses: {len(receiving_addrs):,}\n")

list_stats("--- Coinbase Outputs (in SPR)", coinbase_outputs)
list_stats("--- Spent Outputs (in SPR)", outputs_spent)
list_stats("--- Created Outputs (in SPR)", outputs_created)
list_stats("--- Fees (in SPR)", fees)

bpd = list(blocks_per_daa.values())
bpd.sort()
list_stats("--- Blocks per DAA", bpd, ptotal=False, to_spr=False)

block_timestamps.sort()
block_timestamp_diffs = [
    block_timestamps[i + 1] - block_timestamps[i]
    for i in range(len(block_timestamps) - 1)
]
list_stats(
    "--- Block intervals (in milliseconds)",
    block_timestamp_diffs,
    ptotal=False,
    to_spr=False,
)

chainblock_timestamps.sort()
chainblock_timestamp_diffs = [
    chainblock_timestamps[i + 1] - chainblock_timestamps[i]
    for i in range(len(chainblock_timestamps) - 1)
]
list_stats(
    "--- Chainblock intervals (in milliseconds)",
    chainblock_timestamp_diffs,
    ptotal=False,
    to_spr=False,
)
