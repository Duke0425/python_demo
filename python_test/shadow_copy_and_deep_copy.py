from copy import deepcopy, copy

variableVar = [1, [1, 2, 3], {1, 2}]
immutableVar = {'stri', 1}

variableVarCopy = copy(variableVar)
variableVarDeepCopy = deepcopy(variableVar)

variableVar[0] = 2
variableVar[1][0] = 2

immutableVarCopy = copy(immutableVar)
immutableVarDeepCopy = deepcopy(immutableVar)

"""
赋值 = : 直接是将之前变量的引用赋予新的变量, 这两者保持一致

copy: 浅拷贝操作
deepcopy: 深拷贝操作

相同点: 对于不嵌套的参数拷贝, 结果是一样的. 
不同点: 对于嵌套的参数, 浅拷贝只是拷贝的嵌套中引用, 而深拷贝则会一直递归到最深处,拷贝整个副本

"""
