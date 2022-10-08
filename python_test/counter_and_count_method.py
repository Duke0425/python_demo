"""
    Counter方法: 如何更pythonic地对象计数, 排序. 
    模块: collections
    参数: 接受一个可迭代序列(列表. 字符串, 元组..)
    返回值为一个字典: 元素为键, 频率为值
"""
from collections import Counter

misCounter = Counter("mississippi")

Counter(('Mississippi', ))

# * 1. 使用类的构造方法来模拟类似结果
cOne = Counter(i=4, s=4, p=2, m=1)
cTwo = Counter(i=1)
# * 2. 通过.update,来加入另一个计数器对象或者计数器对象映射: 更新对象计数
cOne.update(cTwo)
cOne.update({'i':1, 's':10, 'p':2})
cOne.update("miss")

# * 3. 访问计数器的内容
misCounter["i"]
# TODO 类似于字典的取值, 可以使用.keys() .values() .items()来循环获取值
for letter in misCounter:
    print(f"{letter}, {misCounter[letter]}")

for letter in misCounter.keys():
    print(letter, misCounter[letter])

# 如果不存在键, 则会返回0, 而不是keyError

# * 4.查找最常见的对象 
"""
使用most_common来返回对象的当前计数排序的列表
接受参数: 整数N, 获得n个最多计数的对象, 省略此参数或者设置为None时, 返回所有对象的一个元组列表
"""
animalCounter = Counter(dog=3, cat=100, lion=23, tiger=2000, elephant=99, alligator=2, giraffe=80)
animalCounter.most_common()
animalCounter.most_common(None)
animalCounter.most_common(3)

# 获取最不常见的参数列表 前三
animalCounter.most_common()[:-4:-1]

# * 5.文件中字符的计数(现有一个文本文档pythonic.txt, 读取此文件, 并且对其中的字符进行排序)
def count_letters(aFile):
    with open(aFile, 'r') as file:
        contentList = file.readlines()
    letterCounter = Counter()
    for line in contentList:
        lineLetters = [letter for letter in line.lower() if letter.isalpha()]
        letterCounter.update(lineLetters)
    return letterCounter.most_common(3)

print(count_letters("../resourse_files/pythonic.txt"))

"""
    Python中的count方法
    1. 列表的count方法, 对于列表某个元素进行计数
    2. 字符串的count方法, 对于字符串的特定字符串进行查询计数, 并且可以设置查询的index头和尾
"""
simpleList = ['happy', 'blue', 'emo', "it's a nice day"]
countNum = simpleList.count('happy')

stringElement = simpleList[3]
countCharNum = stringElement.count('a')

countCharNumIx = stringElement.count('a', 6)
