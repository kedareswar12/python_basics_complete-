import asyncio


async def brew(name):
  print(f"brewing the {name} chai ... ")
  await asyncio.sleep(2)
  print(f"the {name} is ready!")
  
async def main():
  await asyncio.gather(
    brew("Masala chai"),
    brew("Ginger chai"),
    brew("Elachi chai")
  )
  
  
asyncio.run(main())