import asyncio
import aiohttp

async def fetch_url(url , session):
  async with session.get(url) as response:
    print(f"Fethced the {url} with he status {response.status}")
    
async def main():
  urls = ["http://httpbin.org/delay/2"]*3
  async with aiohttp.ClientSession() as session:
    tasks = [fetch_url(url,session) for url in urls]
    await asyncio.gather(*tasks)
    
asyncio.run(main())