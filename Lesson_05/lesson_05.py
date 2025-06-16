import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_excel("data.xlsx")

print(df["Value"])


# data cleaning
df_clean = df.dropna()
print(df_clean)

df_fixed = df.fillna({"Response": "Unknown"})
df_fixed2 = df_fixed.fillna({"Value": 0})

# print(df_fixed2)

df_fixed_final = df_fixed2[df_fixed2["Trial"] >= 0]

# print(df_fixed_final)


# plot with matplotlib
plt.scatter(df["ID"], df["Value"], color = "teal", 
            label = "Value data")
average = df["Value"].mean()   # get the mean of the variable "Value"

plt.axhline(y = average, 
            color = "purple", 
            linestyle = "--", 
            label = f"average: {average:.2f}")

plt.legend()
plt.title("Value by ID")
plt.xlabel("ID")
plt.ylabel("Value (arb. units)")

plt.show()


# plot with plotly
fig = px.scatter(df,    # px creates an interactive html plot
                 title = "My Cool Plot",
                 x = "ID", 
                 y = "Value", 
                 color = "Response", 
                 labels = {"ID": "ID", 
                           "Value": "Value"})

fig.update_layout(showlegend=True)   # show legends

fig.write_image("cool_plot.png")   # save the plot
fig.show()