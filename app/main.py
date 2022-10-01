

from fastapi import FastAPI, Query

from yahoo_search import YahooSearch
from yahoo_data import YahooData

import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# this shows the query is not requied str | None
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# query required
@app.get("/search/isin/")
def read_item(q: str | None = Query(default=None, max_length=50)):
    results = {}
    if q:
        results = YahooSearch.get_by_isin(q)
    return results


# query return all daily data 
@app.get("/data-management/{symbol}/all-market-history")
def read_item(symbol: str):
    results = {}
    df: pd.DataFrame  = YahooData.get_all_market_data(symbol)
    return df.to_json(orient='index')

# query return all daily data 
@app.get("/data-management/{symbol}/latest")
def read_item(symbol: str):
    results = {}
    return YahooData.get_latest_market_data_price(symbol)

