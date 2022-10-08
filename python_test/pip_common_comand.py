"""
    PIP常见指令

    PIP模块: Python包管理器, 从3.4之后, 为每一个python安装包标配了pip

    1. 查看pip版本
        pip -V
        pip --version
    2. 帮助
        pip help
    3. 安装三方库
        - 普通wheel- 只包含python文件, 没有编译的扩展, 并且原生支持Python2和3
        - 纯Python Wheel : 只包含Python文件, 没有编译的扩展, 但不支持原生Python2和3
        - 平台Wheel :包含Python文件和编译的扩展, 但本身不支持Python2和3. 该类型的Wheel特定于平台, 例如Windows和macOS, 因为其包含编译的扩展
        a.普通安装
            pip install 库名
        b.指定库版本安装
            pip install 库名==版本号
        c.安装WHL文件
            pip install xx.Wheel
            WHL文件是以Wheel格式保存的Python安装包，Wheel是Python发行版的标准内置包格式。WHL文件包含Python安装的所有文件和元数据，
            其中还包括所使用的Wheel版本和打包的规范。WHL文件使用Zip压缩进行压缩，实际上也是一种压缩文件。
            Wheel格式是由PEP 427在2012年定义，取代了原先使用的.EGG安装包格式。Wheel支持不需要编译的安装过程，
            安装速度更快、更可靠，且支持离线安装。Wheel现在被认为是Python的二进制包的标准格式。
        d.升级pip版本
            pip install --upgrade pip
    4. 批量导出项目用到的库
        pip freeze > requirements.txt
    5. 批量安装库
        pip install -r requirements.txt
    6. 卸载已安装库
        pip uninstall 库名
    7. pip list
        a. 查看已安装的库
            pip list
        b. 查看可更新的库
            pip list -o

    8.指定源操作
        a.在单次安装时指定源
            pip install 库名 -i 源地址
        b.设置默认源
            pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
        c.换回原来的源
            pip config unset global.index-url
    9. 查看包的版本和安装位置, 以及详细信息
        pip show myPackage
    10. 检查安装的软件包是否都具有兼容的依赖性
        pip check myPackage
    11. pip重安装
        python -m ensurepip
        d:\your path\venv\scripts\python.exe -m pip install --upgrade pip
"""
