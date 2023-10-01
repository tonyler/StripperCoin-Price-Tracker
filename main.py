import discord
import asyncio
import os
from priceAPI import get_price
from ranstatus import random_status

intents = discord.Intents.default()
intents.presences = True

client = discord.Client(intents=discord.Intents.default())



async def send_update(price,unit):
        price = round(price,4)
        nickname = f'{price}₳'
        status=random_status()
        guild = client.get_guild(800875066182205490)

        if guild:
            try:
                await guild.me.edit(nick=nickname)
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

                print(price,"₳",end=" ")
                print(status,"\n******************")

            except Exception as e:
                print(f"An error occurred while changing nickname: {repr(e)}")
        else:
            print("The bot is not a member of the specified guild or cannot access it.")


@client.event
async def on_ready():

        Stripper = 0
        Ada = 0

        while True:
            Stripper, Ada = get_price (Stripper,Ada)
            price = Stripper
            await send_update (price, "₳")
            await asyncio.sleep (120)

bot_key = os.environ.get("DISCORD_KEY")
client.run(bot_key)


