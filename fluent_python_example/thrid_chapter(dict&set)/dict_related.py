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

# 3.5 自动处理确实键的另一种选择
def use_defaultdict():
    index = collections.defaultdict(list)
    index['word'].append(0)
    print(index)

if __name__ == '__main__':
    # dial_dict = dict_derived_formula()
    # print(dumps(**{'x': 1}, y=2, **{'z': 3}))
    # use_merge_map()
    hash_map()
    use_defaultdict()
