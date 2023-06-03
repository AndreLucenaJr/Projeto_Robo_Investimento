import pandas as pd
import plotly.graph_objects as go


def createCandleGraph(data: pd.DataFrame):
    data['MA5'] = data.close.rolling(5).mean()
    data['MA20'] = data.close.rolling(20).mean()

    for i in range(len(data.index)):
        rowBefore = data.iloc[[i - 1]]
        row = data.iloc[[i]]
        if row["MA5"].item() >= row["MA20"].item() and rowBefore["MA5"].item() <= rowBefore["MA20"].item():
            print("5")
            print(row)
        if row["MA20"].item() >= row["MA5"].item() and rowBefore["MA20"].item() <= rowBefore["MA5"].item():
            print("20")
            print(row)
                
    # Creates graph based on received data
    graph = go.Figure(data=[go.Candlestick(x=data.time,
                                          open=data.open,
                                          high=data.high,
                                          low=data.low,
                                          close=data.close, name="CANDLE"),
                                          go.Scatter(x=data.time, y=data.MA5, line=dict(color='orange', width=1), name="MA5"),
                                          go.Scatter(x=data.time, y=data.MA20, line=dict(color='green', width=1), name="MA20")
                                          ])
    # Shows the graph in your browser
    graph.show()