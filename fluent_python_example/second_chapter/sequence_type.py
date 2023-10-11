import pdb

from collections import abc

issubclass(tuple, abc.Sequence)
issubclass(list, abc.MutableSequence)

# 1. 内置的序列类型其实不是 abc.Sequence和 abc.MutableSequence的子类, 而是一种虚拟子类

# 2. listcomps 列表推导式 list comprehension 

string = 'adb'
codes = [string for string in string]
codes = [last:= s for s in string] # 海象运算符: 赋值的变量在列表推导式或者生成器表达式返回后可以访问
# 3. genexps 生成器表达式 generator expression: 使用表达式可以描述可节省内存值
tuple(s for s in string) 

# 4.元组: 不仅仅是不可变列表, 还可用作没有字段名称的记录/ 相同长度的元组, 相较于列表,占用的内存更小
"""
性能优势: 
1. 求解元组字面量,只需一次操作. 求解列表字面量时, 生成的字节码将每个元素作为独立的常量推入数据栈, 然后构建列表
2. 给定一个元组, 长度是固定的, 内存空间刚好够用. 列表内存空间会比给定大一些, 随时准备追加元素
3. 创建列表list(l)时 会创建l的副本, tuple(t) 直接返回t的引用
"""

tm = (1, 'afb', [1, 12])
try:
    hash(tm) # 判断元组的值是否固定 可用hash函数定义
except TypeError:
    pass


# 5.序列和可迭代对象拆包
"""
方式1: 并行赋值
方式2: * 拆包
"""
a, b, c = tm
d = *range(5), 6

metro_areas = [
    ('Tokyo', 'JP', 36.6, (35,33)),
    ('Beijing', 'CN', 36.6, (35,33)),
    ('New York', 'US', - 36.6, (35,-33.33)),
    ('Chengdu', 'CN', 36.6, (35,33)),
]

# 嵌套拆包
for name, _, _, (las, lon) in metro_areas:
    if lon <= 0:
        print(name)


# 序列模式匹配
"""
math case 语法拆包 3.10引入 ,从表象来看 match/case 与 C语言中switch/case语句很像, 与Switch相比, match的一大改进是支持析构,
这是一种高级拆包形式
标准库中以下类型与序列模式兼容:
    list tuple memoryview array.array range collections.deque
"""

for metro_area in metro_areas:
    match metro_area:
        case [str(name), _, _, (int(las), float(lon)) as coord] if lon <= 0:
            print(f"use match/case return {name=!r} {coord=}")

# 切片
list_example = [1,2,3,4,5,6]
print(list_example[::-3])
print(list_example[:3])

# 多维切片和省略号
"""
numpy创建的2纬数组, 可以通过多维切片的方式 例二维数组aa, aa[i:j, k:l]
省略号 (...) python解释器把它识别为一个记号, 省略号是ellipsis对象的别名
"""
type(...)

 # 为切片赋值
l = list(range(10))
l[3:5] = [20, 30]
del l[8:9]
l[3::2] = [11, 22, 33]
l[:3] = [100]

sr = 'IM GOD'

# 使用 + 和 * 号处理序列
lista = [1, 23]
listb = [4, 56]
listc = lista + listb
listd = lista * 3

# 如果a * n 创建多重列表, 如果a中包含可变项, 嵌套的引用会指向同一个列表, 如果进行赋值, 那么这三个
# 嵌套列表将会是相同的, 因为它们引用相同 是同一个对象

# 2.8.1 创建嵌套列表
