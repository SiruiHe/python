from selenium import webdriver
'''
browser=webdriver.Chrome()
browser.get("https://www.baidu.com")
emailElem=browser.find_element_by_css_selector("#kw")
emailElem.send_keys("hello")
#heck=browser.find_element_by_css_selector("#identifierNext > div > button")
emailElem.submit()
new=browser.find_element_by_id("1")
new1=new.find_element_by_css_selector("a")
new1.click()
'''
browser = webdriver.Chrome()

browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

browser.find_element_by_xpath(r'//*[@id="1"]/h3/a[1]')
#browser.quit()