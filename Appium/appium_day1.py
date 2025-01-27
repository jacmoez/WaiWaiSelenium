"""
source venv/bin/activate (For Mac Activate)
pip install appium
pip install Appium-Python-Client

"""
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


options = UiAutomator2Options()
options.set_capability("ignoreHiddenApiPolicyError", True)
URL = "http://127.0.0.1:4723"

driver = webdriver.Remote(URL, options=options)

package_name = 'com.aiamm.plus.uat'

def uninstall_app():

    if driver.is_app_installed(package_name):
        driver.remove_app(package_name)
        print("Uninstall Success")
    else:
        print("No app is install")
    print("-------------uninstall-----------")


def install_app():
        try:
            driver.install_app("C:/Users/DELL/Downloads/aia-plus-uat-release-2025-01-08.apk")
            time.sleep(5)
        except Exception as e:
            print("Could not install error")
        print("App is install: ", driver.is_app_installed(package_name))
        print("-------------------install---------------------")


uninstall_app()
time.sleep(5)
install_app()
