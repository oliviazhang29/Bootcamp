import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plt

data_0 = pd.Series([1, 3, 4, 5, 6])
data_1 = pd.Series([1, 2, 3, 4, 100])
data_2 = pd.Series([2, 2, 4, 4, 6])
data_3 = pd.Series([96, 97, 98, 99, 99])


# descriptives
# mean_0 = data_0.mean()
# mean_1 = data_1.mean()

# print(f"Dataset 0 -> mean: {mean_0}")
# print(f"Dataset 1 -> mean: {mean_1}")

# median_0 = data_0.median()
# median_1 = data_1.median()

# print(f"Dataset 0 -> median: {median_0}")
# print(f"Dataset 1 -> median: {median_1}")

# sd_0 = data_0.std()
# sd_1 = data_1.std()

# print(f"Dataset 0 -> standard dev: {sd_0}")
# print(f"Dataset 1 -> standard dev: {sd_1}")

# print(data_0.describe())



# t test
# t_stat, p_val = stats.ttest_ind(data_0, data_1)
# print(f"p-value: {p_val}")

# if p_val < 0.05:
#     print(f"Yayyy, you guys are correct, they are different, (p-val: {p_val})")
# else:
#     print(f"Yayyy, I'm right. They are the same, (p-val: {p_val})")



# oneway ANOVA
# f_stat, p_val = stats.f_oneway(data_0, data_1, data_2)
# print(f"p-value: {p_val}")



# correlation 
# r_stat, p_val = stats.pearsonr(data_0, data_3)
# print(f"Correlation coefficient: {r_stat} \n(p-value: {p_val})")



df = pd.read_excel("data.xlsx")
# print(df.head())

key_1 = df[df["Response"] == "Key1"]["Value"]
print(key_1)

key_2 = df[df["Response"] == "Key2"]["Value"]
print(key_2)

key_3 = df[df["Response"] == "Key3"]["Value"]
print(key_3)

plt.boxplot([key_1, key_2, key_3], 
            labels = ["Key 1", "Key 2", "Key 3"])

f_stat, p_val = stats.f_oneway(key_1, key_2, key_3)
plt.text(3.5, 2.15, f"p-value: {p_val: .3f}", 
         ha= "right", 
         va= "bottom", 
         fontsize = 10)

plt.show()