import re

def UpdateVersionForPythonCode():
    with open('E:\\platform\\shared\\py\\ms\\common\\android_edition_var.py', mode = 'r', encoding = 'utf-8') as stream:
        content = stream.read()
    
    pCodeFound = re.findall(r"(AndroidClientEngineerMode\s*=\s*(\w+))", content, re.MULTILINE)

    pCode, pStr = pCodeFound[0]
    pCodeNew = pCode.replace(pStr, 'True')
    content = content.replace(pCode, pCodeNew)

    cCodeFound = re.findall(r"(AndroidClientDebugMode\s*=\s*(\w+))", content, re.MULTILINE)

    cCode, cStr = cCodeFound[0]

    vCodeFound = re.findall(r"(AndroidClientLANGSetEnglish\s*=\s*(\w+))", content, re.MULTILINE)

    vCode, vStr = vCodeFound[0]


    with open('E:\\platform\\shared\\py\\ms\\common\\android_edition_var.py', mode = 'w', encoding = 'utf-8') as stream:
        stream.write(content)


if __name__ == '__main__':
    UpdateVersionForPythonCode()