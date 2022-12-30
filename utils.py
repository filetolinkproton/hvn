#This Bot is heavily modified for heaven exclusively By TargetX25 So he deserve a big piece of credits too.

import aiohttp
import asyncio
import os

####################  Tnlink  ####################

async def get_shortlink(link):
    https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)
    url = f'droplink.co'
    params = {'api': 'c154af6fce35ad10d4ebb8fb47cee0d092d065c2',
              'url': link,
              }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            if data["status"] == "success":
                return data['shortenedUrl']
            else:
                return f"Error: {data['message']}"
            
 
