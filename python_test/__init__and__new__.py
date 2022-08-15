"""
    python的类构造函数和实例化过程
        创建一个类的对象, 称为对象构造或者实例化. 负责运行实例化的工具称之为类构造函数
        实例化步骤:
            1. 创建一个新的类实例 __new__()
            2. 初始化这个类实例 __init__()
        * __init__ : 对象的初始化, 是Python对象实例化的第二步, 接受的第一个参数self(包含调用__new__产生的新实例), 其余参数用于对象属性的初始化. 无需返回值
        * __new__: 创建一个新的类实例, 一般不需要重写此方法, 只有在有特定需求自定义新实例时, 需要返回一个新的实例. 接受第一个参数为Cls
"""
import logging
from threading import Lock

logger = logging.getLogger("TEST")
handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

class Simple:

    def __new__(cls, *args, **kwargs):
        logger.debug("1.Create a new instance")
        return super().__new__(cls)

    def __init__(self, aMode, aType):
        logger.debug("2. initial the instance")
        self.myMode = aMode
        self.myType = aType
    
    def __str__(self):
        return f'{type(self).__name__} (Mode={self.myMode}, Type={self.myType})'

class Special:

    def __init__(self, aSpecialName, aSpecialHeight):
        self.myName = aSpecialName
        self.myHeight = aSpecialHeight

class Normal:

    def __new__(cls, *args, **kwargs):
        return Special('bobby', '30')

    def __init__(self, aMode, aType):
        logger.debug("2. initial the instance")
        self.myMode = aMode
        self.myType = aType

class Singleton(object):
    """
        使用__new__() 实现单例模式, 解决多线程问题, 每次请求都需锁资源.还可优化
    """
    _instance = None
    lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            cls._instance = super().__new__(cls) if not cls._instance else cls._instance
            return cls._instance


if __name__ == '__main__':
    simpleInstance = Simple("init", 'Cls')
    print(simpleInstance)

    """
        当Normal.__new__()返回不同类的实例时, Python不会运行Normal.__init__()

    """
    normal = Normal()
    print(isinstance(normal, Normal))
    print(isinstance(normal, Special))
