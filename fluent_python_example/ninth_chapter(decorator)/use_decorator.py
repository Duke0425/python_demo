"""
装饰器是一个函数或者其他可调用对象
装饰器可以把被装饰的函数替换成别的函数
装饰器在加载模块时快速执行

! 函数装饰器在导入模块时立即执行, 而被装饰的函数只在显式调用时执行.

! 闭包是一个函数, 它保留了定义函数时存在的自由变量的绑定。 如此一来， 调用函数时， 虽然定义作用域不可用了
! 但是仍能使用那些绑定> 注意: 嵌套在其他函数中的函数才可能需要不在全局作用域的外部变量, 这些外部变量位于外层函数的局部作用域内.
"""
registry = []

def register(func):
    print(f"running register {func}")
    registry.append(func)
    return func

@register
def f1():
    print("running f1")

@register
def f2():
    print("running f2")

def f3():
    print("running f3")
"""
nonlocal 关键字: 作用是将变量标记为自由变量, 即便在函数中为变量赋予了新值. 
闭包中的保存的绑定也会随之更新.

! 变量查找逻辑: 
- 1. 在外层函数主体的局部作用域中找寻变量a
- 2. 再到模块全局作用域内读取a
- 3. 再从__builtins__.__dict__中读取
"""

global count
count = 100
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        print(count)
        return total / count

    return averager

"""
装饰器的典型行为: 把被装饰的函数替换成新函数, 新函数接受的参数与被装饰的函数一样, 而且通常会返回被装饰的函数返回的值
同时还会做一些额外的操作.

functools.wraps装饰器把相关属性从function身上复制到了clocked中. 此外这个新版还能正确处理关键字参数.
"""
import functools
import time
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        arg_str = ', '.join(repr(arg) for arg in args)
        elpased = time.perf_counter() - start_time
        print(f"[{elpased:.8f}s] {func.__name__} {arg_str} -> {result!r}")
        return result
    return clocked

"""
参数化clock装饰器, 让用户传入一个格式字符串, 控制被装饰的函数的输出.
"""

DEFAULT_FMT = '[{elasped:0.8f}s] {name}({args}) -> {_result}'
def para_clock(fmt=DEFAULT_FMT):
    def decorator(func):
        def clocked(*_args):
            start_time = time.perf_counter()
            _result = func(*_args)
            elasped = time.perf_counter() - start_time
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorator

"""
基于类的参数装饰器
"""
class para_clock_cls:
    def __init__(self, fmt = DEFAULT_FMT) -> None:
        self.fmt = fmt
    
    def __call__(self, func):
        def clocked(*_args):
            start_time = time.perf_counter()
            _result = func(*_args)
            elasped = time.perf_counter() - start_time
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            print(self.fmt.format(**locals()))
            return _result
        return clocked

@para_clock()
def snooze(seconds):
    time.sleep(seconds)

@para_clock_cls('[{elasped:0.8f}s] {name} += ({args}) -> {_result}')
def snooze_2(seconds):
    time.sleep(seconds)

def main():
    # avg = make_averager()
    # avg(12)

    for i in range(3):
        snooze(.123)

    for i in range(3):
        snooze_2(i)

if __name__ == '__main__':
    main()

"""
总结: Python 装饰器符合设计模式一书中对装饰器模式的一般描述: 动态的给一个对象添加一些额外的职责. 就扩展功能而言, 装饰器模式比子类化更加灵活
1. 一般来说, 实现装饰器模式最好是用来类表示装饰器和要包装的组件
2. 函数装饰器的最佳实践就是始终使用 functools.wraps
3. nonlocal 关键词作用: 重新绑定不在全局作用域也不在局部作用域的变量名称

"""