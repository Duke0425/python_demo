"""
    Python一般容器的初始化
        1.dict
        2.list
        3.tuple
        4.set
"""
"""
    dict 初始化
"""
dictMethodOne = {'x': 1, 'y': 2}

dictMethodTwo = {}
dictMethodTwo['x'] = 1
dictMethodTwo['y'] = 2

dictMethodThree = dict(x=1, y=2)

dictMethodFour = dict(zip('xy', [1, 2]))

dictMethodFive = dict.fromkeys('xy' , [1, 2])

tupleElementList = [('x', 1), ('y', 2)]
dictMethodSix = dict(tupleElementList)

"""
    list 初始化
    tuple
    set
"""
listMethodOne = [1, 2]
tupleMethodOne = (1, )
setMethodOne = {1, 2}