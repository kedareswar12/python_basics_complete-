import asyncio
from concurrent.futures import ProcessPoolExecutor

p = ProcessPoolExecutor()

def encrypt(data):
  return f"{data[::-1]}"

async def main():
  loop = asyncio.get_running_loop()
  with p as ProcessPool:
    result = await loop.run_in_executor(ProcessPool , encrypt , "credit_card_1234")
    print(result)
    
    
if __name__ == "__main__":
  asyncio.run(main())