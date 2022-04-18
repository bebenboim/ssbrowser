from ssbrowser import browser
import time


chrome = browser.browser("test", "driver/chromedriver.exe", log=True)
chrome.open_chrome("https://google.com")

xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'

#send key to element and press enter
chrome.act_sendkey_enter(xpath, "Hello Google")
time.sleep(5)

#or you can still use build in selenium function
chrome.driver.get("https://google.com")
chrome.driver.find_element(xpath).send_keys("Hello Google")