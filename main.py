import asyncio
import nodriver
import aiohttp

from aiohttp import ClientSession

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1488512520749842524/lLl8IusI-Eqoa5MhKGEG2CP5AW-ksEQRFLnMEhbJJgRmx7psN2sj-ZsRZJ9bk74JRwMa"

WATCHLIST = [
  {
    "name": "bandit.camp",
    "url": "https://bandit.camp",
    "text": "i am boss"
  }
]

async def send_discord_webhook(session: ClientSession, content: str) -> None:
  payload = {
    "content": content
  }
  
  try:
    await session.post(DISCORD_WEBHOOK_URL, json=payload)
  except:
    pass

async def page_contains_text(tab, target_text: str) -> bool:
  try:
    html = await tab.get_content()
    
    return target_text.lower() in html.lower()
  except:
    return False

async def monitor_website(browser, session: ClientSession, website: dict) -> None:
  last_found_state = False
  
  tab = None
  
  while True:
    try:
      if tab is None:
        tab = await browser.get(website['url'])
        
        await tab.sleep(5)
        
      found = await page_contains_text(tab, website['text'])
      
      if found and not last_found_state:
        last_found_state = True
        
        await send_discord_webhook(session, f"@everyone A rain just started on [{self.name}](<{self.url}>)")
      elif not found and last_found_state:
        last_found_state = False
    except:
      tab = None
      
    await asyncio.sleep(15)

async def start_browser():
  browser = await nodriver.start(headless=False)
  
  return browser

async def run():
  browser = await start_browser()
  
  async with ClientSession() as session:
    tasks = [
      monitor_website(browser, session, website)

      for website in WATCHLIST
    ]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
  nodriver.run_until_complete(run())

  
