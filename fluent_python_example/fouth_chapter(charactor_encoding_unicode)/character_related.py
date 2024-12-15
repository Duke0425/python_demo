from array import array
import locale
import sys
import unicodedata

"""
字符的最佳定义就是Unicode字符. 
  - Python3 str对象 就是Unicode字符, 
  - Python2 str对象中获取的是原始字节序列, unicode对象中是 Unicode字符

字符的标识, 即"码点"(0-114111范围内的数) Unicode字符用4~6位的16进制数来表示, 前加U+
字符的具体表述取决于所用的编码. 将码点转换为字节序列称之为编码, 将字节序列变为码点, 称之为解码

4.1~4.3
- 十进制代码在32-126范围的字节码,采用ASCII字符本身
- 制表符 换行符, 回车符,和\对应的字符, 采用转义序列\t, \n, \r 和\\
- 如果字节序列同时包含 ' "", 整个序列采用'区隔, 序列内的' 采用\'
- 其他字符采用十六进制转义序列显示. 

4.5 处理编码和解码错误
! ASCII字符是所有编码的共同子集, 能被所有编码模式编码,所以可以使用str.isascii()来判断Unicode字符是否由ASCII字符构成
UnicodeEncodeError: 出现此种错误,一般是字符不在当前编码类型可编码的字符集集合中
    - 处理方式有三, errors参数: ignore, 忽略所有不可编码的字符, replace: 用?替换不可编码的字符 xmlcharreplace 用xml文本替换不可编码字符
UnicodeDecodeError: 出现此种错误, 代表编码不能对当前部分字节进行解码. errors 参数设置为replace 用U+FFFD ? 来替换不可解码的字节

Python3 默认使用UTF-8编码, Python2默认使用ASCII编码, 所以.py文件中定义非UTF-8的编码字符时, 会出现SyntaxError

- python 库chardetect 用于识别文件的编码格式

4.6 处理文本文件
- Python的内置方法open, 会在读取文件内容时按照设置的编码方式进行解码, 所以write, read 都是操作的str对象 
    ! 打开文件, 如果不设置编码格式, 则会使用locale.getpreferredencoding() // Python3.6之后, 交互环境的IO输出输入默认都使用UTF-8
    ! 在二进制和字符之间进行转换, Python内部默认使用sys.getdefaultsystemencoding()
    ! 编码和解码文件名(不是文件内容), 使用sys.getfilesystemencoding(), 如果传入的文件名为字符, 则使用sys.getfilesystemencoding(), 如果是bytes, 则直接传给操作系统API
! 如果将一个字符串 以utf8的编码格式进行保存, 但是读取时不设置编码格式, 可能由于windows机器默认编码格式为cp1252 导致读取的字符串异常. 


4.7 为了正确比较而规范化Unicode字符串

unicodedata.normalize 用于规范化字符串 第一个参数可选'NFC', 'NFD', 'NFKC', 'NFKD'
NFC: 使用最少的码点构成等价的字符串
NFD: 把合成字符分解成基字符和单独的组合字符
NFKC 和NFKD 会兼容性分解字符, 替换成一个或者多个字符. 比如'½'-> '1/2'
    ! NFKC和NFKD规范化形式会导致数据损失, 应只在特殊情况下使用. 例如: 搜索和索引, 而不能用于持久存储文本

大小同一化: str.casefold() 与 str.lower() 类似, 只有德语中sharps 和希腊字母μ不同

4.8 对Unicode字符进行排序
"""


class UseCharacter:
    
    def encoding_method(aStr: str) -> bytes:
        return aStr.encode('utf-8')
    
    def decoding_method(aBytes: bytes) -> str:
        return aBytes.decode('utf-8')

    def test_error():
        print("Maitei angirũ")

class BytesAndBytesArray:

    @staticmethod
    def bytes_method(aStr: str) -> None:
        octets = bytes(aStr, encoding='U8') # utf-8 U8 utf_8
        print(octets, type(octets))

    @staticmethod
    def bytesarray_method(aList: list) -> None:
        arrayFoo = array('h', aList)
        result = bytearray(arrayFoo)
        print(result, type(result))


class FamiliarWithDefaultEncode:

    __expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

    @classmethod
    def loop_run(cls):
        my_file = open('dummy', 'w')
        for expression in cls.__expressions.split():
            value = eval(expression)
            print(f"{expression:>30} -> {value!r}")


class StringMatch:

    def nfc_equals(self, str_one, str_two) -> bool:
        return unicodedata.normalize("NFC", str_one) == unicodedata.normalize("NFC", str_two)

    def case_fold_equals(self, str_one: str, str_two: str) -> bool:
        return unicodedata.normalize("NFC", str_one).casefold() == \
            unicodedata.normalize("NFC", str_two).casefold()


def main():
    string = 'Duke'
    # print(UseCharacter.encoding_method(string))
    # bytesOne = b'Duke'
    # print(UseCharacter.decoding_method(bytesOne))
    # UseCharacter.test_error()
    # BytesAndBytesArray.bytes_method(string)
    # BytesAndBytesArray.bytesarray_method([-2, -1, 0, 1, 2])
    # FamiliarWithDefaultEncode.loop_run()
    spanish_cafe = "café"
    spanish_cafe_one = 'cafe\u0301'
    stringMatch = StringMatch()
    print(stringMatch.nfc_equals(spanish_cafe, spanish_cafe_one))
    print(stringMatch.case_fold_equals(spanish_cafe, spanish_cafe_one))



if __name__ == '__main__':
    main()