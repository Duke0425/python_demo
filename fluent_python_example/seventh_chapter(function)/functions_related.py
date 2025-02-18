"""
函数也是一等对象, 可以作为参数返回或者传递

接手函数作为参数或者把函数作为结果返回的函数叫做 高阶函数

python 3.8及以上 创建只能位置参数的函数时, 可以在参数列表中使用/

"""

from functools import reduce
from collections import namedtuple
from operator import methodcaller, mul, itemgetter, attrgetter

def test_function():
    """
    This is a function: use to return a
    """
    return "a"

def divmod(a, b, /):
    return (a//b, a&b)

def factorial(n):
    return reduce(mul ,range(1, n+1))

def useItemgetattr():
    a = [1,2,3,5,56]
    cc = {'a': 1, 'b':2} # error
    t = (0,1,1,2)
    one = itemgetter(1)
    print(one(a), one(t))

def useAttrgetter():
    useItemgetattr()
    person = namedtuple("Person", 'name gender age address')
    p1 = person("test", "man", 12, 'beijing')
    specialAttr = attrgetter('name', 'age')
    print(specialAttr(p1)) # ("test", 12)

def useMethodcaller():
    newSring = 'I know you'
    hyphenate = methodcaller('replace', ' ', '-')
   
    print(hyphenate(newSring))

def main():
    print(test_function.__doc__)
    print(factorial(10))

    useItemgetattr()
    useAttrgetter()
    useMethodcaller()


if __name__ == '__main__':
    main()
