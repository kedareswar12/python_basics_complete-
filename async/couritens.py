# async def -> declares a coroutine , ok what is courotine? A coroutine is a special type of function that can pause its execution before reaching return, and it can indirectly pass control to another coroutine for some time. Coroutines are used for cooperative multitasking, allowing multiple tasks to run concurrently without the need for threads or processes.

# await -> of if the def is async then you can use the await and the await keyword is used to pause the execution of a coroutine until the awaited coroutine completes its execution. 

import asyncio

async def coroutine_example():
    print("Brewing the chai ...")
    await asyncio.sleep(2)  # Simulating a delay for brewing chai
    print ("Chai is ready!")
    
asyncio.run(coroutine_example())