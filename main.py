import asyncio 

# Coroutine functions
# is a wrapped way of a function 

# we need to start an event loop to run an async function

# we need to create a task to run parallel functions 

async def main():
    print('here in main')
    
    task = asyncio.create_task(foo("this is an async function"))
    await asyncio.sleep(0.5)
    print("finished in main")


async def foo(text):
    print(text)
    await asyncio.sleep(10)
    

# we pass a coroutine function    
asyncio.run(main())





    
