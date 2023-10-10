import asyncio
import time 
import random
import logging
import sys
"""
异步IO设计模式: 链接协程(Chain Coroutinue)

    协程的一个关键的特性是它们可以连接到一起(一个协程对象是可以等待的, 所以另一个协程可以 await), 所以允许将程序分为更小, 可管理的, 可回收的协程
"""

async def part_one(aNum):
    timeNum = random.randint(0, 10)
    print(f"part1: ({aNum}) sleeping for {timeNum} seconds.")
    await asyncio.sleep(timeNum)
    result = f"result{aNum}"
    print(f"Returning part1({aNum}) == {result}.")
    return aNum

async def part_two(aNum):
    timeNum = random.randint(0, 10)
    print(f"part2: ({aNum}) sleeping for {timeNum} seconds.")
    await asyncio.sleep(timeNum)
    result = f"result{aNum}"
    print(f"Returning part2({aNum}) == {result}.")
    return aNum

async def chain(aNum):
    logging.info("chain begin")
    start = time.perf_counter()
    logging.info("wait ===one==")
    p_one_result = await part_one(aNum)
    logging.info("wait =***two**=")
    p_two_result = await part_two(aNum)
    end = time.perf_counter() - start
    logging.info(f"-->Chained result{aNum} => {p_two_result} (took {end:0.2f} seconds).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, datefmt="%H:%M:%S")

    command_line_para = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])

    begin_time = time.perf_counter()
    asyncio.run(main(*command_line_para))
    wasted_time = time.perf_counter() - begin_time

    logging.info(f"The code run time is {wasted_time}")
