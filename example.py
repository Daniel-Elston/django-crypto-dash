# My async example
import asyncio

async def worker(event, numbers):
    print('Worker is waiting for the event to be set')
    await event.wait()
    print('Event is set, worker proceeds with processing data')
    processed_numbers = [number * 2 for number in numbers]
    print(f"Processed numbers: {processed_numbers}")

async def main():
    event = asyncio.Event()

    # Initial list
    numbers = [1, 2, 3, 4, 5]
    print(f"Main is starting with numbers: {numbers}")

    # Schedule worker, it will wait until the event is set
    worker_task = asyncio.create_task(worker(event, numbers))

    # Simulate some operation eg. processing
    print('Main is performing some operations...')
    await asyncio.sleep(5)  # Simulate time-consuming task
    
    print('Main is setting the event')
    await asyncio.sleep(5)  # Simulate time-consuming task
    event.set()

    # Wait for the worker task to complete
    await worker_task

asyncio.run(main())
