from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRenovation:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def test_open_browser(self):
        self.driver.get("https://web-staging.renonation.sg/")

    def test_login(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input").send_keys("311")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button").click()
        invalid = self.driver.find_element(By.CSS_SELECTOR, ".flex-1.text-sm.text-error").text
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input").send_keys("83115546")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "otp").send_keys("232323")
        otp_btn = "/html/body/div/div/div[3]/div/div/form[2]/div/div/button"

        self.driver.find_element(By.XPATH,otp_btn ).click()

        print(invalid)
        print("Test 2: Login Success!")


    def test_main(self):
        self.test_open_browser()
        self.test_login()


TestRenovation().test_main()