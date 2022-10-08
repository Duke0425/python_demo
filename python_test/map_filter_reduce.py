from functools import reduce

def use_map():
    """
    map 映射函数, 将匿名函数包含在内, 从一列表创建新列表. Python3之后是一个可迭代对象
    """
    a_list = list(range(1,10,1))
    new_a_object = map(lambda x:x+123, a_list)
    print(list(new_a_object))

def use_filter():
    """
    filter 筛选函数, 参数和map函数相同, 接受function变量和一个可迭代的对象
    """
    a_list = list(range(1,10,1))
    new_a_object = filter(lambda x:x>3, a_list)
    print(list(new_a_object))

def use_reduce():
    """
    裁剪函数, 接受function函数变量，一个可迭代对象和初始值, 会将前一个计算值与后一个值进行运算, 最后得出一个值. 
    """
    c_list = [1, 2, 3, 5]
    print(reduce(lambda x, y: x + y, c_list))
    print(reduce(lambda x, y: x + y, c_list, 200))


def main():
    use_map()
    use_filter()
    use_reduce()

if __name__ == '__main__':
    main()