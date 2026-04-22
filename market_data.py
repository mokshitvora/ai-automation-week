from nsepython import nse_eq, nifty_quote
import requests

def get_market_data():
    try:
        url = "https://www.nseindia.com/api/allIndices"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Referer": "https://www.nseindia.com"
        }
        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)
        response = session.get(url, headers=headers)
        data = response.json()
        
        nifty = next(i for i in data["data"] if i["index"] == "NIFTY 50")
        vix = next(i for i in data["data"] if i["index"] == "INDIA VIX")
        
        return {
            "current_price": nifty["last"],
            "percentage_change": nifty["percentChange"],
            "fifty_day_moving_average": "N/A",
            "two_hundred_day_moving_average": "N/A",
            "fiftytwo_week_high": nifty["yearHigh"],
            "fiftytwo_week_low": nifty["yearLow"],
            "vix_level": vix["last"]
        }
    except Exception as e:
        return {
            "current_price": "N/A",
            "percentage_change": "N/A",
            "fifty_day_moving_average": "N/A",
            "two_hundred_day_moving_average": "N/A",
            "fiftytwo_week_high": "N/A",
            "fiftytwo_week_low": "N/A",
            "vix_level": "N/A"
        }