import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

df = pd.read_csv("data/swing_state_polling_avgs_clean.csv")

# Colored lines for legends
blue_patch = mlines.Line2D([], [], color='blue', label='Harris')
red_patch = mlines.Line2D([], [], color='red', label='Trump')

# Average bar plot
plt.figure(figsize=(14, 8))
sns.barplot(x="state", y="Harris_average", data=df, color="blue", alpha=0.8)
sns.barplot(x="state", y="Trump_average", data=df, color="red", alpha=0.8)
plt.title("Battleground State Polling Averages")
plt.ylabel("Polling Average (%)")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.legend(handles=[blue_patch, red_patch], loc="upper left", title="Candidate")
plt.tight_layout()
plt.savefig("images/polling_bar.png")

# Margin bar plot
plt.figure(figsize=(12, 8))
sns.barplot(x="state", y="margin", data=df, hue="state", palette="coolwarm")
plt.title("Battleground State Polling Margins")
plt.ylabel("Polling Margin (%)")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/margin_plot.png")

# Scatter points
plt.figure(figsize=(14, 7))
sns.stripplot(x="state", y="Harris_average", data=df, jitter=True, color='blue', alpha=0.8)
sns.stripplot(x="state", y="Trump_average", data=df, jitter=True, color='red', alpha=0.8)
plt.title("Battleground State Polling Averages")
plt.ylabel("Polling Average (%)")
plt.xlabel("State")
plt.legend(title="Candidate", handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label="Harris"),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label="Trump")
], loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/polling_plot.png")