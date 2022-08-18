import logging

"""
    * 一. 异步IO


    并发: 是指多个任务能够以重叠的方式运行(threading模块)
        - 用途: 处理IO密集型任务(主要等待输入和输出, 大量IO请求的任务类型)
        - 
    并行: 同时执行多个操作. mutilprocessing是实现并行的一种手段
        - 用途: 处理cpu密集型任务(计算机内核需要大量工作的任务(循环以及数学计算))
        * 1. generator
            生成器是运行我们暂停python函数的对象. 使用关键字yield来实现
            * 与生成器通信
                .send(value): yield调用时, 返回的值为value
                .throw(Exception()): 在yield调用同一位置, 抛出异常
            * 从生成器回去返回值
            * Python3.4 新增关键字 yield from : 能够在生成器创建生产器, 就想隧道一样. 将最里面的数据来回传递到最外部的生成器, 为生成器带了新的含义 协程
        * 2. 协程
            ? 什么是协程:
                - 协程是可以在运行时停止和恢复的函数
                - Python中使用关键字 async def 定义.
                - 和生成器类似, await(Python3.5之前使用yield from), 我们可以创建生成器完全相同的方式的创建协程
                - 就像所有的生成器和迭代器拥有__iter__方法一样. 所有的协程拥有__await__方法允许协程在任何时候 await coro 时调用
            在asyncio中除了协程函数, 还有两个重要的对象 tasks和futures
            ? futures
                - futures是一个有__await__方法的对象, 工作是保持一个肯定的状态和结果, 有以下三种状态
                    1. PENDING - future 没有任何的结果和异常
                    2. CANCELLED - future 已被取消: 使用fut.cancel()
                    3. FINISHED - future 结束, 如果是结果使用 fut.set_result(). 如果是异常使用 fut.set_exception()
                    - 返回的结果, 也是一个Python的对象, 而且拥有一个方法 add_done_callback(): 此方法允许在task结束的时候被调用
                    (无论抛出异常还是正常结束)
            ? Tasks
                - 任务对象是特殊的future, 包裹着协程, 并与最内层和最外层协程进行通信, 每次协程await future时 future都会一路传回给任务
                    (就像yield from 一样), 任务会接受到.
                - 任务将会绑定到future, 它将会通过在future中调用add_done_callback(). 当future对象即将结束时, 无论是CANCELLED, 或者是
                    Exception异常的抛出, 或者得到正常的结果. 任务的回调将会被调用, 将恢复存在

                
"""

def generator_simple():
    val = yield 1
    logging.info(f"return val {val}")
    yield 2
    yield 3
    return 'end of this generator'

def inner():
    inner_result = yield 2
    logging.info(f"inner {inner_result}")
    return 3

def outer():
    yield 1
    val = yield from inner()
    logging.info(f"outer {val}")
    yield 4


class GenTest:
    def __init__(self, aGenerator):
        self.myGen = aGenerator

    def valueGetTest(self):
        try:
            for _ in range(10):
                value = next(self.myGen)
                logging.debug(f"get generator value {value}")
        except:
            logging.info("generator empty")

    def sendAndThrowMethodTest(self):
        # * 与生成器通信
        logging.info(f"sendAndThrowMethodTest: {next(self.myGen)}")
        logging.info(f"sendAndThrowMethodTest: {next(self.myGen)}")
        value = self.myGen.send("one")
        logging.info(f"sendAndThrowMethodTest: {value}")
        # self.myGen.throw(Exception())
        # logging.info(f"sendAndThrowMethodTest: {next(self.myGen)}")

    def getGenRetunValue(self):
        # * 从生成器获取返回值
        try:
            for _ in range(10):
                next(self.myGen)
        except StopIteration as exec:
            logging.info(f"getGenRetunValue: Get the return value [{exec.value}] of generator")

async def inner_simple():
    return 1

async def outer_simple():
    await inner_simple()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, datefmt="%H:%M:%S")
    # TODO:生成器获取值, 生成器send throw方法使用, 生成器返回值获取
    # genTest = GenTest(generator_simple())
    # genTest.valueGetTest()
    # genTest.sendAndThrowMethodTest()
    # genTest.getGenRetunValue()

    # TODO: yield from的使用
    genTestSimple = GenTest(outer()) 
    genTestSimple.sendAndThrowMethodTest()
