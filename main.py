import asyncio
import nodriver
import aiohttp

from aiohttp import ClientSession

DISCORD_WEBHOOK_URL = "xyz"

WATCHLIST = [
  {
    "name": "bandit.camp",
    "url": "https://bandit.camp",
    "text": "placeholder"
  }
]

async def send_discord_webhook(session: ClientSession, content: str) -> None:
  payload = {
    "content": content
  }
  
  try:
    session.post(DISCORD_WEBHOOK_URL, json=payload)
  except:
    pass

  
