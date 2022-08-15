"""
argparse: 简单的命令行参数解析器
    1. 对用户友好的命令行. 参数来自sys.argv
    2. 该模块还自动生成帮助和使用消息, 用户给程序无效参数时, 发出错误
    3. 此模块为python标准模块

"""
import sys
from argparse import ArgumentParser

class SimpleArgsParser:
    def __init__(self):
        self.myParser = ArgumentParser()

    def set_argparse(self):

        """
        位置参数
        """
        self.myParser.add_argument("name")
        self.myParser.add_argument("age")


        self.myParser.add_argument(
            '-o',
            '--output',
            # action = 'store_true',
            help = 'show output',
            dest = 'oo', # 参数别名, args.oo可以调用参数
            required = True, # 设置为True时,必须传入该参数, 否则会失败
            type = int, #设置输入的参数类型
            action = "append",  # 允许重复设置值
            nargs = "*", # * nargs 需要 0 个或多个参数,
            choices = [123, 456]  # 给定参数的限制列表, 只能是其中一个
        )

        self.myParser.add_argument(
            '-c',
            '--congra',
            action = 'store_true',
            help = 'show congra'
        )

        self.myParser.add_argument(
            '-s',
            '--simplemode',
            action = 'store_true',
            help = 'show congra'
        )



if __name__ == '__main__':
    print("You passed the following arguments: ")
    print(sys.argv)

    simpleArgsParser = SimpleArgsParser()
    simpleArgsParser.set_argparse()

    args = simpleArgsParser.myParser.parse_args()

    print(f"args parameters {args.__dict__}")
    
    