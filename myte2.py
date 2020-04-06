from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(browser.title)

browser.find_element_by_id("ctl00_ctl00_TutorialPopUpControl_btnClose").click() 
browser.implicitly_wait(60)
browser.find_element_by_id("ctl00_ctl00_NavigationBarMenu").click() 
browser.implicitly_wait(60)
browser.find_element_by_id("ctl00_ctl00_NavigationBarMenu").click() 
browser.implicitly_wait(60)
Select(browser.find_element_by_name("ctl00$MainContentPlaceHolder$ddl_Reports")).select_by_visible_text("Forecasted Time Details")
browser.implicitly_wait(60)
Select(browser.find_element_by_name("ctl00$MainContentPlaceHolder$ddl_StartDates$dropdownTimePeriod")).select_by_visible_text("2019/4/15")

sleep(2)
Select(browser.find_element_by_name("ctl00$MainContentPlaceHolder$ddl_EndDates$dropdownTimePeriod")).select_by_visible_text("2019/4/30")
sleep(2)
browser.find_element_by_id("ctl00_MainContentPlaceHolder_InOutEnterpriseId_btn_All_In").click() 
sleep(2)
browser.find_element_by_id("ctl00_MainContentPlaceHolder_btn_RunReport").click()

