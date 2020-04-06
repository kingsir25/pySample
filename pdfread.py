# -*- encoding: utf-8 -*-

try:
    from urllib.request import urlopen
except:
    from urllib import urlopen

from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import  LAParams

# 读取pdf的函数，返回内容
def readPdf(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr=rsrcmgr, outfp=retstr, laparams=laparams)

    process_pdf(rsrcmgr=rsrcmgr, device=device, fp=pdf_file)
    device.close()

    content = retstr.getvalue()
    retstr.close()

    return content


url = "http://www.pythonscraping.com/pages/warandpeace/chapter1.pdf"
pdf_file = urlopen(url) # 也可以换成本地pdf文件，用open rb模式打开
content = readPdf(pdf_file)
print(content)
pdf_file.close()

pdf_file2 = open("基金入门基础知识.pdf","rb")
content2 = readPdf(pdf_file2)
print(content2)
pdf_file2.close()

pdf_file3 = open("ozeki06.pdf","rb")
content3 = readPdf(pdf_file3)
print(content3)
pdf_file3.close()