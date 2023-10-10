"""
    Async IO 是一种并发编程设计
    1. 异步IO: 一种与语言无关的编程范式, 具有跨多种编程语言的实现
    2. async/ await : 两个新的关键字, 用于定义协程
    3. asyncio: 为运行和管理协程提供基础和API的Python包
    * 协程(专门的生成器函数)是Python异步IO中的核心

    * asyncio包被Python文档称为编写并发代码的库. 但是, 异步IO既不是线程, 也不是多进程. 更不是建立在这二者之上
    实际上, 异步IO是一种单线程, 单进程的设计: 它使用协作多任务(cooperative multitasking), 尽管在单个进程中使用单个线程, 但是异步IO
        给人一种并发的感觉. 协程可以同时进行调度,但他们的本质上不是并发的/
    ! 异步: 异步例程能够在等待其最终结果时"暂停", 同时让其他例程运行
    异步代码, 通过上面的机制, 方便了并发执行: 所以只是提供了并发的外观和感觉

    协程等待await 关键字参数的返回值, 使当前函数暂停.
    async def 定义协程, 可以使用return yield return 返回值.
        1. 使用await 或者 return 创建协程函数, 必须使用await 使用它来获取其结果
        2. yield 在块中使用不太常见, async def : yield . 这将创建一个异步生成器. 可以使用对其迭代async for.
        3. async def 定义的协程 不能使用yield from, 会引起SyntaxError 
"""
import logging
import asyncio
import time
import random

class SimpleAsynicTest:

    @classmethod
    async def count(cls):
        print("wait before")
        await asyncio.sleep(2)
        print("wait after")

    @classmethod
    async def async_main(cls):
        await asyncio.gather(cls.count(), cls.count(), cls.count())


class TestKeywordsInCor:

    @classmethod
    async def count(cls):
        await asyncio.sleep(1)
        return 2

    @classmethod
    async def test_default_keywords_one(cls):
        result = await cls.count()
        logging.info(f"test_default_keywords_one: return {result}")
        return result

    @classmethod
    async def test_default_keywords_two(cls):
        await asyncio.sleep(2)
        yield 2

    @classmethod
    async def test_default_keywords_three(cls):
        await cls.count()

    @classmethod
    async def test_error_keyword(cls):
        # yield from cls.count()
        pass

    @classmethod
    async def main(cls):
        async for i in cls.test_default_keywords_two():
                print(i)


class AsyncGEN:
    
    @classmethod
    @asyncio.coroutine
    def py34_coro(cls):
        yield from cls.foo()

    @classmethod
    async def py35_coro(cls):
        await cls.foo()
    
    @classmethod
    async def foo(cls):
        await asyncio.sleep(2)

    @classmethod
    async def main():
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, datefmt="%H:%M:%S")

    # s = time.perf_counter()
    # asyncio.run(SimpleAsynicTest.async_main())
    # elapsed = time.perf_counter() - s
    # print(f"{__file__} executed in {elapsed:0.2f} seconds.")


    # asyncio.run(TestKeywordsInCor.test_default_keywords_one()) # use await and return
    # asyncio.run(TestKeywordsInCor.main()) # use yield
    # asyncio.run(TestKeywordsInCor.test_default_keywords_three()) # use await
    # asyncio.run(TestKeywordsInCor.test_error_keyword()) # ! error use yield from 


    # asyncio.run(AsyncGEN.py34_coro())

