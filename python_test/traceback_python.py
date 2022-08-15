"""
    * Python traceback: 回溯
        当代码出现异常时, Python回溯提供了丰富的信息帮助程序员诊断和修复异常
    
    * traceback 内容(从下往上读):
        1. 错误类型(回溯的最后一行包含异常类型和有关该异常的一些相关信息)
        2. 文件名+ 行号 + 模块名称等信息: 
        3. 实际运行的代码:

    * Python常见的回溯
        1. AtrributeError : 特定的对象类型没有访问属性 // 从函数或者方法返回的对象是特定类型时, 也会触发此回溯, 
        2. ImportError: 导入语句时,出现问题引发此回溯
        3. ModuleNotFoundError: 当导入模块不存在, 或者从模块中不存在的模块导入某些内容时
        4. IndexError: 当从序列中检索索引,并且在序列中未找到该序列时引发
        5. KeyError: 访问不在映射(字典)中的键(字典中取不到键)
        6. NameError: 引用了在代码中未被定义的变量, 模块, 类, 函数, 或者其他名称
        7. SyntaxError: 代码中有不正确的python语法
        8. TypeError: 代码尝试对无法执行该操作的对象执行某些操作会引发
        9. ValueError: 当对象的值不正确引发, 可以视作由IndexError引发, 因为索引的值不在序列范围内
    * 如何记录回溯
"""

import logging

logger = logging.getLogger(__name__)

def main(aParam):
    try:
        print(aPara + 'cc')
    except NameError as e:
        logger.exception(e)
        print(-1, 'NameError')
        

if __name__ == '__main__':
    main('time')
    
