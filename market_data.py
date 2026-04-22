import yfinance as yf

def get_market_data():
    try:
        current_nifty = yf.Ticker("^NSEI")
        current_vix = yf.Ticker("^VIX")
        info = current_nifty.info
        return {
            "current_price": info["regularMarketPrice"],
            "percentage_change": info["regularMarketChangePercent"],
            "fifty_day_moving_average": info["fiftyDayAverage"],
            "two_hundred_day_moving_average": info["twoHundredDayAverage"],
            "fiftytwo_week_high": info["fiftyTwoWeekHigh"],
            "fiftytwo_week_low": info["fiftyTwoWeekLow"],
            "vix_level": current_vix.info["regularMarketPrice"]
        }
    except Exception:
        # Fallback when Yahoo Finance rate limits
        return {
            "current_price": "unavailable - Yahoo Finance blocked",
            "percentage_change": "N/A",
            "fifty_day_moving_average": "N/A",
            "two_hundred_day_moving_average": "N/A",
            "fiftytwo_week_high": "N/A",
            "fiftytwo_week_low": "N/A",
            "vix_level": "N/A",
            "note": "Market data unavailable from cloud. AI will rely on news search instead."
        }
