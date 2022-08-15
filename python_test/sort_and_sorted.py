from collections import Iterable, namedtuple
"""
.sort()将不会撤销地覆盖数据, 需保存原始数据使用sorted()
sorted接受迭代对象, sort只能用于list
"""

def use_sorted(aIter, aKey=None):
    """
    1. sorted 不会改变原先变量的值
    2. sorted是一个内置函数, 可以直接调用, 返回值是一个新的列表
    3. sorted接受一个有序序列的参数, 和reverse参数(默认为升序排序, reverse=True降序排列), key参数
    sorted(iterable, reverse=True, key=?)
    key参数 期望接受一个参数, 并且该参数金将会被用与列表中的每个值, 比如(len函数, 通过序列长度来排序)
    mention: key参数 的函数一次接受列表的一个值, 且此函数能够处理迭代中的所有值

    ** 可接受元组和集合, 可以将之前的序列进行排序, 返回一个新的列表
    ** sorted方法不可以排序 两个不能比较的值类型: 比如None 和1, 1和'12'. 这些将会报错

    4.字符串排序为第一个字母的unicode数进行排序
    """
    if not isinstance(aIter, Iterable):
        return
    
    return sorted(aIter, reverse=True, key=aKey)

def use_sort(aList):
    """
    .sort()是list类的一个内置的方法, 只能与列表一起使用. 返回值为None

    1. .sort()返回值为None, 更改了原生列表
    2. 参数key->期望函数 , reverse参数: True或者False(降序和升序)
    """
    if not isinstance(aList, list):
        return
    aList.sort()

def unicode_second_letter(aString):
    """
    获取字符串的第二个字符的unicode
    """ 
    if isinstance(aString, str):
        return ord(aString[1])


if __name__ == '__main__':
    listOne = [i for i in range(10)]
    use_sorted(listOne)
    listTwo = ['harry', 'Suzy', 'al', 'Mark']
    newStringList = use_sorted(listTwo, unicode_second_letter)

    nStringList = sorted(listTwo, reverse=False, key=lambda x:x[::-1])
    [(i, ord(i[-1]))for i in nStringList] #查看排序后的unicode编码

    valueToSort = [1, 9, 2, 0, 3]
    use_sort(valueToSort)
