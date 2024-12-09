import json
import matplotlib.pyplot as plt

# Input file path
payload_analysis_file = r"data\payload_analysis.json"

with open(payload_analysis_file, "r") as f:
    analysis_data = json.load(f)

address_analysis = analysis_data["address_analysis"]
info_analysis = analysis_data["info_analysis"]

# data for address pie chart
address_labels = [entry["address"] for entry in address_analysis]
address_counts = [entry["count"] for entry in address_analysis]

# data for info pie chart
info_labels = [entry["info"] for entry in info_analysis]
info_counts = [entry["count"] for entry in info_analysis]

# pie chart for address distribution
plt.figure(figsize=(14, 8))
plt.pie(
    address_counts,
    labels=address_labels,
    autopct="%1.1f%%",
    startangle=140,
    textprops={"fontsize": 6},
)
plt.title("Mining Address Distribution from Last Pruning Point to Tip")
plt.savefig("data/mining_address_distribution.png")
plt.close()

# pie chart for info distribution
plt.figure(figsize=(14, 8))
plt.pie(
    info_counts,
    labels=info_labels,
    autopct="%1.1f%%",
    startangle=140,
    textprops={"fontsize": 6},
)
plt.title("Mining Info Distribution from Last Pruning Point to Tip")
plt.savefig("data/mining_info_payload_distribution.png")
plt.close()

print("Pie charts have been successfully generated and saved.")
