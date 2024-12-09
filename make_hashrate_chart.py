import json
import matplotlib.pyplot as plt
from datetime import datetime

# Input file path
mining_analysis_file = r"data\mining_analysis.json"

with open(mining_analysis_file, "r") as f:
    mining_data = json.load(f)

# data for the graph
timestamps = []
hashrates = []

for entry in mining_data:
    try:
        timestamp = int(entry["timestamp"]) / 1000
        readable_time = datetime.utcfromtimestamp(timestamp)

        # hashrate in MH/s
        difficulty = entry.get("difficulty", 0)
        hashrate = difficulty * 2
        hashrate_in_mh = hashrate / 1e6

        timestamps.append(readable_time)
        hashrates.append(hashrate_in_mh)
    except Exception as e:
        print(f"Error processing entry: {e}")

# Plot the graph
plt.figure(figsize=(12, 6))
plt.plot(timestamps, hashrates, label="Hashrate (MH/s)", color="blue")

# Formatting
plt.title("Hashrate (MH/s) from Last Pruning Point to Tip")
plt.xlabel("Time (UTC)")
plt.ylabel("Hashrate (MH/s)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

# Save graph
output_image = "hashrate_over_time.png"
plt.tight_layout()
plt.savefig(output_image)
plt.close()

print(f"Successfully saved as {output_image}")
