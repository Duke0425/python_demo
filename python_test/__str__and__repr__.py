import random
"""
__str__ :将任何对象传递给str()函数时, __str__方法将会被调用
__repr__:将任何对象传递给repr函数时, __repr__方法将会被调用

默认定义的类中, 两个魔法方法的输出是一样的.
但是两种方法的工作方式完全不同, 

如果不定义__str__方法, 那么str()函数将会返回__repr__()方法的定义
* 实际开发中, 应该尽量避免重写__repr__方法

__repr__() 方法主要供开发人员在调试时使用。另一方面，__str__() 方法用于获取用户可以理解的对象的文本表示。
当我们在交互式 python 控制台中键入变量的名称或对象时，调用 __repr__() 方法以产生输出。另一方面，当我们将变量传递给 print() 函数或 str() 函数时，会调用 __str__() 方法。
如果类定义不包含 __str__() 方法，则当我们将对象传递给 str() 函数时，python 解释器会调用 __repr__() 方法。
当我们将容器对象传递给 print() 函数时，无论我们是否在类定义中实现了 __str__() 方法，都会打印容器对象元素的 __repr__() 方法元素。
"""

class Dog:
    def __init__(self, aName, aGender):
        self.myName = aName
        self.myGender = aGender
        self.myYear = None

    def GetStringOfDogYear(self):
        randomNumber = random.randint(0,1)
        if randomNumber:
            return str(self.myYear)
        else:
            return repr(self.myYear)

    def __str__(self):
        return f'this is a {self.myYear} years-old and {self.myGender} dog, named {self.myName}'


def implying():
    myStr = 'duke'
    myStr1 = myStr.__repr__()
    myStr2 = myStr.__str__()

    print("The string is:", myStr)
    print("The output from the __repr__() method is:", myStr1)
    print("The output from the __str__() method is:", myStr2)
    output1 = eval(myStr1)
    print(output1)
    output2 = eval(myStr2)
    print(output2)


if __name__ == '__main__':
    dog = Dog('bobby', 'male')
    dog.myYear = 12
    
    dog.GetStringOfDogYear()
    implying()
    
    
