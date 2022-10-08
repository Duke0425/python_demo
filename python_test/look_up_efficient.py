import time

"""
(set)集合 和 (dict)字典都是哈希表,查询时 能够通过哈希值快速找到指定的值, 时间复杂度为O(1)
而list不是, 时间复杂度为O(N), 如果查询列表不需要指定的索引, 使用集合会更快

"""

def time_decorator(aFunc):
    def wraps(*args, **kwargs):
        startTime = time.time()
        aFunc(*args, **kwargs)
        endTime = time.time()
        print(f"waste time {endTime - startTime}")
    return wraps

@time_decorator
def look_for_element(simpleList):
    return '100000' in simpleList

@time_decorator
def look_for_element_in_set(simpleSet):
    return '100000' in simpleSet

def main():
    simpleList = list(range(1,100000,1))
    simpleSet = set(simpleList)
    look_for_element(simpleList)
    look_for_element_in_set(simpleSet)

if __name__ == '__main__':
    main()
