import os
from zlib import compress
from multiprocessing import Process

def save_to_datfile(aFileContent: str, aDatFilePath: str) -> None:
    compressContent = compress(aFileContent)
    with open(aDatFilePath, mode='wb') as fp:
        fp.write(compressContent)
    print(f"\r Save file succeed {aDatFilePath}")

def read_json_file(aFilePath) -> str:
    with open(aFilePath, 'r') as file:
        filecontent = file.read()
    return filecontent.encode('utf-8')

def single_json_transto_datfile(aFilePath: str) -> None:
    if not os.path.exists(aFilePath):
        print(f"{aFilePath} not exists")
        return

    filecontent = read_json_file(aFilePath)
    aDatFilePath = aFilePath.replace('.json', '.dat')
    save_to_datfile(filecontent, aDatFilePath)
    print(f"trans to dat file succeed {aDatFilePath}")

def main():
    exampleJsonFolder = r"E:\duke_summary_python\python_test\fileread_write\测试样例"
    for root, dir, files in os.walk(exampleJsonFolder):
        for f in files:
            if f.endswith('.json'):
                jsonFile = os.path.join(root, f)
                p = Process(target=single_json_transto_datfile, args=(jsonFile,))
                p.start()

if __name__ == '__main__':
    main()
