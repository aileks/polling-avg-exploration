import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/swing_state_polling_avgs_clean.csv")

plt.figure(figsize=(14, 7))

# Plot polling averages
sns.stripplot(x="state", y="Harris_average", data=df, jitter=True, color='blue', alpha=0.8)
sns.stripplot(x="state", y="Trump_average", data=df, jitter=True, color='red', alpha=0.8)

# Add labels and title
plt.title("Battleground State Polling Averages")
plt.ylabel("Polling Average (%)")
plt.xlabel("State")

# Adjust the legend and layout
plt.legend(title="Candidate", handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label="Harris"),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label="Trump")
], loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/polling_plot.png")
