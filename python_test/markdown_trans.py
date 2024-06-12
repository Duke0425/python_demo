import markdown

import os
GTK_FOLDER = r'F:\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
import weasyprint

markdown_file = open('D:\Typora\Emei Project\图像不增量绘制.md', mode='r', encoding="utf-8")
markdown_string = markdown_file.read()
markdown_file.close()

html = markdown.markdown(markdown_string, extensions=['md_in_html'])

pdf = weasyprint.HTML(string=html).write_pdf()
with open('output.pdf', 'wb') as f:
    f.write(pdf)
