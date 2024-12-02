"""
字符的最佳定义就是Unicode字符. 
  - Python3 str对象 就是Unicode字符, 
  - Python2 str对象中获取的是原始字节序列, unicode对象中是 Unicode字符

字符的标识, 即"码点"(0-114111范围内的数) Unicode字符用4~6位的16进制数来表示, 前加U+
字符的具体表述取决于所用的编码. 将码点转换为字节序列称之为编码, 将字节序列变为码点, 称之为解码

4.1~4.3
"""
class UseCharacter:
    
    def encoding_method(aStr: str) -> bytes:
        return aStr.encode('utf-8')
    
    def decoding_method(aBytes: bytes) -> str:
        return aBytes.decode('utf-8')

def main():
    string = 'Duke'
    print(UseCharacter.encoding_method(string))
    bytesOne = b'Duke'
    print(UseCharacter.decoding_method(bytesOne))


if __name__ == '__main__':
    main()