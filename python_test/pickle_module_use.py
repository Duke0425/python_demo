"""
    1.Python中的序列化
        序列化(编组): 将复杂的对象结构转化为可以存储在磁盘或者通过网络发送的字节流
        反序列化(解组): 将字节流转换回数据结构的反向过程称为反序列化

        * Python提供了3个不同的模块来序列化和反序列化对象
            - marshal : 读写Python模块的编译字节码, 或者直接从.pyc解释器导入Python模块时得到的文件(可以序列化对象, 但是不建议使用)
            - json : 可操作标准Json文件(JSON是一种非常方便且广泛使用的数据交换格式)
            - pickle : 以二进制格式序列化对象,所以结果是不可读, 但是也可以使用更多的Python类型, 包括自定义对象

            ? 三种模块的使用场景
                1. 不要使用marshel模块, 他主要由解释器使用, 官方文档警告Python维护者可能会以向后不兼容的方式修改格式
                2. 如果需要不同语言或者可读格式的互操作性, Json和XML是不错的选择
                3. pickle是所有剩余用例的最好选择, 不需要可读性或者标准的可互操作格式, 或者需要自己序列化对象 

        * JSON 格式易于阅读且与语言无关, 比XML更加轻巧, 使用Json模块, 可以序列化和反序列化集中标准的Python类型
            - bool, string , dict, list, int, float, tuple, None
"""
import pickle
import json
import marshal
import dill

"""
    # 1. pickle模块的方法
        ? dump / dumps
            dump: 序列化对象, 创建一个包含序列化对象的文件
            dumps: 序列化对象, 返回一个字符串
        ? load / loads
            load: 读取文件中的对象, 并且反序列化
            loads: 将字符串反序列化
    # 2. pickle模块的协议版本
        协议版本 0是第一个版本。与后来的协议不同，它是人类可读的。
        协议版本 1是第一个二进制格式。
        协议版本 2是在 Python 2.3 中引入的。
        Python 3.0 中添加了协议版本 3 。它不能被 Python 2.x 解开。
        Python 3.4 中添加了协议版本 4 。它支持更广泛的对象大小和类型，并且是从Python 3.8开始的默认协议。
        Python 3.8 中添加了协议版本 5 。它支持带外数据并提高了带内数据的速度。

        * 3.8之后默认协议版本为4, 支持更加广泛的对象大小和类型

    # 3. pickle的安全使用
        由于反序列化的时候, __setstate__()，该方法非常适合在 unpickling 时进行更多初始化，但它也可以用于在 unpickling 过程中执行任意代码！
        ! 永远不要解开来自不可信来源或者通过不安全网络传输的数据, 防止中间人的攻击, 最好使用诸如hmac对数据进行前面并确保其并未被篡改
"""

class Serializer:

    @staticmethod
    def pickle_serialze_to_string(aObject):
        return pickle.dumps(aObject)

    @staticmethod
    def pickle_serialze_to_file(aObject):
        pass

    @staticmethod
    def pickle_deserialze_from_string(aString):
        return pickle.loads(aString)

    @staticmethod
    def pickle_deserialze_from_file(aFile):
        pass


class PersonSimple:
    _name = "duke"
    _age = 18
    _body = ['eyes', 'legs', 'ears', 'knees']
    _lover = {'name': 'vivian', 'age': 18}
    _hobby = ('The Ghost of Tsushima', 'LOL')


class FooBar:
    def __int__(self):
        self.myAttriA = 1
        self.myAttriB = 'c'
        # self.myAttriC= lambda x : x ** x

    # def __getstate__(self):
    #     attributes = self.__dict__.copy()
    #     del attributes['myAttriC']
    #     return attributes

    def __setstate__(self, aState):
        self.__dict__ = aState
        self.myAtrriC = lambda x: x ** x

def do_serialize_test():
    person = PersonSimple()
    pickle_object = Serializer.pickle_serialze_to_string(person)
    print(f"序列化之后的二进制字符串: {pickle_object}")

    person._age = 25
    unpickled_object = Serializer.pickle_deserialze_from_string(pickle_object)

    """
        * picklable 和 unpicklabel 类型
            pickle可以序列化比json更多类型的Python数据, 但是也存在不能序列化的对象
            ! unpickale: 打开的套接字对象, lambda函数, 正在运行的线程, 数据库的连接 
            TODO: 如果需要序列化这些对象--> 1. 使用dill第三方模块
            TODO: dill 模块甚至可以序列化整个解释器会话
            * 
    """
    cube = lambda x: x * x * x
    dill_lambda = dill.dumps(cube)
    # pickle_lambda = Serializer.pickle_serialze_to_string(cube)
    print(f'序列化之后的lambda函数{dill_lambda}')

    # dill.dump_session('test.pkl')
    # exit()

    """
        序列化和反序列化对象的例子
        __getstate__ , 将unpiclable的属性给删除
        __setstate__ , 反序列化后将unpicklable的属性复原
    """
    exampleFooBar = FooBar()
    pickableString = pickle.dumps(exampleFooBar)
    newExampleFooBar = pickle.loads(pickableString)
    print(exampleFooBar.__dict__)
    print(newExampleFooBar.__dict__)
    """
        pickle 数据格式是对象结构的紧凑的二进制表示, 任然可以通过bzip2 gzip来进行压缩
    """
    aString = "拉萨或过多多多多多多多多多多多多多多多多多多多多多多多多多大绿所多军啦所军绿多扩军奥所多绿 \
    军啦所军多扩军按所氨基酸对抗拿贾斯丁比伯三大部分不舍得放几把卡仅代表把喇叭收到了吧点击可不能框架那家里看上你的接口把科技部"
    one = pickle.dumps(aString)
    import bz2
    oneCompress = bz2.compress(one)
    print(f"压缩之后的长度{len(oneCompress)}, 压缩之前的长度{len(one)}")

    

def do_deserialize_test():
    """
        使用dill反序列化会话
    """
    globals().items()
    dill.load_session("test.pkl")
    globals().items()

if __name__ == '__main__':
    do_serialize_test()
    # do_deserialize_test()
