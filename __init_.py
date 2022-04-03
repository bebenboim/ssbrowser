# Created By Ben Saputra
# 2020 boim browser v1.5 -> Update v2.1 2022 Support Chrome and Add to Git

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pickle


class browser:
    """
    Simple selenium webdriver browser .
    headless: mode using bool Default False
    profile: is path where your firefox or chrome directory profile is
    driverpath: where webdriver path is default is in driver/webdriver
    log: if you want to print error massage just gift True default is False
    Note: All element search by Xpath 
    """
    def __init__(self, profile, driverpath, headless=False, log=False):
        self.gcdriver = driverpath
        self.headless = headless
        self.profile = profile
        self.log = log
    
    def open_firefox(self):
        """Opening Firefox Browser"""
        try:
            options = Options()
            options.headless = self.headless
            self.driver = webdriver.Firefox(options=options, executable_path=self.path_firefox, firefox_profile=self.profile_firefox)
            self.driver.get(self.linkdibuka)
            self.driver.maximize_window()
            self.act = ActionChains(self.driver)
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def open_chrome_remote(self, hostport:str):
        """Opening Chrome Browser with remote debug just gift debuggerAddress host:port ex: 127.0.0.1:7777"""
        try:
            option = webdriver.ChromeOptions() 
            option.add_experimental_option("debuggerAddress", hostport)
            self.driver = webdriver.Chrome(options=option, executable_path=self.path_chrome)
            self.driver.maximize_window()
            self.driver.get(self.linkdibuka)
            self.act = ActionChains(self.driver)
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def open_chrome(self, link):
        """Opening Chrome Browser"""
        try:
            option = webdriver.ChromeOptions() 
            option.headless = self.headles_mode
            option.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.driver = webdriver.Chrome(options=option, executable_path=self.path_chrome)
            self.driver.maximize_window()
            self.driver.get(link)
            self.act = ActionChains(self.driver)
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def save_cookie(self, filepath):
        """Saving Cookies to file with pickle"""
        with open(f"{filepath}.pkl", 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)

    def load_cookie(self, filepath):
        """Loading Cookies to file with pickle. Before you add load cookies first you must open domain realted to cookies"""
        with open(f"{filepath}.pkl", 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
    
    def open_link(self, link):
        try:
            self.driver.get(link)
            return self.driver.title
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def get_source_page(self):
        try:
            return self.driver.page_source
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def close_browser(self):
        try:
            self.driver.close()
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False

    def refresh_browser(self):
        try:
            self.driver.refresh()
            time.sleep(2)
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def act_sendKey(self, element , key):
        """Using ActionChains to send keys to element, provide element using Xpath, and key to send"""
        try:
            self.act.move_to_element(self.driver.find_element_by_xpath(element))
            self.act.send_keys(key)
            self.act.perform()
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def act_sendKey_click(self, element , key):
        """Using ActionChains to click and send keys to element, provide element using Xpath, and key to send"""
        try:
            self.act.move_to_element(self.driver.find_element_by_xpath(element))
            self.act.click()
            self.act.send_keys(key)
            self.act.perform()
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False

    def act_sendKey_clear(self, element , key):
        """Using ActionChains to clear, send keys and click field to element, provide element using Xpath, and key to send"""
        try:
            self.act.move_to_element(self.driver.find_element_by_xpath(element))
            self.act.click()
            for _ in range(35):
                self.act.send_keys(Keys.BACK_SPACE)
            self.act.send_keys(key)
            self.act.perform()
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def act_sendkey_enter(self, element, sendkey):
        """Send Enter key to element"""
        try:
            self.act.move_to_element(self.driver.find_element_by_xpath(element))
            self.act.send_keys(sendkey, Keys.ENTER)
            self.act.send_keys(Keys.ENTER)
            self.act.perform()
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def act_sendkey_enter_click(self, element, sendkey):
        """Click, send key and Send Enter to element"""
        try:
            self.aksi.move_to_element(self.driver.find_element_by_xpath(element))
            self.aksi.click()
            self.aksi.send_keys(sendkey, Keys.ENTER)
            self.aksi.send_keys(Keys.ENTER)
            self.aksi.perform()
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False

    def act_btn(self, element):
        """Click button by xpath"""
        try:
            self.act.move_to_element(self.driver.find_element_by_xpath(element))
            time.sleep(1)
            self.act.click()
            self.act.perform()
        except Exception as e:
            if self.log:
                print(e)
    
    def act_btn_scrol(self, element):
        """Scroling to element and Click button by xpath"""
        try:
            scrol = self.driver.find_element_by_xpath(element)
            scrol.location_once_scrolled_into_view
            time.sleep(1)
            self.act.move_to_element(self.driver.find_element_by_xpath(element))
            time.sleep(1)
            self.act.click()
            self.act.perform()
        except Exception as e:
            if self.log:
                print(e)
    
    def act_get_text(self, element):
        """Get text on element using xpath"""
        try:
            text = self.driver.find_element_by_xpath(element).text
            return text
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def act_get_link(self, element):
        """Get link on element using xpath"""
        try:
            link = self.driver.find_element_by_xpath(element).get_attribute('href')
            return link
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def move_to_iframe(self, xpath):
        """Move to specific iframe using xpath"""
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))
            return True
        except:
            return False
    
    def move_default_iframe(self):
        self.driver.switch_to.default_content()

    def wait_until_show(self, xpath, timeout=15):
        """Wait until element show on DOM , using timeout=int to set max timeout wait default 15 second"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False
    
    def wait_until_gone(self, xpath, timeout=15):
        """Wait until element gone on DOM , using timeout=int to set max timeout wait default 15 second"""
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except Exception as e:
            if self.log:
                print(e)
            return False