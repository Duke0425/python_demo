"""
    经典协程:
    协程其实就是生成器函数, 通过主体中含有yield关键字的函数创建, 协程对象就是生成器对象.
"""
from typing import Iterator, Generator

readings: Iterator[float]
# sim_taxi: Generator[Event, float, int]

"""
    # Generator[YieldTupe, SendType, ReturnType] -> 此参数类型与typing.Coroutine 相同
    ! typing.Coroutine 已弃用, collection.abc.Coroutine(python 3.9 起可用的泛型) 仅用于注解原生协程, 不能注解经典协程.
     经典协程的类型提示只能使用模糊不清的GeneratorGenerator[YieldTupe, SendType, ReturnType] 

     以下是一个简单计算平均数的协程, 可以观察到协程好处: 在协程暂停并且等待下一次调用.send期间, 无需使用实例属性或者闭包保持上下文。
     异步编程中， 把回调换成协程， 因为在多次激活之间，协程能够保持局部状态。

     一般不终止生成器, 因为一旦没有对生成器的有效引用, 生成器就会被当做垃圾回收掉. 
     如果想要显式终止协程, 可以调用.close()方法
"""

def averager() -> Generator[float, float, None]:
    total = 0
    count = 0
    average = 0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


def main():
    calGen = averager()
    next(calGen) # 预激协程， 或者使用.send(None) 进行激活. send只能在yield处暂停时接受发送的值.

    a = calGen.send(10)
    b = calGen.send(50)
    c = calGen.send(0)
    print(a, b, c)

if __name__ == '__main__':
    main()
