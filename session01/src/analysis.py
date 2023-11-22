import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("temp/output2.csv")

df = df.sort_values("comment", ascending=True)

df["fraction"] = df["comment"] / df["size"]

df["package"] = df["path"].apply(lambda x: "/".join(x.split("/")[:-1]))

df = df.groupby("package")["comment"].sum()

df = df.sort_values(ascending=False)

print(df)

#df = df.sort_values("fraction", ascending=False)
#print(df)

#print(df.iloc[0,0])

