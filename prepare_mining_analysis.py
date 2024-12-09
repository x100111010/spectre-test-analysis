import json
from helper.mining_address import retrieve_miner_info_from_payload

# Input and output file paths
blocks_file = r"data\block.json"
output_file = r"data\mining_analysis.json"

# prepares data from blocks.json

mining_data = []

# Load the blocks.json file
with open(blocks_file, "r") as f:
    blocks_data = json.load(f)["blocks"]

# Iterate through each block and extract required information
for block_hash, block_data in blocks_data.items():
    try:
        difficulty = block_data["verboseData"].get("difficulty", 0)
        bits = block_data["header"].get("bits", 0)
        payload = (
            block_data["transactions"][0].get("payload", "")
            if block_data.get("transactions")
            else ""
        )
        block_time = (
            block_data["transactions"][0]["verboseData"].get("blockTime", 0)
            if block_data.get("transactions")
            else 0
        )
        timestamp = block_data["header"].get("timestamp", 0)

        # Decode payload
        decoded_info, decoded_address = retrieve_miner_info_from_payload(payload)

        mining_data.append(
            {
                "blockhash": block_hash,
                "difficulty": difficulty,
                "bits": bits,
                "payload": payload,
                "decoded_payload_address": decoded_address,
                "decoded_payload_info": decoded_info,
                "blocktime": block_time,
            }
        )
    except Exception as e:
        print(f"Error processing block {block_hash}: {e}")

with open(output_file, "w") as f:
    json.dump(mining_data, f, indent=4)

print(f"Successfully written to {output_file}")
