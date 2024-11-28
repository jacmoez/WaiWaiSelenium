import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ParaBank:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def setup(self):
        self.driver.get("https://parabank.parasoft.com/parabank/admin.htm")
        print("Test: Open Page Success")


    def login(self):
        self.driver.find_element(By.NAME, "username").send_keys("AMS")
        self.driver.find_element(By.NAME, "password").send_keys("123456", Keys.ENTER)
        print(" Test 2 : Login Success!")

    def account_overview(self):
        time.sleep(5)
        print(1)
        acc_number = self.driver.find_element(By.LINK_TEXT, "15453").text
        time.sleep(2)
        print(2)
        acc_balance = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]").text
        time.sleep(2)
        print(3)
        acc_amount = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]").text
        time.sleep(2)
        print(4)
        total = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[3]/td[2]/b").text
        print(5)
        print("Account Number : ", acc_number)
        print("Account Balance : ", acc_balance)
        print("Account Amount : ", acc_amount)
        print("Account Total : ", total)
        time.sleep(5)
        print("Test 3 : Account Overview Success! ")



    def open_account(self):
        time.sleep(3)
        #17562m
        self.driver.find_element(By.LINK_TEXT, "Open New Account").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/form/select[1]").click()
        self.driver.find_element(By.CLASS_NAME, "button").click()
        print("Testing 4 : Open New Account Success!")


    def transfer(self):
        time.sleep(3)
        print("1")
        self.driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
        print("2")
        self.driver.find_element(By.NAME, "input").send_keys("10")
        time.sleep(2)
        print(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[1]/select[1]/option[1]").click()
        time.sleep(2)
        print(4)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[1]/select[2]/option[2]").click()
        time.sleep(2)
        print(5)
        self.driver.find_element(By.NAME, "button").click()
        print("Testing 5 : Transfer Success!")


    def main(self):
        self.setup()
        self.login()
        self.account_overview()
        #self.open_account()
        self.transfer()

ParaBank().main()