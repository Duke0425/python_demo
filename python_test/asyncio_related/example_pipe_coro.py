import os
import asyncio
import time
import logging
import itertools as it
import random
import argparse

async def makeitem(size):
    return os.urandom(size).hex()

async def randsleep(aCaller):
    rNum = random.randint(0, 10)
    if aCaller:
        logging.info(f"{aCaller} sleeping for {rNum} seconds.")
    await asyncio.sleep(rNum)

async def produce(name: int, q: asyncio.Queue):
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):
        pass

async def consume(name: int, q: asyncio.Queue): 
    pass

async def main(aPro, aCon):
    queue = asyncio.Queue()
    producers = [asyncio.create_task(produce(num, queue)) for num in aPro]
    consumers = [asyncio.create_task(consume(num, queue)) for num in aCon]
    await asyncio.gather(*producers)
    await queue.join()
    for con in consumers:
        con.cancel()


if __name__ == '__main__':
    logging.BASIC_FORMAT(level=logging.DEBUG, datefmt="%H%M%S")
    random.seed(444)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--p",
        "--nprod",
        type=int,
        default=5
    )
    parser.add_argument(
        "--c",
        "--ncon",
        type=int,
        default=10
    )
    command_line_args =parser.parse_args()

    start_time = time.perf_counter()
    asyncio.run(main(**command_line_args.__dict__))
    elapsed_time = time.perf_counter()  - start_time

    logging.info(f"Program completed in {elapsed_time:0.5f} seconds.")