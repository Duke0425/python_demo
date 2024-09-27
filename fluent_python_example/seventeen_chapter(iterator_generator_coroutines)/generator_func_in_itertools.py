"""
1. 用于筛选的基础生成器函数
"""
from threading import stack_size


class FilterGeneratorClass:

    _fruit_list = ['pear', 'apple',  'strawberry', 'watermelon', 'orange']

    @classmethod
    def test_func(cls):
        cls.use_itertools_compress()
        cls.use_itertools_dropwhile()
        cls.use_itertools_filterfalse()
        cls.use_itertools_islice()
        cls.use_itertools_takewhile()

    @classmethod
    def use_itertools_compress(cls):
        """
        此迭代器根据作为其他参数传递的布尔列表值，从传递的容器中选择性地挑选要打印的值。将打印与布尔值 true 对应的参数，否则将跳过所有参数. 选择器的长度不影响.
        """
        from itertools import compress
        selectors = [False, False, True, False, False, False, True] # 0,1 也可以作为值
        print(list(compress(cls._fruit_list, selectors)))

    @classmethod
    def use_itertools_dropwhile(cls):
        """
        此迭代器, 接受一个函数对象及一个序列, 跳过函数返回为真值的值, 直到false后, 返回剩下的值
        """
        from itertools import dropwhile
        print(list(dropwhile(lambda x: len(x) < 5, cls._fruit_list)))

    @classmethod
    def use_itertools_filterfalse(cls):
        """
        此迭代器仅打印传递函数返回false的值
        第一个参数接受函数或者None, 第二参数接受序列
        """
        from itertools import filterfalse
        print(list(filterfalse(lambda x: len(x) > 5, cls._fruit_list)))

    @classmethod
    def use_itertools_islice(cls):
        """
        此迭代器有选择性地打印作为参数传递的可迭代下容器中提到的值
        参数类型: 可迭代序列,停止
        islice(sequences, stop) == sequences[:stop]
        参数类型: 可迭代序列, 开始, 停止, 步骤
        islice(sequences, start, stop, step) == sequences[start:stop:step]
        """
        from itertools import islice
        for i in islice(range(20), 5):
            print(i)
        print(list(islice(cls._fruit_list, 1, 4, 2)))

    @classmethod
    def use_itertools_takewhile(cls):
        """
        takewhile(predicate, iterable)
        此迭代器返回当predicate为真值时对应的项, 不是真值立即停止, 不再继续检查
        """
        from itertools import takewhile
        print(list(takewhile(lambda x: len(x) <= 5, cls._fruit_list)))


"""
2. 用户映射的生成器函数
"""
# from itertools import accumulate, starmap
# enumerate
# map
class MappingGeneratorClass:

    _sample = [5, 4, 2, 1]
    _nums = [1, 2, 3, 5, 7]

    @classmethod
    def test_func(cls):
        # cls.use_itertools_accumulate()
        # cls.use_itertools_starmap()
        cls.use_map()

    @classmethod
    def use_itertools_accumulate(cls):
        """
        此迭代器产出累计求和, 如果提供了func, 那么将前两个项传给他, 然后吧计算结果和下一项传给他, 以此类推, 产生最后结果
        accumulate(it, [func])
        """

        from itertools import accumulate
        import operator
        print(list(accumulate(cls._sample)))
        print(list(accumulate(cls._sample, operator.mul)))

    @classmethod
    def use_itertools_starmap(cls):
        """
        starmap(func, it): 第一个参数为函数, 第二个参数为可迭代对象
        """
        list_one = [(1,2), (2,3)]
        from itertools import starmap
        print(list(starmap(pow, list_one)))

        # 勾股定理的使用
        co_ordinates =[(2, 3, 4), 
                    (3, 4, 5),
                    (6, 8, 10),
                    (1, 5, 7),
                    (7, 4, 10)]
        
        
        # Set true if coordinates form
        # a right-triangle else false
        right_triangles = list(starmap(lambda x, y, z:True
                                    if ((x * x)+(y * y))==(z * z)
                                    else False, co_ordinates))


    @classmethod
    def use_map(cls):
        """
        map(func, iter): 接受函数和可迭代对象啊. 可以传输多个可迭代对象给map函数
        给定函数应用于给定可迭代对象后, 返回结果生成器    
        """
        print(list(map(lambda x, y: x*y, cls._sample, cls._nums)))
        print(list(map(pow, [(1,2), (2,3)]))) # ! Error, 需要两个参数却只获取到一个

"""
3. 合并多个可迭代对象的生成器函数
"""
# from itertools import chain, product, zip_longest
# chain.from_iterable
# zip

class CombinationGeneratorClass:

    @classmethod
    def test_func(cls):
        # cls.use_itertools_chain()
        # cls.use_chain_from_iterable()
        # cls.use_itertools_product()
        # cls.use_itertools_zip_longest()
        cls.use_zip()

    @staticmethod
    def use_itertools_chain():
        """
        chains(*its)
        此函数接受一系列迭代器对象
        将所有可迭代对象组合在一起并生成单个可迭代对象作为输入.
        """

        from itertools import chain
        list_a, str_b = [1, 23, 1, 5] , "1234"
        print(list(chain(list_a, str_b)))

    @staticmethod
    def use_chain_from_iterable():
        """
        from_iterable(it)
        此函数接受单个可迭代对象, 可迭代对象中的每个元素也应该是可迭代对象. 
        返回包含输入可迭代对象所有元素的扁平化可迭代对象
        """
        from itertools import chain
        print(list(chain.from_iterable(["AD", [1,"123",4]])))

    @staticmethod
    def use_itertools_product():
        """
        itertools.product(*it, repeat=1)
        返回给定迭代器与自身的笛卡尔积, 重复次数可由可选关键字"repeat"指定
        """
        from itertools import product
        print(list(product([1,2,3], repeat = 3)))

    @staticmethod
    def use_itertools_zip_longest():
        """
        zip_longest(it, it, fillval)
        此函数接受多个可迭代对象, 和一关键字参数
        顺序打印可迭代对象中的元素, 如果迭代器用尽, 将会使用fillval来代替, 如果没设置, 则默认是None
        """
        from itertools import zip_longest
        print(list(zip_longest("ASDFG", [1,2,3,5,6,7,8,0], fillvalue = 'nothing')))

    @staticmethod
    def use_zip():
        """
        zip(*it)
        此函数为内置函数, 可接受多个可迭代对象参数
        返回单个迭代器对象, 如果其中一迭代对象已用尽, 那么停止组装迭代
        """
        persons = ["Chandler", "Monica", "Ross", "Rachel", "Joey", "Phoebe", "Joanna"]
        genders = ["Male", "Female", "Male", "Female", "Male", "Female", "Female"]
        ages = (35, 36, 38, 34)
        # print(list(zip(persons, genders, ages)))
        for person, gender, age in zip(persons, genders, ages):
            print(person, gender, age)

"""
4. 把输入的各项扩充成多个输出项的生成器函数
# from itertools import combinations, combinations_with_replacement
# from itertools import cycle, pairwise, permutations, repeat

"""

"""
5. 用于重新排列元素的生成器函数
from itertools import groupby, tee
reversed
"""


def main():
    # FilterGeneratorClass.test_func()
    # MappingGeneratorClass.test_func()
    CombinationGeneratorClass.test_func()

if __name__ == '__main__':
    main()
