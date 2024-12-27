# https://testautomationpractice.blogspot.com/
import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  Select
driver=webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
# driver.find_element(By.CSS_SELECTOR,"input[id='name']").send_keys("Automation")
# driver.find_element(By.CSS_SELECTOR,"input[maxlength='15']").send_keys("QA")
name=driver.find_element(By.CSS_SELECTOR,'input[placeholder$="Name"]')
name.send_keys('QA')
time.sleep(2)
name.clear()
el=driver.find_elements(By.CSS_SELECTOR,'input[placeholder^="Enter"]')
# print(el)
# print(len(el))
user=["QA","qa@email.com","09334445555"]
for i in range(len(el)): #
    el[i].send_keys(user[i])
driver.find_element(By.ID,"textarea").send_keys("Yangon")
driver.find_element(By.CSS_SELECTOR,"input[value='female']").click()

form_checks=driver.find_elements(By.CLASS_NAME,'form-check-input')
print(len(form_checks))
for i in range(2,len(form_checks),2):
    form_checks[i].click()
time.sleep(3)
country=Select(driver.find_element(By.ID,"country"))
country.select_by_index(1)
color=Select(driver.find_element(By.ID,"colors"))
color.select_by_index(1)
color.select_by_index(2)

animal=Select(driver.find_element(By.ID,"animals"))
animal.select_by_index(2)
animal.select_by_index(3)

driver.find_element(By.ID,"datepicker").send_keys("12/26/2024")
driver.find_element(By.ID,"txtDate").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[4]/td[6]/a").click()

time.sleep(3)
# driver.find_element(By.ID,"start-date").click()
# dt=driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[8]/input[1]")
# driver.execute_script("arguments[0].scrollIntoView()",dt)
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Start Date"]').click()

# driver.find_element(By.XPATH,"//a[text()='28']").click()
time.sleep(5)
driver.quit()







