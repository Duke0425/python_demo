# 2.9 list.sort与内置函数 sorted
"""
list.sort 方法返回None, 此方法更改的原列表, 而没有创建新列表对象; 此种修改原对象, 返回None的方法不适合级联调用, 适合流式调用
sorted() 方法创建了新的排序列表, 而不影响原列表
! Python 主要使用的排序方法 Tim Sort , Time peter创建
"""
fruit = ["grape", 'raspberry', 'apple', 'banana']
print(sorted(fruit))
print(sorted(fruit, key=len))
print(sorted(fruit, key=len, reverse=True))
print(fruit)

fruit.sort(key=len, reverse=True)
print(fruit)

# 2.10 当列表不适用时
"""
TODO 如果经常需要在列表的两端添加和删除项, 使用deque(双端队列)更合适, 这是一种更加高效的FIFO数据结构
TODO 如果经常需要检查容器是否存在某一项(item in my_collection), 应考虑使用set类型存储my_collection, 尤其是项数比较多的情况. Python对Set成员检查做了优化,速度更快,set也是可迭代对象, 但不是序列,因为Set中的项是无序的
"""
from collections import deque
set()

# 2.10.1 数组
"""
如果一个列表只包含数值, 那么使用array.array会更加高效, 数值支持所有可变序列的操作, 此外还有快速加载项和保存项的方法, 例如.frombytes 和 .tofile
"""
from array import array
from random import random

# floats = array('d', (random() for _ in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp) # 保存双精度比正常文本保存快7倍
# fp.close()

# floats2 = array('d')
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10**7) # 读取1000万双精度, 时间预估0.1秒, 比文本读取快了60倍
# fp.close()
# print(floats2[-1])
# print(f"{floats == floats2=}")

# 2.10.2 memoryview

