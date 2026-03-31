import asyncio
import nodriver
import aiohttp

DISCORD_WEBHOOK_URL = "xyz"

WATCHLIST = [
  {
    "name": "bandit.camp",
    "url": "https://bandit.camp",
    "text": "placeholder"
  }
]

async def send_discord_webhook(content: str) -> None:
  payload = {
    "content": content
  }
  try:
    async with 

  
