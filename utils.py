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
    url = f'https://tnlink.in/api'
    params = {'api': '63d2f2708e0cb0a9904185e967f224807337af6e',
              'url': link,
              }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            if data["status"] == "success":
                return data['shortenedUrl']
            else:
                return f"Error: {data['message']}"
            
 
