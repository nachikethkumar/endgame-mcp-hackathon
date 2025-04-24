import os
import asyncio
import aiohttp
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

MASA_BASE_URL = os.getenv("MASA_BASE_URL", "https://data.dev.masalabs.ai")
MASA_API_KEY = os.getenv("MASA_DATA_API_KEY")

if MASA_API_KEY is None:
    raise EnvironmentError("MASA_DATA_API_KEY not found in .env!")

# Initialize FastMCP server
mcp = FastMCP("CryptoNewsScraper", settings={})

HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {MASA_API_KEY}",
}


async def _post(session: aiohttp.ClientSession, endpoint: str, json_data: dict) -> dict:
    url = f"{MASA_BASE_URL}{endpoint}"
    async with session.post(url, json=json_data, headers=HEADERS) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _get(session: aiohttp.ClientSession, endpoint: str) -> dict:
    url = f"{MASA_BASE_URL}{endpoint}"
    async with session.get(url, headers=HEADERS) as resp:
        resp.raise_for_status()
        return await resp.json()


@mcp.tool()
async def search_crypto_news(crypto_name: str, max_results: int = 10) -> list[dict]:
    """Search the MASA API for latest crypto news related to a specific crypto coin."""
    async with aiohttp.ClientSession() as session:
        start_payload = {"query": crypto_name, "max_results": max_results}
        start_resp = await _post(session, "/api/v1/search/live/news", start_payload)
        job_id = start_resp.get("uuid")
        if not job_id:
            raise RuntimeError("Failed to start crypto news search job.")

        for _ in range(30):
            status_resp = await _get(session, f"/api/v1/search/live/news/status/{job_id}")
            if status_resp.get("status") == "done":
                break
            await asyncio.sleep(2)
        else:
            raise TimeoutError(f"Crypto news search job {job_id} did not complete in time.")

        result_list = await _get(session, f"/api/v1/search/live/news/result/{job_id}")
        return result_list


@mcp.tool()
async def fetch_crypto_news(crypto_name: str, max_results: int = 10) -> str:
    """Fetch crypto news without sentiment analysis."""
    news_list = await search_crypto_news(crypto_name, max_results)
    if not news_list:
        return "No news articles found."

    news_titles = [news.get("title", "No Title") for news in news_list]
    return "\n".join(news_titles)


if __name__ == "__main__":
    mcp.run()
