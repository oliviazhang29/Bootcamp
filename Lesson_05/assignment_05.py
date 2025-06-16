import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_excel("drawing_data.xlsx")

# print(df)

# plt.scatter(df["x"], df["y"], color = "teal", label = "Coordinates")

# plt.xlabel("X")
# plt.ylabel("Y")

# plt.show()

fig = px.scatter(df, 
                 title = "Game Data", 
                 x = "x", 
                 y = "y", 
                 color = "x", 
                 labels = {"x": "X coordinates", 
                           "y": "Y coordinates"})

fig.show()