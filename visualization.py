import  pandas as pd
from dash import Dash,dcc,html
import  plotly.express as px

df = pd.read_csv("pink_morsel_sales.csv")

df["date"]  = pd.to_datetime(df["date"])
df = df.sort_values("date")

# daily wise sales
daily_total = df.groupby("date",as_index=False)["sales"].sum()
app = Dash(__name__)


fig = px.line(daily_total, x="date", y="sales", title="Pink Morsel — Daily Sales")

app.layout = html.Div([
    html.H1("Pink Morsel Sales"),
    dcc.Graph(id = "sales-line",figure = fig)]
)

if __name__ == "__main__":
    app.run(debug=True)