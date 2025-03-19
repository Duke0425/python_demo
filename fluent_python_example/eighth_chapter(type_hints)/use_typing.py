"""
* 渐进式类型系统：
1. 默认情况下类型检查工具不应对没有类型提示的代码发出警告
2. 不再运行时捕获类型错误.
3. 不能改善性能

python 的静态类型检查, 注意Duck类型, 因为超类的类型检查, 需要在执行过程中才能发现问题.
- 如果需要避免这种情况, 请使用使用Mypy工具进行代码检查

python3.10为Optional, Union 提供的句法更好, 不用再从typing模块导入
- Union[str, bytes]直接写成   str | bytes
- Optional[str] 直接写成 str | None

! Union[float, int] 写成 Union[float] , 因为int和float相容, 仅适用float注解的参数也接受int值

! 按照PEP488的建议, 使用int ,float 或者complex中的某个类型
! PEP484的建议, 增加了typing.TypeVar构造函数, 把变量名称引入当前命名空间.

# 静态鸭子类型, 静态类型检查工具知晓鸭子类型的深意

* repl 函数: read eval print loop, 交互式解释器的基本行为

类型不完美, 测试需全面: 
- 静态类型很难发现以下问题:
1. 误报: 代码中正确的类型被检查工具报告有错误
2. 漏报: 代码中不正确的类型没有被检查工具报告有错误

建议把静态类型检查工具纳入到现代CI流水线, 与测试运行程序, lint程序等结合一起使用。CI流水线的目的是减少软件故障， 自动化
测试可以捕获许多超出类型提示范围的bug。Python写出的代码都能使用Python测试， 有没有类型提示无关紧要。
"""

from decimal import Decimal
from fractions import Fraction
from typing import Hashable, Optional, TypeVar, Iterator, AnyStr
from collections.abc import Hashable, Callable

NumberT = TypeVar('NumberT', float, Decimal, Fraction)
HashableT = TypeVar('HashableT', bound=Hashable) # 类型参数可以是Hashable或它的任何子类(因为Hashable是抽象类, 不能直接写入泛型中, 没有意义)
AnyStr = TypeVar('AnyStr', bytes, str) # 此类型变量为typing模块预定义的

def example_fuc(aVar: Iterator[NumberT]) -> NumberT | None:
    return aVar[0]


# python3.9及以上的版本, 支持直接在泛型中使用标准库的类
def tokenize(aText: str) -> list[str]:
    return aText.upper().split()
"""
# python 3.7及以上的版本
from __future__ import annotations

def tokenize(text: str) -> list[str]:
    return text.upper().split()

from typing import List

# python 3.5及以上的版本
def tokenize(text: str) -> List[str]:
    return text.upper().split()
"""


def use_callabel_para(aFunc: Callable[[str], list[str]]) -> Callable[[Iterator], NumberT | None]:
    return tokenize

"""
注解位置参数和变长参数
**foo: float , 指代dict[str, float]
"""
def tag(aVar: str, /, *content: str,  class_: Optional[str], **foo: float) -> None:
    return None


def main() -> None:
    aFunc = use_callabel_para(example_fuc)
    return


if __name__ == '__main__':
    main()