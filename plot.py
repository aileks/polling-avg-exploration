import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

df = pd.read_csv("data/swing_state_polling_avgs_clean.csv")

# Colored lines for legends
blue_patch = mlines.Line2D([], [], color='blue', label='Harris')
red_patch = mlines.Line2D([], [], color='red', label='Trump')

# Polling average bar plot
df_long = pd.melt(df, id_vars=['state'], value_vars=['Harris_average', 'Trump_average'],
                  var_name='Candidate', value_name='Polling_Average')

# Create the bar plot
plt.figure(figsize=(17, 10))
sns.barplot(x="state", y="Polling_Average", hue="Candidate", data=df_long,
            palette={"Harris_average": "blue", "Trump_average": "red"}, alpha=0.8)

# Add title and labels
plt.title("Battleground State Polling Averages")
plt.ylabel("Polling Average (%)")
plt.xlabel("State")
plt.xticks(rotation=45)

# Add legend
plt.legend(title="Candidate", loc="upper left")

# Adjust layout and save plot
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

"""
Comparison Data
"""

# Real voting data
actual_voting_results = {
    'Arizona': {'Trump': 52.2, 'Harris': 46.7},
    'Nevada': {'Trump': 50.6, 'Harris': 47.5},
    'Georgia': {'Trump': 50.7, 'Harris': 48.5},
    'Pennsylvania': {'Trump': 50.4, 'Harris': 48.6},
    'Michigan': {'Trump': 49.6, 'Harris': 48.2},
    'Wisconsin': {'Trump': 49.6, 'Harris': 48.8},
    'North Carolina': {'Trump': 51.0, 'Harris': 47.7}
}

# Create a dataframe from the real voting data
actual_df = pd.DataFrame(actual_voting_results).T.reset_index()
actual_df.columns = ["state", "Trump_actual", "Harris_actual"]

# Merge polling data with actual results
df_poll = df[['state', 'Trump_average', 'Harris_average']].groupby('state').mean().reset_index()
merged_df = pd.merge(df_poll, actual_df, on='state')

# TODO: Implement a comparison plot