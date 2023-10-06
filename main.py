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
        try:
            await guild.me.edit(nick=nickname)
            print ("Nickname changed successfuly!✅")
        except Exception as e:
            print(f"An error occurred while changing nickname: {e}")



@client.event
async def on_ready():
        price = 0
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Minswap DEX"))
        while True:
            if guild in client.guilds:
                    price = get_price (price) #if there's an error, the bot will show 0 or the price of 2 minutes ago.
                    price = round(price,4)
                    print (f"New price: {price}₳")
                    
                    for guild in client.guilds:
                        print (f"Updating data for {guild.name}")
                        await send_update (price, guild.id)
            else:
                print ("The bot isn't a member of any server yet!)
                       
            print ("***************************")
            await asyncio.sleep (120)


bot_key = os.environ.get("DISCORD_KEY")
client.run(bot_key)


