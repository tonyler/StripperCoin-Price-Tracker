import requests
import os
from dotenv import load_dotenv
load_dotenv()
import minswap.pools

def get_price(price, Ada):
    pool_id = os.environ.get("POOL_ID")
    try:
        price = float((minswap.pools.get_pool_by_id(pool_id).price)[0])
    except Exception as e:
        print ("MinSwap error: ",e)

    try:
        url = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd")
        data = url.json()
        Ada = float(data["cardano"]["usd"])

    except Exception as e:
        print ("Coingecko ADA Api Error: ",e)

    return price, Ada

