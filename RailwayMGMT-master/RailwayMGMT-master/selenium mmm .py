from selenium import  webdriver
import time
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get('https://myclass.lpu.in/')
reg_no=driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
reg_no.send_keys('12016050')
pass_word=driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
pass_word.send_keys('2001@Prateek')
enter=driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
enter.click()
time.sleep(3)
view_class=driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
view_class.click()
ongoing_class=driver.find_element_by_xpath("//<span>11:54</span>")
ongoing_class.click()