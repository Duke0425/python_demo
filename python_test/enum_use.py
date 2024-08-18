from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 78

    kitten = 1 # little cat
    puppy = 2 # little dog

def main():
    test_enum_class_get_value()
    test_enum_type()
    test_enumerate_func()

def test_enum_type():
    Animal = namedtuple('Animal', 'name age type')
    Perry = Animal(name="Perry", age=30, type=Species.cat)
    Dking = Animal(name="Dking", age=20, type=Species.horse)
    ff = Animal(name="ff", age=30, type=Species.cat)
    cc = Animal(name="cc", age=30, type=Species.kitten)
    print(f"Perry.type : {Perry.type} , Dking.type: {Dking.type} , cc.type: {cc.type}")
    if cc.type == ff.type:
        print(f"ff.type equal to cc.type")

def test_enum_class_get_value():
    print(f"Species(1) {Species(1)}")
    print(f"Species['cat'] {Species['cat']}")
    print(f"Species.cat {Species.cat}")

def test_enumerate_func():
    """
        enumerate 可通过start设置下标起始位置的值
    """
    list_a = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(list_a, start=2):
        print(c, value)

if __name__ == '__main__':
    main()
