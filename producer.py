import aiohttp
import asyncio

API_KEY = "XO6KHCWT5Z5GBU2H"
BASE_URL = "https://www.alphavantage.co/query"

async def fetch_stock_price(session, symbol):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": API_KEY
    }
    async with session.get(BASE_URL, params=params) as response:
        data = await response.json()
        if "Time Series (5min)" in data:
            latest_time = list(data["Time Series (5min)"].keys())[0]
            price = data["Time Series (5min)"][latest_time]["1. open"]
            return {symbol: price}
        else:
            return {symbol: "Error fetching data"}

async def main():
    stock_symbols = ["AAPL", "GOOGL", "TSLA"]  
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [fetch_stock_price(session, symbol) for symbol in stock_symbols]
            results = await asyncio.gather(*tasks)
            print(results)
            await asyncio.sleep(5)  

asyncio.run(main())
