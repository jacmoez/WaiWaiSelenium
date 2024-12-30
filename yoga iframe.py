from time import time_ns

from pyotp import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


class TestYoGa:

    driver = webdriver.Chrome()

    def test_open_browser(self):
        self.driver.get("https://webfront-uat.yogamovement.com/")
        self.driver.maximize_window()
        time.sleep(2)
        #close alert box
        self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/button").click()
        print("Test 1 : Open browser success!")

    def test_register_test(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a").click()

        #Ramdom Email

        user_email = [random.randint(0,9) for i in range(2)]
        num = "".join(str(x) for x in user_email)


        self.driver.find_element(By.NAME, "email").send_keys("waiwai", num, "@yopmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Phy123", Keys.RETURN)
        time.sleep(3)

        #First Name
        self.driver.find_element(By.NAME, "firstname").send_keys("QA")
        time.sleep(3)

        #Last Name
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input").send_keys("Wai Wai")
        time.sleep(2)

        #Email Check
        email = self.driver.find_element(By.NAME,"email")
        val = email.get_attribute("value")
        if val == user_email : print("Email Match")
        else : print("Not Email Match")

        #I Identify as
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/div/div").click()
        time.sleep(2)

        #Country
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[1]/div[2]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[1]/input").send_keys("Myanmar")
        time.sleep(2)

        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]").click()

        #Mobile Number
        phone_number = [random.randint(0,9) for i in range(9)]
        num = "".join(str(x) for x in phone_number)
        self.driver.find_element(By.NAME, "mobile").send_keys("9",num)
        time.sleep(2)

        #DOB
        self.driver.find_element(By.ID, "dob").click()
        time.sleep(2)

        #Year
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]/option[74]").click()
        time.sleep(2)

        Select(self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]")).select_by_value("1998")


        time.sleep(2)
        Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]")).select_by_value("10")

        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[4]").click()
        time.sleep(2)


        #Home Country
        self.driver.find_element(By.CLASS_NAME, "css-egispl").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//img[@src='https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-hk.png']" ).click()

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

        time.sleep(5)
        #btn Click
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/button").click()

        print("Go to next page successfully")


    def test_sing_in(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[2]/a").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "email").send_keys("waiwai60@yopmail.com")
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys("Phy123", Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/button").click()

    def test_buy_class_pack(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[2]/a[2]/div/button[1]").click()
        time.sleep(2)

        self.driver.find_element(By.LINK_TEXT, "ALL ACCESS").click()
        time.sleep(2)


        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[1]").click()


        # All Access btn Click
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[1]/div[4]/button").click()


        time.sleep(2)
        #Next Btn
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/form/button").click()
        print("Test 3:", "All Class Success")



    def test_summary(self):
        print(1)
        img_path = "/Users/user/Desktop/Screenshot 2024-11-27 at 14.49.38.png"

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/label/input").send_keys(img_path)
        print("Image Success!")


    def test_payment_method(self):
        time.sleep(2)
        #Change Button
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/button").click()
        time.sleep(3)

        js_code = """let element = document.querySelector("input[name='hidden']");
        element.disable = false;
        return element"""
        #Car Number
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure card number input frame']")

        self.driver.switch_to.frame(iframe)

        self.driver.execute_script(js_code)

        self.driver.find_element(By.NAME, "cardnumber").send_keys("4111111111111111")
        self.driver.switch_to.default_content()
        time.sleep(3)

        #exp-date

        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure expiration date input frame']")

        self.driver.switch_to.frame(iframe)

        self.driver.execute_script(js_code)

        self.driver.find_element(By.NAME, "exp-date").send_keys("12/26")
        self.driver.switch_to.default_content()

        #CVC
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure CVC input frame']")

        self.driver.switch_to.frame(iframe)

        self.driver.execute_script(js_code)

        self.driver.find_element(By.NAME, "cvc").send_keys("123")
        self.driver.switch_to.default_content()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/button").click()

        time.sleep(3)
        file_path = "waiwai.png"
        self.driver.save_screenshot(file_path)


        print("Payment Success")

    def test_main(self):
        self.test_open_browser()
        #self.test_register_test()
        self.test_sing_in()
        self.test_buy_class_pack()
        #self.test_summary()
        self.test_payment_method()
        time.sleep(10)

TestYoGa().test_main()

