from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

from test import driver


class TestYoGa:

    driver = webdriver.Firefox()

    def test_open_browser(self):
        self.driver.get("https://www.yogamovement.com/")
        print("Test 1 : Open browser success!")

    def test_register_test(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a").click()

        user_email = "phy112@yopmail.com"
        self.driver.find_element(By.NAME, "email").send_keys(user_email)
        self.driver.find_element(By.NAME, "password").send_keys("Phy123", Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.NAME, "firstname").send_keys("Kaung")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input").send_keys("Kaung")
        time.sleep(2)

        email = self.driver.find_element(By.NAME,"email")
        val = email.get_attribute("value")
        if val == user_email : print("Email Match")
        else : print("Not Email Match")

        #I Identify as
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/div/div").click()


        #Country
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[1]/input").send_keys("Myanmar")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]").click()

        #Mobile Number
        self.driver.find_element(By.NAME, "mobile").send_keys("9764426445")
        time.sleep(2)
        #DOB
        self.driver.find_element(By.ID, "dob").click()

        time.sleep(2)
        #Year
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]/option[74]").click()
        time.sleep(2)

        Select(self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]")).select_by_value("1998")
        time.sleep(2)

        #month
        Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]")).select_by_value("10")
        time.sleep(2)
        
        #day
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[4]").click()





    def test_main(self):
        self.test_open_browser()
        self.test_register_test()

TestYoGa().test_main()
