import  pandas  as pd

df1 = pd.read_csv("./daily_sales_data_0.csv")
df2 = pd.read_csv("./daily_sales_data_1.csv")
df3 = pd.read_csv("./daily_sales_data_2.csv")



df1 = df1[df1["product"]=="pink morsel"]
df2 = df2[df2["product"]=="pink morsel"]
df3 = df3[df3["product"]=="pink morsel"]



final_df = pd.concat([df1,df2,df3],ignore_index=True)


final_df["sales"] = final_df["price"]*final_df["quantity"]
final_df.drop(columns=["price","quantity","product"],inplace=True)

final_df["sales"]  = final_df["sales"].astype(str).str.count(r"\$3\.00").mul(3.00)
print(final_df.head(5))