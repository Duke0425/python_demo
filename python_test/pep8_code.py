"""
    PEP8 代码布局
    1.每个缩进级别使用4个空格
"""
from calendar import c
import collections


def long_function(
        var_one, var_two,
        var_three, var_four):
    pass

foo = long_function(var_one, var_two,
                    var_four, var_five)

foo = long_function(
    var_one, var_two,
    var_four, var_five)

# if语句多行格式, 以下是比较推荐的
if (foo and
    foo):
    # 通过注释,语法高亮区分
    pass

# 最后一行增加额外的缩进
if (foo and
        foo):
    pass

my_list = [
    1, 2, 3,
    4, 5, 6
]

foo = long_function(
    var_one, var_two,
    var_four, var_four
)
"""
    代码布局总结: 
    空格是缩进的首选, 制表符已经在Python3中弃用.
    行的最大长度 - 79字符
    字符串和注释 - 72字符
    折叠长行首选为大括号, 中括号和小括号内隐式换行, 连续行使用反斜杠
"""

# 二元运算符换行 : 在二元运算符之前换行

income = (a
          + b
          + (c - w)
          + d)

"""
    空行
    顶级函数和类的定义之间有两行空行
    类内部的函数定义之间有一行空行

"""

"""
    导入
    导入顺序:
        1. 标准库导入
        2. 相关的第三方导入
        3. 特定的本地应用/库导入
    每个导入组之间放一行空行
"""
import os
import sys

"""
    模块级别的内置属性
    例如像__all__,__author__ , 应该放在模块的文档字符串后.
    Python强制要求from __future__导入必须在任何代码之前, 只能在文档字符串之后
"""

"""
    字符串引号, 单引号和双引号都可以, 但是当一个字符包含单引号或者双引号字符时, 使用另一种引号避免使用反斜杠
"""

foo_string = "123'sd22"

"""
表达式和语句中空格
"""
# 1.紧挨着大括号,中括号和小括号
func(num[1:2], {'a': 1})

# 2.为了与另外的赋值（或其它）操作符对齐，不止一个空格。
a = 1
b = 2
a_long_define = 3

# 3.始终避免行尾空白

# 4.二元运算符的两边放置空格 (*-=/)(== <= >= != < >) (in , not in) (and, or, not)
i = a + 1
a not in b
a != b

special = (a+b) * (a-b) #如果使用了不同优先级的操作符, 低优先级的二元运算符周围增加空格
special_two = a*b - 1

# 5.当=使用指示关键字参数和默认参数时, 周围不要使用空格
def complex2(real, a=1):
    return foo(a=real, b)

# 6.带注解的函数 等号两边需要加上空格
def complex3(a: int, c = 3) -> int:
    pass

"""
    不鼓励使用多行语句
"""
if foo is True:
    pass
else:
    pass

"""使用尾部逗号
        列表每个元素独占一行时, 尾部可以留有逗号: 当列表元素、参数、导入项未来可能不断增加
"""
a = [
    '阿萨德',
    '按少点',
    '把vv',
]
a = [1,2,3,5]  # 元素存在于一行时,不要使用尾部逗号

"""
    命名规范风格
        1. 包名和模块名 :模块名应该短，所有的字母小写。可以在模块名中使用下划线来提高可读性。Python包名也应该短，所有的字母小写，不鼓励使用下划线。
        2. 异常名: 使用后缀"ERROR"
        3. 全局变量名: 
        4. 函数名: 最好是小写字母, 必要时通过下划线分开单次增加可读性
        5. 如果类中的公开属性名和保留关键字发生冲突, 为属性名添加一个后置下划线
"""

"""
    二. 程序设计建议
"""

'a'.join('阿萨德') # 字符串的连接使用''.join 而不是+和-.
'aasd1'.startswith('aa')  # 代替字符串切片来检查前缀和后缀。

# functools.total_ordering()
"""
   1.  异常捕获
"""
# 捕获异常,尽可能提及到特定的异常,而不是使用空的except
try:
    value = a['key']
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)


