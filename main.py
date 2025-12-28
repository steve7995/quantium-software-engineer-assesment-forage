import  pandas  as pd

# Reading the given three datasets
df1 = pd.read_csv("./daily_sales_data_0.csv")
df2 = pd.read_csv("./daily_sales_data_1.csv")
df3 = pd.read_csv("./daily_sales_data_2.csv")

# filtering only pink morsel from all three datasets
df1 = df1[df1["product"]=="pink morsel"]
df2 = df2[df2["product"]=="pink morsel"]
df3 = df3[df3["product"]=="pink morsel"]


# adding all datasets and converting price into a float and calculating final sales
# sales = price * quantity
final_df = pd.concat([df1,df2,df3],ignore_index=True)
final_df["price"] = final_df["price"].str.replace("$","",regex=False).astype(float)
final_df["sales"] = final_df["price"]*final_df["quantity"]

# removing all columns except date region and sales
final_df = final_df.drop(columns=["product","price","quantity"])

final_df  = final_df.sort_values("date")


# exporting to csv for further visualization
final_df.to_csv("pink_morsel_sales.csv", index=False)

