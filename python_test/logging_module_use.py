"""
    * logging模块
        - 日志的记录

        * 日志级别(默认的日志级别有五个, 表示了事件的严重程度不同) 从上到下, 事件的严重程度依次增加
            - DEUBG
            - INFO
            - WARNING
            - ERROR
            - CRITICAL
"""
import logging
import logging.config

def default_logger_test():
    """
        使用默认的logger 来开始记录日志, 不需要其余的设置
    """
    logging.debug("Debug Message")
    logging.info("Debug Message")
    logging.warning("Debug Message")
    logging.error("Debug Message")
    logging.critical("Debug Message")

def cus_logger_test():
    """
        自定义日志的配置
            - level: 设置显示的特定的严重级别
            - filename: 指定的文件名
            - filemode: 如果有filename存在, 文件通过filemode的模式打开,  默认是 'a'(追加)
            - format: 日志的格式
    """
    # logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG, filemode='w', filename='logging_test.log', format="%(name)s - %(levelname)s - %(message)s")

    logging.debug("debug Message")
    logging.info("Debug Message")
    logging.warning("Debug Message")
    logging.error("Debug Message")
    logging.critical("Debug Message")
    """
        记录回溯的信息
    """
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Atrribute Error", exc_info=True)

class LoggerSingeton:

    def __init__(self):
        self.myLogger = logging.getLogger("TEST")
        
        self.AddStream()

    def SetLevel(self, aLevel):
        self.myLogger.setLevel(aLevel)

    def AddStream(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.myLogger.addHandler(handler)

    def AddLogFile(self, aFilePath, aMode='a', aEncoding='utf-8'):
        handler = logging.FileHandler(aFilePath,  mode=aMode, encoding=aEncoding)
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.myLogger.addHandler(handler)

    def warning(self, aMessage):
        self.myLogger.warning(aMessage)

if __name__ == '__main__':
    # default_logger_test()
    # cus_logger_test() # 使用默认日志对象 root

    """
        通过类来创建日志处理器
    """
    # logger = LoggerSingeton()
    # logger.SetLevel(logging.DEBUG)
    # logger.AddLogFile('test.log')
    # logger.warning("warning message test")

    """
        通过配置文件创建日志处理器
    """
    logging.config.fileConfig(fname='E:\\duke_summary_python\\resourse_files\\logger.conf', disable_existing_loggers=False)

    simpleLogger = logging.getLogger(__name__)
    simpleLogger.error("dangerous")

    