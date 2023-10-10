import logging
"""
Python中的内置函数
    1. abs(x) :返回整型、浮点数的绝对值， 以及实现了__abs__() 方法的任何对象. 如果是复数, 则返回其模
    2. aiter(async_iterable): 3.10新增, 返回异步迭代对象
    3. all(iterable): 可迭代对象中所有元素均为真值(或者可迭代对象为空).
    4. any(iterable): 可迭代对象中任一元素为真值返回True
    5. ascii(object): 返回一个字符串. 对于非ASCII编码 返回"\x, \u 和\U" 进行转义
    6. bin(x): 将整数转化为"0b"开头的二进制字符串. 包含__index__()方法的对象也可以使用该方法
    7. bool(): 真值转换
    8. callable(object): 如果对象包含__call__()方法返回True, 否则返回False
    9. chr(i): 返回Unicode码为整数i的字符串形式
    10. compile(source, filename, mode): 将字符串编译成字节代码
    11. complex(): 返回复数
    12 delattr(obj, attr_name): 删除对象属性
    13.
"""

class FooTest:

    def __init__(self) -> None:
        self.myName = ''
        self.myHeight = 1

def main():
    abs(-12.122)  # 12.122
    
    all([1, False])  # False

    any({'a': None, 'x': 1})  # True

    ascii("非ASCII编码")  # "'\\u975eASCII\\u7f16\\u7801'"

    bin(12)  # '0b1100'
    format(12, '#b')  # '0b1100'
    format(12, 'b')  # '1100', 使用format去除0b头部

    bool(0)  # False
    bool([])  # False

    chr(12)  # '\x0c'

    complex("1+2j")  # 1+2j

if __name__ == '__main__':
    
    main()