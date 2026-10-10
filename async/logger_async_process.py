import asyncio
import threading

import time 

def back_ground_worker():
  while True:
    time.sleep(1)
    print(f"logging the system health")
    
async def fetch_oders():
  await asyncio.sleep(3)
  print("Oder fetched ")
  
threading.Thread(target=back_ground_worker , daemon = True).start()

asyncio.run(fetch_oders())


import asyncio

async def fetch_score(player_name, delay):
    print(f"Fetching score for {player_name}...")
    await asyncio.sleep(delay)
    score = len(player_name) * 10  # Just some dummy calculation
    print(f"Got score for {player_name}!")
    return score

async def main():
    # We want to fetch scores for three players concurrently
    # Player 1 takes 1s, Player 2 takes 3s, Player 3 takes 2s
    
    # YOUR TURN: How would you use asyncio.gather here 
    # to capture all three returned scores into a list?
    socres = asyncio.gather(
      fetch_score("Player1" , 1),
      fetch_score("Player2" , 3),
      fetch_score("Player3" , 2)
    )
    print(socres)

asyncio.run(main())