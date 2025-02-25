import aiohttp
import asyncio

API_KEY = "S4NN5RB1IP5G10TO"  # Replace with your actual API key

async def fetch_stock(session, symbol):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",  # Get stock prices every 5 minutes
        "apikey": API_KEY
    }
    async with session.get(url, params=params) as response:
        data = await response.json()
        
        if "Time Series (5min)" not in data:
            print(f"Error fetching {symbol}: {data}")
            return None

        # Get the latest timestamp
        latest_timestamp = max(data["Time Series (5min)"].keys())
        latest_data = data["Time Series (5min)"][latest_timestamp]
        
        price = latest_data["1. open"]  # Get the latest price
        
        print(f"Fetched {symbol}: {price} at {latest_timestamp}")
        return symbol, float(price), latest_timestamp

async def get_stock_prices(symbols):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_stock(session, symbol) for symbol in symbols]
        stock_data = await asyncio.gather(*tasks)
        return [item for item in stock_data if item]  # Remove None values

async def main():
    symbols = ['AAPL', 'TSLA', 'GOOGL']  # List of stocks to track
    stock_data = await get_stock_prices(symbols)
    print("Final Data:", stock_data)  # Check the final result

if __name__ == "__main__":
    asyncio.run(main())
