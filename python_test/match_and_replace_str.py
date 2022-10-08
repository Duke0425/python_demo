import re
import sys

def alter(aFile, aOldStr, aNewStr):
    with open(aFile, 'r', encoding="utf-8") as file_one:
        content = file_one.read()
    
    new_content = re.sub(aOldStr,aNewStr, content)

    with open(aFile, 'w', encoding="utf-8") as file_new:
        file_new.write(new_content)


if __name__ == '__main__':
    alter('e:/duke_summary_python/resourse_files/buildozer.spec',"#android.manifest.intent_filters", "android.manifest.intent_filters")
