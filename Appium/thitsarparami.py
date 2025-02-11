import time

from appium  import  webdriver
from appium.options.android import  UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains


options=UiAutomator2Options()
url='http://127.0.0.1:4723'
options.set_capability('ignoreHiddenApiPolicyError',True)

driver=webdriver.Remote(url,options=options)


def bottom_nav_tabs():
    bottom_nav_list=['Home','Search','Library','Player','More']
    for nav in bottom_nav_list:
        el=driver.find_element(AppiumBy.ACCESSIBILITY_ID,nav)
        el.click()
        print(f'{nav} Click')
        time.sleep(3)


def category_tabs():
    category_list=['တရားတော်များ','ဓမ္မပို့ချချက်တရားတော်များ','ဓမ္မစာအုပ်များ','ဘုရားရှိခိုးနှင့်ဝတ်ရွတ်စဥ်','တိုက်ရိုက်ထုတ်လွှင့်ခြင်း','အွန်လိုင်းရေဒီယို']
    for i in range(len(category_list)):
        el=driver.find_element(AppiumBy.ACCESSIBILITY_ID,category_list[i])
        el.click()
        print(f'{i+1} . {category_list[i]} Click')
        time.sleep(3)
        driver.back()
        time.sleep(3)


def scroll_left():
    scroll_el_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View'
    scroll_element=driver.find_element(AppiumBy.XPATH,scroll_el_xpath)
    scroll_el_size=scroll_element.size
    print('Scroll Element Size' ,scroll_el_size)
    width=scroll_el_size['width']
    height=scroll_el_size['height']
    start_x=width-100
    end_x=0 # left
    # start_x=0
    print('Before Scroll')
    time.sleep(6)
    action=ActionChains(driver)
    action.move_to_element(scroll_element)
    action.click_and_hold()
    action.move_by_offset(end_x-start_x,0)
    action.release()
    action.perform()
    print('After Scroll')


def scroll_right():
    scroll_el_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View'
    scroll_element=driver.find_element(AppiumBy.XPATH,scroll_el_xpath)
    scroll_el_size=scroll_element.size
    print('Scroll Element Size' ,scroll_el_size)
    width=scroll_el_size['width']
    height=scroll_el_size['height']
    start_x=0
    end_x=width-100 # right
    print('Before Scroll')
    time.sleep(6)
    action=ActionChains(driver)
    action.move_to_element(scroll_element)
    action.click_and_hold()
    action.move_by_offset(end_x-start_x,0)
    action.release()
    action.perform()
    print('After Scroll')
