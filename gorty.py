# bot.py
import asyncio
import os
import discord
from datetime import datetime
from mcstatus import JavaServer
from dotenv import load_dotenv

ip_list = ["192.168.1.221:25565",
        "192.168.1.221:25566"]
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    #await client.get_channel(996546379755311145).send('stinky, uhoh')

# ive never done threading before so if this is a sin: sorry!!
async def check_update(ips):
    await client.wait_until_ready()
    testint = 0
    while(True):
        print("help computer")
        serverStr = f'SERVER STATUS FOR GALA:\n-----updated {datetime.now().replace(microsecond=0).isoformat()}-----\n'
        for i in range(len(ips)):
            server = JavaServer.lookup(ips[i])
            status = server.status()
            channel = client.get_channel(996546379755311145)
            message = await channel.fetch_message(996589722799443999)
            testint = testint + 1
            serverStr = serverStr + f"* {ips[i]} has {status.players.online} players and replied in {status.latency:.2f} ms\n"
            await message.edit(content=serverStr)
            await asyncio.sleep(15) # raise later when testing good 

client.loop.create_task(check_update(ip_list))
client.run(TOKEN)