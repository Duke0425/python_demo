from collections import namedtuple
from typing import NamedTuple, get_type_hints
import inspect

"""
namedtuple 可以进行equal对比, 同样数据则相等
! NamedTuple 区别于namedtuple, 1. 是在可以为每个字段进行注解, 2. 并且可以使用解包的方式, 进行字段赋值. 3.可以集成创建class , 且创建的方式是元类创建 不是超类.
! 元类创建 issubclass(,tuple) is True, issubcalss(,typing.NamedTuple) is False
"""

def main():
    coordinateTupleOne = namedtuple('Coordinate', 'lat lom')
    coordinateTupleTwo = NamedTuple('Coordinate', [("lat", float), ('lon', float)])
    coordinateTupleThree = NamedTuple('Coordinate', lat=float, lon=float)
    moscowO = coordinateTupleOne(55.756, 37.317)
    moscowS = coordinateTupleTwo(55.756, 37.317)
    moscowT = coordinateTupleThree(55.756, 37.317)

    print(get_type_hints(moscowS))
    print(moscowO, moscowS, moscowT)
    print(inspect.get_annotations(coordinateTupleThree))

if __name__ == '__main__':
    main()
