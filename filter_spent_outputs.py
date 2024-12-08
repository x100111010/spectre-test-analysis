import json

# Input and output paths
blocks_file = r"data\block.json"
output_file = r"data\spent-outputs.json"

# init outputs dictionary
outputs = {}
referenced_outputs = {}

with open(blocks_file, "r") as f:
    blocks_data = json.load(f)["blocks"]

# First pass: Gather referenced outputs from inputs and populate outputs from current transactions
for block_hash, block_data in blocks_data.items():
    for transaction in block_data.get("transactions", []):
        # Capture referenced outputs from inputs
        for input in transaction.get("inputs", []):
            prev_outpoint_tx_id = input["previousOutpoint"]["transactionId"]
            prev_outpoint_index = input["previousOutpoint"].get("index", 0)
            unique_key = f"{prev_outpoint_tx_id}-{prev_outpoint_index}"

            # placeholder for referenced outputs
            if unique_key not in referenced_outputs:
                referenced_outputs[unique_key] = {"amount": 0, "address": "unknown"}

        # Iterate through transaction outputs to populate outputs
        for index, output in enumerate(transaction.get("outputs", [])):
            # Construct the unique key
            transaction_id = transaction["verboseData"]["transactionId"]
            unique_key = f"{transaction_id}-{index}"

            # amount and address
            amount = int(output["amount"])
            address = output["verboseData"]["scriptPublicKeyAddress"]

            # Add to outputs dictionary
            outputs[unique_key] = {"amount": amount, "address": address}

# Merge referenced outputs with actual outputs
for key, placeholder in referenced_outputs.items():
    if key not in outputs:
        outputs[key] = placeholder

# Write the outputs to spent-outputs.json
with open(output_file, "w") as f:
    json.dump({"outputs": outputs}, f, indent=4)

print(f"Successfully written to {output_file}")
