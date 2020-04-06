# cmd环境下，用pip install selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import os

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()}
options.add_experimental_option('prefs', prefs)
#静默运行
#options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)

# browser=webdriver.Chrome()
# browser=webdriver.Firefox()
# browser=webdriver.Edge()   #  Microsoft Edge
# browser=webdriver.Safari()
# browser=webdriver.Android()
# browser=webdriver.BlackBerry()
# browser=webdriver.Ie()
# browser=webdriver.Opera()
# browser=webdriver.PhantomJS()

#browser = webdriver.Chrome()
#chrome webdriver 驱动下载chromedriver.exe
#http://chromedriver.storage.googleapis.com/index.html
#拷贝到chrome安装目录C:\Program Files (x86)\Google\Chrome\Application
#添加系统path=C:\Program Files (x86)\Google\Chrome\Application
browser.get("https://myte.accenture.com")
browser.set_window_size(500,800)

browser.implicitly_wait(60)# 隐性等待到加载完毕，最长等60秒
#browser.find_element_by_id("kw").send_keys("python")
#单击搜索按钮
browser.find_element_by_id("ctl00_ctl00_TutorialPopUpControl_btnClose").click() 
browser.implicitly_wait(60)
# browser.find_element_by_id("ctl00_ctl00_NavigationBarMenu").click() 
browser.find_element_by_link_text("Reports").click() 
browser.implicitly_wait(60)
Select(browser.find_element_by_name("ctl00$MainContentPlaceHolder$ddl_Reports")).select_by_visible_text("Forecasted Time Details")
browser.implicitly_wait(60)
Select(browser.find_element_by_name("ctl00$MainContentPlaceHolder$ddl_StartDates$dropdownTimePeriod")).select_by_visible_text("2019/4/15")
sleep(2)# 强制等待2秒再执行下一步
Select(browser.find_element_by_name("ctl00$MainContentPlaceHolder$ddl_EndDates$dropdownTimePeriod")).select_by_visible_text("2019/4/15")
sleep(2)
browser.find_element_by_id("ctl00_MainContentPlaceHolder_InOutEnterpriseId_btn_All_In").click() 
sleep(2)
browser.find_element_by_id("ctl00_MainContentPlaceHolder_btn_RunReport").click()

# js = "$find('ctl00_MainContentPlaceHolder_ReportViewerControl').exportReport('CSV');"
# browser.execute_script(js)  #执行JavaScript代码
#browser.execute_async_script()
sleep(180)
browser.find_element_by_id("ctl00_MainContentPlaceHolder_ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
browser.implicitly_wait(60)
#WebDriverWait(browser, 600).until(browser.find_element_by_link_text("CSV (逗号分隔)"))
browser.find_element_by_link_text("CSV (逗号分隔)").click()
#关闭浏览器
#browser.close()

# find_elements_by_id
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector