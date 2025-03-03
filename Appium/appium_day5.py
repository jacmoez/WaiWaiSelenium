from argparse import Action

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import Interaction, POINTER
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located, element_to_be_clickable  # Correct import
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


options = UiAutomator2Options()
options.set_capability("ignoreHiddenApiPolicyError",True)
options.set_capability("platformName","Android")
URL = 'http://127.0.0.1:4723'
driver=webdriver.Remote(URL, options=options)

package_name='com.aiamm.plus.uat'

# install app
def install_app():
    try:
        driver.install_app('/Users/user/Documents/AMSProjects/Apks/aia-plus-uat-release-2025-01-08.apk')
        time.sleep(5)
    except Exception as e :
        print("Could not install error")
    print('------------- install --------')


# uninstall if exist
def uninstall_app():

    if driver.is_app_installed(package_name):
        driver.remove_app(package_name)
        print("After uninstalled")
    else:
        print('No app is installed')
    print('----- uninstall ----')

options.set_capability("appPackage",package_name)
options.set_capability("appWaitActivity","com.aiamm.plus.uat.dev.*")

def open_app():
    driver.launch_app()
    time.sleep(2)
    driver.activate_app(package_name)
    time.sleep(3)
    print('------------- App is opened -------------')


# change language
def change_language():
    # click language drop down
    language_dd_xpath='//android.view.View[@content-desc="ic_order_down"]'
    driver.find_element(AppiumBy.XPATH,language_dd_xpath).click()

    time.sleep(3)

    # Burmese
    burmese_lan_xpath='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]'
    driver.find_element(AppiumBy.XPATH,burmese_lan_xpath).click()

    time.sleep(3)

    # Done button
    done_btn_xpath='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]'
    driver.find_element(AppiumBy.XPATH,done_btn_xpath).click()

    time.sleep(5)

    # English
    # click language drop down again
    driver.find_element(AppiumBy.XPATH,language_dd_xpath).click()

    # eng language option
    eng_lan_xpath='(//android.widget.TextView[@text="English"])[1]'
    driver.find_element(AppiumBy.XPATH,eng_lan_xpath).click()
    # click done button again
    driver.find_element(AppiumBy.XPATH,done_btn_xpath).click()

    time.sleep(3)

    print('------------- Change language -------------')


def login_with_error():
    time.sleep(5)
    # login button
    login_btn_path='//android.widget.ScrollView/android.view.View[2]'
    driver.find_element(AppiumBy.XPATH,login_btn_path).click()

    time.sleep(5)

    # mobile or email
    email_or_mobile_path='//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]'
    email="qa@gmail.com"
    # add invalid email
    driver.find_element(AppiumBy.XPATH,email_or_mobile_path).send_keys(email)

    time.sleep(5)

    # password
    password_path='//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
    # add invalid password
    password="aq123"
    driver.find_element(AppiumBy.XPATH,password_path).send_keys(password)

    time.sleep(10)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Demo').click()
    time.sleep(5)

    # login button
    login_btn_path='//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]'
    driver.find_element(AppiumBy.XPATH,login_btn_path).click()

    time.sleep(5)

    # print login error message
    err_msg_el=driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Authentication Failed!"]').text
    print("Error Message : ",err_msg_el)



    print('------------- login ----------------')


def loginFirstTime():
    time.sleep(5)
    # login button
    login_btn_path='//android.widget.ScrollView/android.view.View[2]'
    driver.find_element(AppiumBy.XPATH,login_btn_path).click()

    time.sleep(5)

    # mobile or email
    email_or_mobile_path='//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]'
    phone="09764426445"
    driver.find_element(AppiumBy.XPATH,email_or_mobile_path).send_keys(phone)

    time.sleep(5)

    # password
    password_path='//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
    password="P@ssw0rd2026@"
    driver.find_element(AppiumBy.XPATH,password_path).send_keys(password)

    time.sleep(5)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Demo').click()
    time.sleep(5)

    # login button
    login_btn_path='//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]'
    driver.find_element(AppiumBy.XPATH,login_btn_path).click()

    time.sleep(5)




    print('------------- login ----------------')


