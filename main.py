from fastapi import FastAPI
from analyzer import analyze
from market_data import get_market_data
app = FastAPI()
@app.get("/analyze")
def analyze_route():
    data = get_market_data()
    return analyze(data)