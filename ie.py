from selenium import webdriver
import os
browser = webdriver.Ie()

browser.get("http://www.baidu.com")
browser.implicitly_wait(60)
#在百度搜索框中输入关键字"python"
browser.find_element_by_id("kw").send_keys("python")
#单击搜索按钮
browser.find_element_by_id("su").click() 

#关闭浏览器
#browser.close()
