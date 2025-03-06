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
from dotenv import  load_dotenv
import os
from helper import  *

load_dotenv()
from VarPath import  *

package_name=os.getenv('package_name')

# uninstall if exist
def uninstall_app():
    print('Uninstall')
    if driver.is_app_installed(package_name):
        driver.remove_app(package_name)
        print("After uninstalled")
    else:
        print('No app is installed')
    print('----- uninstall ----')

# u , i , o

# install app
def install_app():
    print('Install')
    try:
        driver.install_app(os.getenv('app_path'))
        time.sleep(5)
    except Exception as e :
        print("Could not install error")
    print('------------- install --------')


def open_app():
    print('Launch')
    # driver.launch_app()
    time.sleep(2)
    driver.activate_app(package_name)
    time.sleep(3)
    print('------------- App is opened -------------')

# change language
def change_language():
    # click language drop down
    click_by_xpath(change_language_path['language_dd_xpath'])
    time.sleep(3)
    # Burmese
    click_by_xpath(change_language_path['burmese_lan_xpath'])
    time.sleep(3)
    # Done button
    click_by_xpath(change_language_path['done_btn_xpath'])
    time.sleep(5)
    # English
    # click language drop down again
    click_by_xpath(change_language_path['language_dd_xpath'])
    # eng language option
    click_by_xpath(change_language_path['eng_lan_xpath'])
    # click done button again
    click_by_xpath(change_language_path['done_btn_xpath'])
    time.sleep(3)
    print('------------- Change language -------------')


def login_with_error():
    time.sleep(5)
    # login button
    click_by_xpath(login_path['login_btn_path_1'])
    time.sleep(5)
    # mobile or email
    email="qa@gmail.com"
    # add invalid email
    send_keys_by_xpath(login_path['email_or_mobile_path'],email)
    time.sleep(5)

    # password
    # add invalid password
    password="aq123"
    send_keys_by_xpath(login_path['password_path'],password)
    time.sleep(10)

    click_by_accessibility_id(login_path['switch_id'])
    time.sleep(5)

    # login button
    click_by_xpath(login_path['login_btn_path_2'])
    time.sleep(5)

    # print login error message
    err_msg_el=get_text_by_xpath(login_path['err_msg_path'])
    print("Error Message : ",err_msg_el)
    print('------------- login ----------------')


def login_first_time():
    time.sleep(5)
    # login button
    click_by_xpath(login_path['login_btn_path_1'])
    time.sleep(5)

    # mobile or email
    phone="09764426445"
    send_keys_by_xpath(login_path['email_or_mobile_path'],phone)
    time.sleep(5)

    # password
    password="P@ssw0rd2026@"
    send_keys_by_xpath(login_path['password_path'],password)
    time.sleep(10)

    # switch
    click_by_accessibility_id(login_path['switch_id'])
    time.sleep(5)

    # login button
    click_by_xpath(login_path['login_btn_path_2'])
    time.sleep(5)


    print('------------- login ----------------')

def logout():
    time.sleep(3)
    # settings
    click_by_accessibility_id(logout_path['setting_path'])
    # logout
    click_by_xpath(logout_path['logout_btn_path'])
    # popup ok
    click_by_xpath(logout_path['ok_btn_path'])


def login_second_time():
    # login button - first page
    click_by_xpath(login_path['login_btn_path_1'])
    time.sleep(4)
    # password
    password="P@ssw0rd2026@"
    send_keys_by_xpath(login_path['second_time_password'],password)
    time.sleep(10)
    # login button
    click_by_xpath(login_path['login_btn_path_2'])
    # driver.find_element(AppiumBy.XPATH,'//v1.m1/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]').click()
    time.sleep(3)


def policy_requests():
    # time.sleep(20)
    wait=WebDriverWait(driver,20)
    #PolicyRequests
    click_by_accessibility_id(policy_requests_path['policy_requests_path'])
    time.sleep(5)

    # member information change
    click_by_xpath(policy_requests_path['member_information_change_path'])
    time.sleep(5)

    # beneficiary information
    click_by_xpath(policy_requests_path['beneficiary_information_path'])
    time.sleep(5)

    # choose a policy
    click_by_xpath(policy_requests_path['choose_a_policy_path'])
    # continue
    click_by_xpath(policy_requests_path['continue_path'])






# env
# helper - actions
# path

