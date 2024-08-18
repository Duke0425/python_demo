# CPyton Cython Jython是什么?
Qestion(stackOverFlow)[https://stackoverflow.com/questions/17130975/python-vs-cpython]
## 1. CPython
- CPython是原始的python实现(The traditional implement of Python(nickmaed Cpython))
- CPython恰好也是用C实现的。这实际上只是一个实现细节，CPython将Python代码（透明的）编译为字节码，并在评估循环中解释该字节码
- CPython是第一个实现新功能的， Python语言开发基于CPytho
## 2.Cython
- CPython 不会自行将 Python 代码转换为 C。相反，它运行一个解释器循环。有一个项目可以将 Python 风格的代码转换为 C 语言，名为Cython。Cython 向 Python 语言添加了一些扩展，并允许您将代码编译为 C 扩展，即插入CPython解释器的代码。
## 3.Jython， IronPython, PyPy
- Jython、IronPython和PyPy是 Python 编程语言当前的“其他”实现；它们分别用 Java、C# 和 RPython（Python 的子集）实现。
- Jython 将您的 Python 代码编译为Java字节码，以便您的 Python 代码可以在 JVM 上运行。
- IronPython 允许您在Microsoft CLR上运行 Python 。
- PyPy 是用 Python（Python 的一个子集）实现的，可以让你比 CPython 更快地运行 Python 代码.
- 