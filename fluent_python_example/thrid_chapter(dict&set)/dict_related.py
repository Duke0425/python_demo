import collections

# 3.2.1 字典推导式
def dict_derived_formula():
    
    dial_codes = [
        (880, 'bangladesh'),
        (55, 'Brazil'),
        (86, 'China'),
    ]
    dial_dict = {country: code for code, country in dial_codes}
    print(f'{dial_dict}')
    return dial_dict

# 3.2.2 映射拆包
def dumps(**kwargs):
    """
        调用参数字典所有键必须为字符串才行
    """
    # 此种**映射解包方法也可以在字典字面量中使用, 键可以重复, 但是后面的键覆盖前面的键
    print({'a': 0, **{'x':1}, 'c': 2, **{'x': 4}})

    return kwargs

# 3.2.3 使用| 合并映射
"""
Python 3.9 支持使用| 和|= 合并映射。 这并不难理解， 因为二者也是并集运算符
"""
def use_merge_map():
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 2, 'b': 4, 'c': 6}
    print(f'{d1 | d2=}')

    d1 |= d2
    print(d1, d2)

# 3.3 使用模式匹配处理映射
"""
match case
"""

# 3.4 映射类型的标准API

isinstance(dict, collections.abc.Mapping)
isinstance(dict, collections.abc.MutableMapping)

# 3.4.1 可哈希, 如果一个对象的哈希码(__hash__())在整个生命周期内永不改变, 而且可与其他对象比较(__eq__()方法), 那么这个对象就是可哈希的
def hash_map():
    tt = (1, 2, 3)
    tl = (1, 2, [3, 4])
    tf = (1, 2, frozenset([3, 5]))

    hash(tt)
    try:
        hash(tl)
    except TypeError as error:
        print(f'{error=}')
    hash(tf)

# 3.5 自动处理缺失键的另一种选择
def use_defaultdict():
    index = collections.defaultdict(list)
    index['word'].append(0)
    print(index)

# 3.5.2 dict处理映射缺失键在__missing__中, dict基类未定义, 但是如果定义, 通过__getitem__取值时, 不会抛出KeyError
class CusDict(dict):
    """
    在查找键时, 将非字符串值键转换为字符串
    """
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key) -> bool:
        return key in self.keys()or str(key) not in self.keys()

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
"""
不同的标准基类对于__missing__方法调用不同, 这个需要注意
dict子类: 如果增加__missing__方法, 那么只有d[k]操作会调用此方法
collection.UserDict子类 :如果增加__missing__方法, 继承UserDict的类只有d.get()会调用此方法
abc.Mapping子类: 以最简单的方式实现__getitem__方法, 此类将永不会调用__missing__
abc.Mapping子类: 让__getitem__调用 __missing__方法, d[k] d.get(k) k in d 遇到缺失的键时, 都将会调用__missing__方法
"""
# 3.6 dict的变体
# 3.6.1 OrderedDict (python3.6之后, 内置的dict也保留键的顺序) 
"""
1. OrderedDict 等值检查考虑顺序
2. OrderedDict 的popitem()方法签名不同, 可通过一个可选参数指定移除哪一项
3. OrderedDict 多了一个move_to_end()方法, 可将元素的位置移到某一端
4. 常规Dict主要用于执行映射操作, 插入顺序都是次要的
5. OrderedDict的目的主要是方便执行重新排序操作, 空间利用率、迭代速度和更新操作的性能是次要的
6. 从算法上来看， OrderedDict处理频繁重新排序操作的效果比dict好, 因此适合用于跟踪近期的存取情况(LRU缓存中)
"""
# 3.6.2 collections.ChainMap
"""
ChainMap储存一组映射, 查找输入映射在构造函数调用的先后顺序进行查找, 查找到后, 直接结束.
更新操作也如此, 只更新到含有输入映射的第一个字典
ChainMap可用于实现支持嵌套作用域的语言解释器
"""
def use_chain_map():
    d1 = dict(a=1, b=2)
    d2 = dict(a=4, b=9, c=3)
    from collections import ChainMap
    chainMap = ChainMap(d1, d2)
    print(chainMap['a'], chainMap['c'])

# 3.6.3 collections.Counter
"""
这是一种对于键进行计数的映射.
!Notice: most_common(3), 如果出现次数相同的键排在前三, 此方法也只会显示3个
"""
def use_counter():
    from collections import Counter
    ct = Counter("adjfhasdfgasgdfradf")
    print(ct)
    print(ct.most_common(3))

# 3.6.4 shelve.Shelf
"""
标准库中的shelve模块持久存储字符串键与Python对象之间的映射.
模块级函数shelve.open 返回一个shelve.Shelf实例,这是一个简单的键值DBM数据库, 背后是dbm模块, shelve.Shelf具有以下特征
- shelve.Shelf 是abc.MutableMapping的子类, 提供了我们预期的映射类型基本方法
- 此外shelve.Shelf还提供了一些其他I/O 管理方法, 例如sync和close.py
- Shelf实例时上下文管理器, 因此可以使用with块确保使用后关闭
- 为键分配新值后即保存键和值
- 键必须是字符串
- 值必须是pickle模块可以序列化的对象
"""
# 3.6.5 子类应集成UserDict而不是dict

from collections import UserDict
class CusDict(UserDict):
    """
    在查找键时, 将非字符串值键转换为字符串
    """
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key) -> bool:
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# 3.7 不可变映射
"""
标准库中中的映射都是可变的, 不过有时也要防止用户意外更改映射.
types模块提供的MappingProxyType是一个包装类,把传入的映射包装成一个mappingproxy实例,
这是原映射的动态代理,只可读取. 
"""
def use_not_modify_mapping_type():
    from types import MappingProxyType
    d1 = {'A': 1}
    mappingProxyType = MappingProxyType(d1)
    print(mappingProxyType['A'])
    try:
        mappingProxyType['A'] = 3
    except Exception as e:
        print(e)

# 3.8 字典视图
"""
.values()  
.items()
.keys()
都是字典的只读视图, values()最为简单, 只实现了__len__. __iter__, __reversed__这三个特殊方法
dict_keys dict_items 还实现了多个集合方法
"""

# 3.9 dict实现方式对于实践的影响
"""
1.键必须是可哈希的对象,
2. 通过键来访问值非常快, 因为Python 通过计算所得哈希码就可以直接定位键
3. Cpython3.6中, dict的内存布局更加紧凑,顺带的一个副作用就是键的顺序得以保留,
4. 尽管采用了更加紧凑的布局, 但是dict仍然占用大量内存, 这是不可避免的,
5. 为了节省内存,不要在__init__之外创建实例属性.

类的实例可以共用一个哈希表, 随类仪器存储, 如果新实例与__init__返回的第一个实例拥有相同的属性名称, 那么新实例的__dict__属性就共享
这个哈希表,仅以指针数组的形式存储新实例的属性值. __init__方法执行完毕后再添加实例属性, Python就会为这个实例创建一个新的__dict__哈希表
PEP412: 这种优化可将面向对象程序内存使用量减少10~20%
"""

# 3.10 集合论

if __name__ == '__main__':
    # dial_dict = dict_derived_formula()
    # print(dumps(**{'x': 1}, y=2, **{'z': 3}))
    # use_merge_map()
    # hash_map()
    # use_defaultdict()
    # use_chain_map()
    # use_counter()
    use_not_modify_mapping_type()
