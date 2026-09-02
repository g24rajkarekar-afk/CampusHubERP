import aiohttp
import asyncio


async def fetch_data(session, url):
    async with session.get(url) as response:

        if response.status == 200:
            data = await response.json()
            return data

        return {"error": f"Request failed: {response.status}"}


async def fetch_multiple_apis():

    urls = [
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/users/2",
        "https://jsonplaceholder.typicode.com/users/3"
    ]

    async with aiohttp.ClientSession() as session:

        results = await asyncio.gather(
            *(fetch_data(session, url) for url in urls)
        )

    return results