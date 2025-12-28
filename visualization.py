import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("pink_morsel_sales.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# daily total sales
daily_total = df.groupby("date", as_index=False)["sales"].sum()

# daily sales by region
daily_by_region = df.groupby(["date", "region"], as_index=False)["sales"].sum()

app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "maxWidth": "900px",
        "margin": "auto",
        "padding": "20px"
    },
    children=[
        html.H1(
            "Pink Morsel Sales",
            style={"textAlign": "center"}
        ),

        dcc.RadioItems(
            id="region-radio",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={
                "textAlign": "center",
                "marginBottom": "20px"
            }
        ),

        dcc.Graph(id="sales-line")
    ]
)

@app.callback(
    Output("sales-line", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        fig = px.line(
            daily_total,
            x="date",
            y="sales",
            title="Pink Morsel — Daily Sales (All Regions)"
        )
    else:
        filtered_df = daily_by_region[daily_by_region["region"] == selected_region]
        fig = px.line(
            filtered_df,
            x="date",
            y="sales",
            title=f"Pink Morsel — Daily Sales ({selected_region.capitalize()})"
        )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        template="plotly_white"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)
