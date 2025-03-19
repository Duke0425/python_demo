"""
functools.cache: 此装饰器实现了备忘, 能够将耗时的函数得到的结果保存起来, 避免传入相同的参数重复计算
嵌套装饰器, 下方的函数调用类似于 functools.caches(block(fibonacci))

对于长期运行的进程, functools 可能耗尽所有可用内存, @cache更适合短期运行的命令行脚本使用, 对于长期运行的进程.推荐
使用functools.lru_cache , 并合理设置maxsize参数/typed参数, maxsize参数设置最多可以缓存多少条目, 缓存满了之后, 最不常用的条目将会被丢弃, 为新条目腾出空间
. 为了获得最佳性能, 应将maxsize设为2的次方. typed默认为false, 如果设置为True, 将会区分参数的类型进行缓存, 比如1和1.0
"""

import functools
from use_decorator import clock

@functools.lru_cache(maxsize=128, typed=True)
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@functools.singledispatch
def foo_test(obj: object):
    content = str(obj)
    return content

@foo_test.register
def _(n: bool) ->str:
    return f'{n}'

@foo_test.register
def _(n: float) ->str:
    return f'{n}'

@foo_test.register
def _(n: int) ->str:
    return f'{n}'

@foo_test.register
def _(n: str) ->str:
    return f'{n}'

if __name__ == '__main__':
    print(fibonacci(10))
    foo_test(True)
    foo_test(2.1)
    foo_test(1)
    foo_test('real')
