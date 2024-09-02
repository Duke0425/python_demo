"""
    函数的主体中包含yield 关键字, 则此函数对象为一个生成器
"""

def gen_nums():
    print("start")
    yield 1
    print("continue")
    yield 2
    print("finished")

def main():
    for num in gen_nums():
        print(f"->{num}")

    nums_generator = gen_nums()
    while True:
        next(nums_generator)

if __name__ == '__main__':
    main()
