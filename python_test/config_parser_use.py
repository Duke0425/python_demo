"""
    ConfigParser是Python类, 实现对于python程序基本配置语言, 构建类似于Micrsoft Windows INI文件结构
    ConfigParser允许编写最终用户可以轻松定制的Python程序

    ini配置文件格式 :
    [mysql]
    host = 127.0.0.1
    1. 注释使用# 或者;
    2. 使用键值对 key:value 或者 key=value
    3.[]中填写分区的名称
"""
from configparser import ConfigParser
from pathlib import Path
configString = """
[mysql]
host = 127.0.0.1
port = 3307
user = admin
password = 12356**
db = teacher

[postgresql]
host = localhost
port = 4396
user = engineer
password = diff44
db = student
"""
configDict = {
    "mysql": {
        "host":"127.0.0.1",
        "port": 3306,
        "user":"admin",
        "password":"2356**",
        "db":"teacher"
    },
    "postgresql":{
        "host":"127.0.0.1",
        "port": 3306,
        "user":"admin",
        "password":"2356**",
        "db":"teacher"
    }
}


class ConfigParserSimple:
    def __init__(self, aConfig):
        self.myConfig = aConfig

    @property
    def mysqlConfig(self):
        return self.myConfig['mysql']

    @property
    def pgsqlConfig(self):
        return self.myConfig['postgresql']

    @classmethod
    def read_ini_from_file(cls, aFilePath):
        if not Path(aFilePath).exists():
            return "File not exist"
        config = ConfigParser()
        config.read(aFilePath)

        if cls.verify_sections(config):
            return cls(config)

    @classmethod
    def read_ini_from_string(cls, aString):
        config = ConfigParser()
        config.read_string(aString)

        if cls.verify_sections(config):
            return cls(config)

    @classmethod
    def read_ini_from_dict(cls, aDict):
        config = ConfigParser()
        config.read_dict(aDict)

        if cls.verify_sections(config):
            return cls(config)

    @staticmethod
    def verify_sections(aConfig):
        if not aConfig.has_section('mysql'):
            print(f"Config file has section [mysql]")
            return False
        if not aConfig.has_section('postgresql'):
            print("Config file has section [postgresql]")
            return False
        return True

    def save_config_to_ini_file(self, aFilePath):
        with open(aFilePath, 'w') as file:
            self.myConfig.write(file)

    def __str__(self):
        configMysqlDict = configPgresqlDict = {}
        configList = ['host', 'port', 'user', 'password', 'db']
        for configName in configList:
            configMysqlDict[configName] = self.myConfig['mysql'][configName]
        for configName in configList:
            configPgresqlDict[configName] = self.myConfig['postgresql'][configName]
        
        return f"mysql: {configMysqlDict} \npostgresql: {configPgresqlDict}"

if __name__ == '__main__':
    configFromFile = ConfigParserSimple.read_ini_from_file("E:\\duke_summary_python\\resourse_files\\db.ini")
    configFromStr = ConfigParserSimple.read_ini_from_string(configString)
    configFromDict = ConfigParserSimple.read_ini_from_dict(configDict)
    print(configFromFile, configFromStr, configDict)
    
    configFromFile.mysqlConfig['host'] = "192.168.69.255"
    configFromFile.save_config_to_ini_file("E:\\duke_summary_python\\resourse_files\\db.ini")
    # host = configFromFile.mysqlConfig['host']
    # port = configFromFile.mysqlConfig['port']
    print(configFromFile.mysqlConfig['IP'])
    

    
    
    