from collections import abc
from random import randint

class seq:

    def __init__(self) -> None:
        pass

    def __getitem__(self, key) -> None:
        print(">+", key)
        raise IndexError

def iterable_obj() -> None:
    # 实现了 __getitem__  并且可以从0开始迭代. 就是一个可迭代对象(iterator) 但是无法等同于abc.Iterable . 
    # 拥有__iter__方法可以肯定可迭代对象, 不管是实例还是class. 且是abc.Iterable
    s = seq()
    print(f"s is abc.Iterable type ? {'YES' if isinstance(s, abc.Iterable) else 'No'}")

def return_random_int() -> int:
    return randint(1,10)

def iter_func_use() -> None:
    iterator = iter(return_random_int, 1)
    for num in iterator:
        print(num)

def main() -> None:
    # iterable_obj()
    iter_func_use()

if __name__ == '__main__':
    main()