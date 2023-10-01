import requests
import os
from dotenv import load_dotenv
load_dotenv()
import minswap.pools

def get_price(price):
    pool_id = os.environ.get("POOL_ID")
    try:
        price = float((minswap.pools.get_pool_by_id(pool_id).price)[0])
    except Exception as e:
        print ("MinSwap error: ",e)
        
    return price

