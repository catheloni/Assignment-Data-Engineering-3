import requests
import pandas as pd


def get_eth_stats():
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": "ETHUSDT", "interval": "1m", "limit": 60}

    response = requests.get(url, params=params)
    data = response.json()

    # Convert directly to a DataFrame for cleaner handling
    df = pd.DataFrame(
        data,
        columns=[
            "open_time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_asset_volume",
            "trades",
            "taker_buy_base",
            "taker_buy_quote",
            "ignore",
        ],
    )

    # Convert price columns to float
    df[["high", "low"]] = df[["high", "low"]].astype(float)

    # Calculate min and max
    min_price = df["low"].min()
    max_price = df["high"].max()

    print(f"--- ETH/USDT Last 60 Minutes ---")
    print(f"Minimum Price: ${min_price:,.2f}")
    print(f"Maximum Price: ${max_price:,.2f}")


if __name__ == "__main__":
    get_eth_stats()
