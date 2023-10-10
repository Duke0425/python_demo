import asyncio
import logging
import time
import concurrent

"""
    * 1. 并发运行任务: asyncio.gather(*aw) 方法, 将多个协程任务或者未来添加到集合中, 并发开始运行, 并且
                接受到所有协程任务的返回值                
    * 2. 屏蔽取消: asyncio.shield(aw) 保护等待对象不会被取消, 如果aw是协程,将会自动安排为任务

    * 3. 等待超时: asyncio.wait_for(aw, timeout): 等到aw超时完成

    * 4. 等待原语: asyncio.wait(aws, *, timeout, return_when=ALL_COMPLETED)
    *              asyncio.as_completed(aws, * , timeout = None)

    * 5. 从其他线程调度: asyncio.run_coroutine_threadsafe(coro, loop): 将协程提交给给定的事件循环, 线程安全

    ! 6. 在线程中运行: asyncio.to_thread(func, /, *args, **kwargs)

    * 7.
"""
# TODO gather
async def factorial(aName, aNumber):
    fa = 1
    for i in range(2, aNumber + 1):
        logging.info(f"Task {aName}: Compute factorial({aNumber}), currently i={i}...")
        fa *= i
        await asyncio.sleep(1)
    logging.info(f"Task {aName}: factorial({aNumber}) = {fa}")
    return fa

async def main():
    L = await asyncio.gather( 
        factorial("A", 2),
        factorial("B", 5),
        factorial("C", 3),
        factorial("D", 9),
    )
    print(L)

# TODO shiled
async def something():
    await asyncio.sleep(2)
    logging.info("something coro finished!")

async def shield_example():
    await asyncio.shield(something())

# TODO wait_for
async def wait_for_example_main():
    try:
        await asyncio.wait_for(something(), 1.0)
    except asyncio.TimeoutError:
        logging.info("Timeout")

# TODO wait
async def wait_example_main():
    coro = asyncio.create_task(something())
    done, pending = await asyncio.wait({coro})
    if coro in done:
        logging.info("Finished")

# TODO to_thread !(Python3.9新功能)
def block_io(aTime):
    time.sleep(aTime)

async def to_thead_example():
    logging.info(f"started main at {time.strftime('%X')}")
    L = asyncio.gather(
        something(),
        asyncio.to_thread(block_io(3))
    )
    logging.info(f"finished main at {time.strftime('%X')}")

# TODO 基于生成器的协程
@asyncio.coroutine
def old_style_coroutine():
    yield from asyncio.sleep(1, result=2)

async def example_main():
    await old_style_coroutine()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, datefmt="%H:%M:%S")
    logging.getLogger("asyncio")
    # asyncio.run(main()) # gather方法

    # asyncio.run(shield_example()) # shield方法
    # asyncio.run(wait_for_example_main()) # wait_for方法
    # asyncio.run(wait_example_main())# wait方法
    # asyncio.run(to_thead_example())# to_thead (3.9中的新功能)

    # ! run_coroutine_threadsafe
    # coro = asyncio.sleep(4, result=3)
    # future = asyncio.run_coroutine_threadsafe(coro, loop=asyncio.get_event_loop())
    
    # try:
    #     result = future.result(timeout = 1)
    # except concurrent.futures.TimeoutError:
    #     print('The coroutine took too long, cancelling the task...')
    #     future.cancel()
    # except Exception as exc:
    #     print(f'The coroutine raised an exception: {exc!r}')
    # else:
    #     print(f'The coroutine returned: {result!r}')

    
    asyncio.run(example_main())