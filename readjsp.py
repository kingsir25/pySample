from bs4 import BeautifulSoup #导入bs4库
html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's stopy</b></p>
<p class="story">Once upon a time there were three little sisters;and their names where
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
"""
#soup = BeautifulSoup(html_str,'lxml') #html.parser是解析器，也可是lxml
#print(soup.prettify())
soup = BeautifulSoup(open(r'C:\Users\Administrator\OneDrive\study\python\beantest.jsp','r',encoding='utf-8'),features='html.parser')#html.parser是解析器，也可是lxml
print(soup.title.string)
print(soup.title.name)


