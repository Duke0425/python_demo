"""
    函数的主体中包含yield 关键字, 则此函数对象为一个生成器
"""

def gen_nums():
    print("start")
    yield 1
    print("continue")
    yield 2
    print("finished")

"""
    yield from : 从子生成器中产出
    重要作用: 建立子生成器与客户之前的直接联系, 绕过委托生成器。 把生成器用作协程时， 这种联系就变得十分重要， 它不仅能够产出值， 而且还利用客户代码提供的值。
"""

def use_yield_from_key():
    yield "a"
    yield "b"
    yield from gen_nums()
    yield "c"

def main():
    # for num in gen_nums():
    #     print(f"->{num}")

    # nums_generator = gen_nums()
    # while True:
    #     next(nums_generator)
    for num in use_yield_from_key():
        print(f"->{num}")

if __name__ == '__main__':
    main()
