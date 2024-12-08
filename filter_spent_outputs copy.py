import json

# Input and output paths
blocks_file = r"data\block.json"
output_file = r"data\spent-outputs.json"

# init outputs dictionary
outputs = {}
referenced_outputs = {}

# Load the blocks.json file
with open(blocks_file, "r") as f:
    blocks_data = json.load(f)["blocks"]

# Iterate through each block and its transactions
for block_hash, block_data in blocks_data.items():
    for transaction in block_data.get("transactions", []):
        # Iterate through transaction outputs
        for index, output in enumerate(transaction.get("outputs", [])):
            # Construct the unique key for each output
            transaction_id = transaction["verboseData"]["transactionId"]
            unique_key = f"{transaction_id}-{index}"

            # Extract amount and address
            amount = int(output["amount"])
            address = output["verboseData"]["scriptPublicKeyAddress"]

            # Add to outputs dictionary
            outputs[unique_key] = {"amount": amount, "address": address}

# Write the outputs to spent-outputs.json
with open(output_file, "w") as f:
    json.dump({"outputs": outputs}, f, indent=4)

print(f"Spent outputs have been successfully written to {output_file}")
