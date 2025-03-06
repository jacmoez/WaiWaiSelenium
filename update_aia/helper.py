from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import  load_dotenv
import os
from appium.webdriver.common.appiumby import AppiumBy


load_dotenv()

options = UiAutomator2Options()
options.set_capability("ignoreHiddenApiPolicyError",True)
options.set_capability("platformName","Android")
driver=webdriver.Remote(os.getenv('url'), options=options)


def click_by_xpath(xpath):
    driver.find_element(AppiumBy.XPATH,xpath).click()

def send_keys_by_xpath(xpath,value):
    driver.find_element(AppiumBy.XPATH,xpath).send_keys(value)

def click_by_accessibility_id(idd):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,idd).click()

def get_text_by_xpath(xpath):
    return driver.find_element(AppiumBy.XPATH,xpath).text
