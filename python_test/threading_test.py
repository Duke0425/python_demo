"""
    python中threading模块

    1. 守护进程/线程
        设置daemon = True, Setdaemon = function
        - 当守护线程结束时, 会杀掉线程
    2. 线程阻塞
        join()
        在当前线程等待另一线程的结束
"""

import threading
import logging
import time
import numbers
import dis
from concurrent.futures import ThreadPoolExecutor


def thread_function(aPra):
    logging.info(f"Thread: {aPra} start")
    time.sleep(2)
    logging.info(f"Thread: {aPra} finish")


class ThreadTest:

    @staticmethod
    def single_thread(aFunction, afunctinPra):
        """
            单线程例子
        """
        thread_one = threading.Thread(target=aFunction, args=(afunctinPra, ), daemon=True)
        logging.info("Main: before running thread")
        thread_one.start()
        logging.info("Main: wait for the thread to finish")
        # thread_one.join()
        logging.info("Main: all done")
    
    @staticmethod
    def multi_thread_native(aFunction, aThreadNums=2):
        """
            多线程例子
        """
        threads = []
        for _ in range(aThreadNums):
            thread_one = threading.Thread(target=aFunction, args=(_, ))
            threads.append(thread_one)
            thread_one.start()

        for index, thread in enumerate(threads):
            logging.info("Main    : before joining thread %d.", index)
            thread.join()
            logging.info("Main    : thread %d done.", index)

    @staticmethod
    def use_thread_pool_executer(aFunction, aPra, aMaxWorker=3):
        """
            使用ThreadPoolExecuter
                : 使用该模块启动多线程, 不会忘记join线程
        """
        with ThreadPoolExecutor(max_workers=aMaxWorker) as executor:
            executor.map(aFunction, aPra)

    @staticmethod
    def use_thread_pool_executer_submit(aFunction, aMaxWorker):
        """
            使用ThreadPoolExecuter submit方法
                :submit方法接受位置参数和关键字参数
        """
        with ThreadPoolExecutor(max_workers=aMaxWorker) as executor:
            for index in range(aMaxWorker):
                executor.submit(aFunction, index)


class FakeDatabase:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        with cls._lock:
            cls._instance = super().__new__(cls)
            return cls._instance

    def __init__(self, aNumbers = 1090):
        self.myDataNumbers = aNumbers

    def __add__(self, aValue):
        if isinstance(aValue, numbers.Number):
            self.myDataNumbers += aValue
            return self

    def __repr__(self):
        return f"DataNumbers: {self.myDataNumbers}"

    def __str__(self):
        return f'ohhh shiiiiiit'

    def update(self, aThread):
        with self._lock:
            logging.info(f"Thread {aThread} starting addd")
            localCopy = self.myDataNumbers
            localCopy += 1
            time.sleep(0.1)
            self.myDataNumbers = localCopy
            logging.info(f"Thread {aThread} finishing addd")

def inc(x):
    x += 1

def dead_lock_simple():
    # l = threading.RLock()
    l = threading.Lock()
    print("before first acquire")
    l.acquire()
    print("before second acquire")
    l.acquire()
    print("acquired lock twice")


if __name__ == '__main__':
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main: before creating thread")

    # ThreadTest.single_thread(thread_function, 1)
    # ThreadTest.multi_thread_native(thread_function, aThreadNums=3)
    # ThreadTest.use_thread_pool_executer(thread_function, ("one", "two", "Three", 'four'), aMaxWorker=4)

    """
        1. 创建一个单例的假数据库类
        2. 创建多线程, 调用update函数(函数中使用函数变量保存对象属性值, 并且进行短时间的延时), 使对象属性myDataNumbers + 1
            ! 结果: 最后的属性值错乱
            * 原因: 每一个线程保存有自己的函数变量值, 当进行延时时, 操作系统会调用另一线程, 调用update函数, 同时 /
            *           复制myDataNumbers属性值, 最后延时结束, 多线程产生的值已经错乱, 最后赋值给myDataNumbers的值错乱

            TODO 那么如果是全局的值, 不是local变量, 会错乱吗. 使用+=1 会错乱吗?
            --> 使用REPL(交互式解释器)查看+=1 的处理步骤
                0 LOAD_FAST                0 (x)
                2 LOAD_CONST               1 (1)
                4 INPLACE_ADD
                6 STORE_FAST               0 (x)
                8 LOAD_CONST               0 (None)
                10 RETURN_VALUE
                * 通过dis模块能够看到 就算是+= 1 操作系统也有多个步骤, 如果操作系统换出这个线程并且运行同样修改另一个线程
                *    那么这个线程恢复的时候, 将会用不正确的值覆盖
                ! 很少会发生这样的竞争条件，但请记住，经过数百万次迭代的罕见事件很可能会发生。这些竞争条件的罕见性使得它们比常规错误更难调试。

        
    """

    fakeDatabaseSingleton = FakeDatabase(aNumbers=1000)
    fakeDatabaseSingleton += 3

    ThreadTest.use_thread_pool_executer_submit(fakeDatabaseSingleton.update, 3)
    logging.info(f"Main: Ending dataNumber -->{fakeDatabaseSingleton.myDataNumbers}")

    dis.dis(lambda x: x + 1)
    dis.dis(inc)
    """
        如何解决和避免资源竞争条件:  一次只允许一个线程进入代码的读取-修改-写入部分
        Python使用lock (其他语言称为Mutex 或者 Mutually Exclusion)
        * 执行此操作的基本功能:
            1. .acquire(): 获取锁对象
            2. .release(): 释放锁
            如果锁已被持有, 调用线程将等待直到它被释放. 如果锁不被释放, 那么程序将会被卡住(使用with上下文语法, 避免忘记释放锁)

        ! DeadLock : 当Lock已被获取, 则第二次调用.acquire()将等到调用的线程.release()
            可以从dead_lock_simple函数的运行结果来看, 两次对锁的来连续获取会导致死锁
            Python中RLock可以避免这种情况的死锁, 但是有多少个acquire, 需要有对应数量的release

    """
    dead_lock_simple()

    """
        生产者-消费者线程
    """
