import json
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Load data from JSON file
with open("results.json") as file:
    data = json.load(file)

# macOS data
macos_labels = list(data["macOS"].keys())
macos_values = list(data["macOS"].values())

# Windows 11 data
windows_labels = list(data["Windows11"].keys())
windows_values = list(data["Windows11"].values())

# Create macOS histogram
plt.figure(figsize=(10, 6))
plt.bar(macos_labels, macos_values, alpha=0.7, edgecolor='black')
plt.title("macOS Performance (tokens per second)")
plt.xlabel("Configurations")
plt.ylabel("Tokens per Second")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("macos.png")  # Save the figure as a PNG file
plt.close()  # Close the figure to avoid overlapping with the next one

# Create Windows 11 histogram
plt.figure(figsize=(10, 6))
plt.bar(windows_labels, windows_values, alpha=0.7, edgecolor='black')
plt.title("Windows 11 Performance (tokens per second)")
plt.xlabel("Configurations")
plt.ylabel("Tokens per Second")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("win11.png")  # Save the figure as a PNG file
plt.close()  # Close the figure to avoid overlap
