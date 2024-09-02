import re
from collections.abc import Iterator

"""
迭代器, 实现了__iter__ 和 __next__ 方法的对象, 只能通过StopIteration 异常判断内部已空, 且迭代器使用后不能重置, 只能够重新构建
"""
match = re.compile(r'\w+')

class Sentence:

    def __init__(self, string: str) -> None:
        self.origin_string = string
        self.str_list = match.findall(string)

    def __getitem__(self, key) -> str:
        return self.str_list[key]
    
    def __len__(self) -> int:
        return len(self.str_list)

def use_iterator():
    s = Sentence("I'm a God!")
    iterator = iter(s)
    if isinstance(iterator, Iterator):
        print("Is abc.Iterator!")
    while True:
        try:
            str = next(iterator)
            print(str)
        except StopIteration as e:
            print(f"iterator is empty , {e}")
            break

    print("func end")

def main():
    use_iterator()

if __name__ == '__main__':
    main()