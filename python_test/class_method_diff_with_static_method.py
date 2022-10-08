"""
一.类方法: 使用装饰器@classmethod, 第一个参数必须是未实例化的类本身
    1. 可以将一些解析的逻辑封装在方法本身内部 
    2. 子类继承之后依旧可以使用

二.静态方法: 使用装饰器@staticmethod, 可以不接收参数
    1. 不需要用到实例
    2. 也不需要用到未实例化的类本身

相同点: 
    1. 都可以在未实例化的类对象上调用
    2. 类方法包含cls参数, 可以轻松实例化类,而不管任何继承
    3. 静态方法主要目的是包含与类有关的逻辑, 但是该逻辑不应该对特定的类实例数据有任何要求
"""

class Student:
    """
    例子1: 类方法的使用
    """
    def __init__(self, aFirstName, aLastName):
        self.myFirstName = aFirstName
        self.myLastName = aLastName

    @classmethod
    def from_string(cls, aNameString):
        firstName, lastName = map(str, aNameString)
        student = cls(firstName, lastName)
        return student

    @classmethod
    def from_json(cls, aJsonFile):
        # parse json
        return

    @classmethod
    def from_pickle(cls, aPickleFile):
        # parse pickle
        return

class ClassGrades:
    """
    例子2: 类方法和静态方法的使用
    """
    def __init__(self, grades):
        self.grades = grades

    @classmethod
    def from_csv(cls, grade_csv_str):
        grades = map(int, grade_csv_str.split(', '))
        cls.validate(grades)
        return cls(grades)


    @staticmethod
    def validate(grades):
        for g in grades:
            if g < 0 or g > 100:
                raise Exception()

try:
    # Try out some valid grades
    class_grades_valid = ClassGrades.from_csv('90, 80, 85, 94, 70')
    print('Got grades:', class_grades_valid.grades)

    # Should fail with invalid grades
    class_grades_invalid = ClassGrades.from_csv('92, -15, 99, 101, 77, 65, 100')
    print(class_grades_invalid.grades)
except:
    print('Invalid!')