import json
from collections import defaultdict

mining_analysis_file = r"data\mining_analysis.json"

# load mining_analysis.json file
with open(mining_analysis_file, "r") as f:
    mining_data = json.load(f)

address_counts = defaultdict(int)
info_counts = defaultdict(int)

address_details = defaultdict(list)
info_details = defaultdict(list)

# payloads
for entry in mining_data:
    address = entry.get("decoded_payload_address", "unknown")
    info = entry.get("decoded_payload_info", "unknown")

    address_counts[address] += 1
    info_counts[info] += 1

    # Store blockhashes for each unique address and info
    address_details[address].append(entry["blockhash"])
    info_details[info].append(entry["blockhash"])

# results
analysis_results = {
    "address_analysis": [
        {
            "address": addr,
            "count": count,
            "blockhashes": hashes,
        }
        for addr, (count, hashes) in zip(
            address_counts.keys(),
            zip(address_counts.values(), address_details.values()),
        )
    ],
    "info_analysis": [
        {
            "info": inf,
            "count": count,
            "blockhashes": hashes,
        }
        for inf, (count, hashes) in zip(
            info_counts.keys(),
            zip(info_counts.values(), info_details.values()),
        )
    ],
}

# Output file
output_file = r"data\payload_analysis.json"

with open(output_file, "w") as f:
    json.dump(analysis_results, f, indent=4)

print(f"Successfully written to {output_file}")
