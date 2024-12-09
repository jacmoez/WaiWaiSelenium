from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select




class TestYoGa:

    driver = webdriver.Firefox()

    def test_open_browser(self):
        self.driver.get("https://www.yogamovement.com/")
        print("Test 1 : Open browser success!")

    def test_register_test(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a").click()

        user_email = "phy12@yopmail.com"
        self.driver.find_element(By.NAME, "email").send_keys(user_email)
        self.driver.find_element(By.NAME, "password").send_keys("Phy123", Keys.RETURN)
        time.sleep(3)
        self.driver.find_element(By.NAME, "firstname").send_keys("Kaung")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input").send_keys("Kaung")
        time.sleep(2)

        email = self.driver.find_element(By.NAME,"email")
        val = email.get_attribute("value")
        if val == user_email : print("Email Match")
        else : print("Not Email Match")

        #I Identify as
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/div/div").click()

        time.sleep(3)
        #Country

        self.driver.find_element(By.CLASS_NAME, "css-egispl").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//img[@src='https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-hk.png']" ).click()
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



        #Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]")).select_by_value("1998")

        time.sleep(2)
        Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]")).select_by_value("10")

        #Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]")).select_by_value("10")

        time.sleep(2)
        #self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[4]").click()

        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[4]").click()

      #Referral
        #time.sleep(2)
        #self.driver.find_element(By.NAME, "referral").send_keys(("X96695X2"))

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[6]/div/button").click()
        time.sleep(2)
        text= self.driver.find_element(By.CSS_SELECTOR, ".terms__title.text-uppercase").text
        time.sleep(2)
        self.driver.find_element(By.NAME, "name").send_keys(Keys.RETURN)
        time.sleep(2)
        err_name = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[1]/label[1]/div[2]").text
        print(err_name)

        time.sleep(2)
        err_mobile = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[1]/label[2]/div[2]").text
        print(err_mobile)
        time.sleep(2)
        self.driver.find_element(By.NAME, "name").send_keys("QA Wai Wai")
        time.sleep(2)
        self.driver.find_element(By.NAME, "mobile").send_keys("959796686061")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[2]/div/label/div/div").click()
        print(text)
        #btn Click
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/button").click()
        print("Go to next page successfully")





    def test_main(self):
        self.test_open_browser()
        self.test_register_test()
        time.sleep(10)

TestYoGa().test_main()