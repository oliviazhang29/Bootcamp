import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plt


# get descriptives
df = pd.read_csv("treasure_hunt_scores.csv")
# print(df.head())

print(df.describe())

map = df[df["Condition"] == "Map"]["Score"]
print(map.describe())

nomap = df[df["Condition"] == "NoMap"]["Score"]
print(nomap.describe())


# t test
t_stat, p_val = stats.ttest_ind(map, nomap)
print(f"p-value: {p_val}")

if p_val < 0.05:
    print(f"Yayyy, they are different, (p-val: {p_val})")
else:
    print(f"Nooo, they are the same, (p-val: {p_val})")


# plot boxplot
plt.boxplot([map, nomap], 
            labels = ["Map", "No Map"])

plt.text(2.3, 95, f"p-value: {p_val: .3f}", 
         ha= "right", 
         va= "bottom", 
         fontsize = 10)

plt.axhline(y=df['Score'].mean(), color='red', linestyle='--',
            label=f'Mean: {df["Score"].mean():.2f}')

plt.title("Treasure Hunt Scores by Condition")
plt.xlabel("Condition")
plt.ylabel("Scores")
plt.legend()

plt.show()