def loginSecondTime():
    # login button - first page
    login_btn_path='//android.widget.ScrollView/android.view.View[2]'
    driver.find_element(AppiumBy.XPATH,login_btn_path).click()
    time.sleep(4)
    # password
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').send_keys('P@ssw0rd2026@')
    # login button
    driver.find_element(AppiumBy.XPATH,'//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]').click()
    time.sleep(20)

def PolicyRequests():
    # time.sleep(20)
    wait=WebDriverWait(driver,20)
    # number
    policy_request=wait.until(presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'PolicyRequests')))
    policy_request.click()
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID,'PolicyRequests').click()
    time.sleep(5)

    # member information change
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Member Information Change"]').click()
    time.sleep(5)

    # beneficiary information
    driver.find_element(AppiumBy.XPATH,'(//android.view.View[@content-desc="Logo"])[3]').click()
    time.sleep(5)

    # choose a policy
    driver.find_element(AppiumBy.XPATH,'(//android.view.View[@content-desc="checkbox"])[1]').click()

    # continue
    driver.find_element(AppiumBy.XPATH,'//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]').click()



def create_a_new_beneficiary():
    time.sleep(2)
    # add benificiary
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Add beneficiary"]').click()
    time.sleep(5)
    # create a new one
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Create a new one"]').click()
    time.sleep(3)
    # full name
    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.widget.EditText[1]').send_keys("New beneficiary one")
    # date of birth
    # # click date icon
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID,'ic_calendar').click()
    # time.sleep(3)
    # # select date
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Switch to selecting a year').click()
    # time.sleep(3)
    # #scroll
    # window_size=driver.get_window_size()
    # width=window_size['width']
    # x=width/2
    # driver.swipe(x,800,x,1600)
    # time.sleep(3)
    # # choose year
    # driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Navigate to year 1998"]/android.widget.Button').click()
    # time.sleep(3)
    #
    # # edit icon
    # driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button').click()
    # #edit text
    # driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').send_keys('04/11/1998')
    # driver.press_keycode(8)
    # driver.press_keycode(8)
    # driver.press_keycode(7) # 0
    # driver.press_keycode(11) # 7-16 (0-9)
    # driver.press_keycode(8)
    # driver.press_keycode(16)
    # driver.press_keycode(16)
    # driver.press_keycode(15)
    # date_list=[8,8,7,11,8,16,16,15]
    # for dt in date_list:
    #     driver.press_keycode(dt)
    # # ok
    # driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button').click()
    time.sleep(3)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'ic_calendar').click()

    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button').click()
    time.sleep(5)
    # edit text
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').clear()
    time.sleep(2)
    date_list=[8,8,7,11,8,16,16,15]
    for dt in date_list:
        driver.press_keycode(dt)
    # ok
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="OK"]').click()
    time.sleep(3)

    #phone
    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.widget.EditText[3]').send_keys('09444333222')
    # female
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Female"]').click()

    window_size=driver.get_window_size()
    width=window_size['width']
    x=width/2
    driver.swipe(x,1600,x,800)
    time.sleep(5)

    # NRC detail
    driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="trailingIcon"]').click()
    time.sleep(5)
    time.sleep(3)
    wait=WebDriverWait(driver,20)
    # number
    number_scroll=wait.until(presence_of_element_located((AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[1]/android.view.View[1]')))
    number_rect=number_scroll.rect

    #{'height': 366, 'width': 163, 'x': 53, 'y': 1031}
    print(number_rect)
    scroll_nrc(number_rect,4)

    #nrc
    time.sleep(5)
    nrc_scroll=wait.until(presence_of_element_located((AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[1]/android.view.View[2]/android.view.View')))
    nrc_rect=nrc_scroll.rect
    scroll_nrc1(nrc_rect,12)

    #Char
    time.sleep(5)
    city_scroll=wait.until(presence_of_element_located((AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[1]/android.view.View[3]')))
    city_rect=city_scroll.rect
    #scroll_nrc1(city_rect,3)

    # nrc no
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').send_keys('034194')

    time.sleep(3)
    # done
    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[2]').click()
    time.sleep(3)

    # front
    driver.find_element(AppiumBy.XPATH,'(//android.view.View[@content-desc="ic_upload_cloud"])[1]').click()
    time.sleep(3)

    # photo gallery
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Photo Gallery"]').click()
    time.sleep(3)

    # front image
    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]').click()
    time.sleep(8)

    #back
    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]').click()
    time.sleep(3)

    # photo gallery
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Photo Gallery"]').click()
    time.sleep(3)

    # front image
    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[2]').click()
    time.sleep(3)

    # create
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Create"]').click()

    #

def  add_second_new_beneficiary():
    # scroll_element('Add beneficiary')
    # driver.find_element(AppiumBy.XPATH,'(//android.view.View[@content-desc="iconResId"])[2]').click()
    # click_by_xpath('//android.widget.TextView[@text="Select from existing beneficiaries"]')
    # time.sleep(1)
    # click_by_xpath('//android.view.View[@content-desc="checkbox"]')
    # click_by_xpath('//android.widget.TextView[@text="Add"]')
    # click_by_id('iconResId')
    # time.sleep(2)
    # click_by_id('trailingIcon')
    # send_keys_by_xpath('//android.widget.EditText','CHILD')
    # click_by_xpath('//android.widget.TextView[@text="CHILD"]')
    # click_by_xpath('//android.widget.TextView[@text="Done"]')
    # send_keys_by_xpath('//android.widget.EditText[@text="100"]',50)

    # seek_bar=driver.find_element(AppiumBy.XPATH,'//android.widget.SeekBar')
    # change_seekbar_percent(seek_bar,150)
    time.sleep(2)
    # scroll_element('Total share percentage')
    window_size=driver.get_window_size()

    window_size=driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]').size
    width=window_size['width']
    x=width/2
    print('Width : ',x)
    print('Height : ',window_size['height'])
    driver.swipe(x,440,x,100)
    time.sleep(5)

    click_by_xpath('(//android.view.View[@content-desc="trailingIcon"])[2]')
    time.sleep(2)

    send_keys_by_xpath('//android.widget.EditText','PARENT')
    time.sleep(3)
    click_by_xpath('//android.widget.TextView[@text="PARENT"]')
    # //android.widget.TextView[@text="PARENT"]
    click_by_xpath('//android.widget.TextView[@text="Done"]')

    time.sleep(2)
    seek_bar1=driver.find_element(AppiumBy.XPATH,'//android.widget.SeekBar[@text="0.0"]')
    actions=ActionChains(driver)
    actions.move_to_element(seek_bar1).perform()
    change_seekbar_percent(seek_bar1,150)
    time.sleep(2)
    first_seek_bar_edit=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@text="100"]')
    first_seek_bar_edit.click()
    first_seek_bar_edit.clear()
    time.sleep(2)
    # second seek bar text
    text=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@text="57"]').text
    val=100-int(text)
    time.sleep(2)
    # send to first
    xp='//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.EditText[2]'
    send_keys_by_xpath(xp,val)
    time.sleep(2)
    click_by_xpath('//android.widget.TextView[@text="Save changes"]')



# 65 - 200
# 50 -?



def change_seekbar_percent(seek_bar,move_to_x):
    x_start=seek_bar.location['x']
    y_start=seek_bar.location['y']+(seek_bar.size['height']//2)
    print("SeekView :",x_start,y_start)
    end_x=x_start+seek_bar.size['width']
    actions=ActionChains(driver)
    # move_to_x=x_start+int((end_x-x_start)*0.4)
    # move_to_x=x_start+int(seek_bar.size['width']*0.4)
    # move_to_x=153
    print("SeekView : start x, y start",x_start,y_start)
    print('move to ',500)
    print('end x ',end_x)
    print('width ',seek_bar.size['width'])
    actions.move_to_element_with_offset(seek_bar,0,0).click_and_hold().move_by_offset(end_x-x_start,0).release().perform()
    actions.move_to_element_with_offset(seek_bar,0,0).click_and_hold().move_by_offset(move_to_x-x_start,0).release().perform()



def logout():
    # settings
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Settings').click()
    time.sleep(2)
    # logout
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Log out"]').click()
    # popup ok
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="OK"]').click()
def register():
    # register
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Register now"]').click()
    time.sleep(3)
    # No, I am not
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="No, I am not"]').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    # Yes, I am
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Yes, I am"]').click()
    time.sleep(2)
    create_account()



def create_account():
    driver.find_element(AppiumBy.XPATH,'//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.EditText[1]').clear()
    # full name
    full_name="Wai"
    driver.find_element(AppiumBy.XPATH,'//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.EditText[1]').send_keys(full_name)
    # dob
    driver.find_element(AppiumBy.XPATH,'//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.EditText[2]').click()
    time.sleep(5)
    # edit
    driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button').click()
    time.sleep(3)
     # edit text
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').clear()
    time.sleep(2)
    date_list=[8,8,7,11,8,16,16,15]
    for dt in date_list:
        driver.press_keycode(dt)
    # ok
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="OK"]').click()
    time.sleep(3)

    # female
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Female"]').click()
    time.sleep(5)
    window_size=driver.get_window_size()
    width=window_size['width']
    x=width/2
    driver.swipe(x,1600,x,800)
    time.sleep(5)
    # click nrc drop down
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'trailingIcon').click()
    time.sleep(3)
    wait=WebDriverWait(driver,20)
    # number
    number_scroll=wait.until(presence_of_element_located((AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[1]/android.view.View[1]')))
    number_rect=number_scroll.rect

    #{'height': 366, 'width': 163, 'x': 53, 'y': 1031}
    print(number_rect)
    scroll_nrc(number_rect,4)

    #nrc
    time.sleep(5)
    nrc_scroll=wait.until(presence_of_element_located((AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[1]/android.view.View[2]/android.view.View')))
    nrc_rect=nrc_scroll.rect
    scroll_nrc1(nrc_rect,12)

    #Char
    time.sleep(5)
    city_scroll=wait.until(presence_of_element_located((AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[1]/android.view.View[3]')))
    city_rect=city_scroll.rect
    #scroll_nrc1(city_rect,3)

    # nrc no
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').send_keys('034194')

    time.sleep(3)
    # done
    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View[2]').click()
    time.sleep(3)

    # continue
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Continue"]').click()

    time.sleep(5)

    # phone number
    phone='09300200400'
    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.widget.EditText[1]').send_keys(phone)

    time.sleep(2)
    # email
    email="aia@yopmail.com"
    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.widget.EditText[2]').send_keys(email)
    time.sleep(2)
    # password
    password="Abc123"
    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View/android.widget.EditText[1]').send_keys(password)
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View/android.widget.EditText[2]').send_keys(password)

    # continue
    #driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Continue"]').click()
# top to bottom
def scroll_nrc(rect,max_scroll):
    # 9 - bottom
    for _ in range(max_scroll):
        start_x=rect['x']+rect['width']//2
        print('Start X',start_x)
        start_y=rect['y']+rect['height']*0.8
        end_x=start_x
        end_y=rect['y']+rect['height']*0.2
        driver.swipe(start_x, start_y, end_x, end_y,100)
        time.sleep(2)

# bottom to top
def scroll_nrc1(rect,max_scroll):
    # 9 - bottom
    for _ in range(max_scroll):
        start_x=rect['x']+rect['width']//2
        print('Start X',start_x)
        start_y=rect['y']+rect['height']*0.2
        end_x=start_x
        end_y=rect['y']+rect['height']*0.8
        driver.swipe(start_x=start_x, start_y=end_y, end_x=end_x, end_y=start_y,duration=100)
        time.sleep(2)

#"nrc": "12/AHLANA(N)000002"
# "nrc": "12/AHLANA(N)000001"
# "nrc": "13/KaLaTa(N)034194"


def click_by_xpath(xpath):
    driver.find_element(AppiumBy.XPATH,xpath).click()

def click_by_id(idd):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,idd).click()
def scroll_element(text):
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
    )
def send_keys_by_xpath(xpath,value):
    driver.find_element(AppiumBy.XPATH,xpath).send_keys(value)








def main():
    # uninstall_app()
    # time.sleep(10)
    # install_app()
    # time.sleep(10)
    # open_app()
    time.sleep(5)
    # change_language()
    # loginFirstTime()
    # loginSecondTime()
    # logout()
    #register()
    #create_account()
    #PolicyRequests()
    #create_a_new_beneficiary()
    # add_second_new_beneficiary()
    

main()











# # pop up edit
# driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button').click()
# time.sleep(5)
# print('dop popup open')
#
# # date_edit_text=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
# # date_edit_text.click()
# time.sleep(10)
# driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').send_keys('04/11/1998')
# time.sleep(5)
# driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button').click()






#aia-plus-uat-release-2025-01-08.apk
