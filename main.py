import discord
import asyncio
import os
from minswap_price import get_price

intents = discord.Intents.default()
intents.presences = True
client = discord.Client(intents=discord.Intents.default())

async def send_update(price,server_id):
        nickname = f'{price}₳' #the price is in ADA
        guild = client.get_guild(server_id)

        if guild:
            try:
                await guild.me.edit(nick=nickname)
            except Exception as e:
                print(f"An error occurred while changing nickname: {repr(e)}")
        else:
            print("The bot is not a member of the specified guild or cannot access it.")


@client.event
async def on_ready():
        try:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Minswap DEX"))
            while True:
                    price = 0
                    price = get_price (price) #if there's an error, the bot will show 0 or the price 2 minutes ago.
                    price = round(price,4)
                    print (f"New price: {price}₳")

                    for guild in client.guilds:
                        print (f"Updating data for {guild.name}")
                        await send_update (price, guild.id)
                    print ("***************************")
                    await asyncio.sleep (120)
        except: 
            print ("The bot has not joined any discord server yet!")

bot_key = os.environ.get("DISCORD_KEY")
client.run(bot_key)


