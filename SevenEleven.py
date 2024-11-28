from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tabulate import tabulate

driver = webdriver.Firefox()
driver.maximize_window()
def browser_open():
    driver.get("https://staging.d3hi9g2bzkelg7.amplifyapp.com/")
    print('Test : Browser Open Success')

def product_menu_link():
    time.sleep(10)
    product_link_xpath="/html/body/div[1]/header/div/div[2]/div[1]/li[1]/a/div/h5"
    driver.find_element(By.XPATH,product_link_xpath).click()
    print('Test : Product Menu Link Click Success')

def product_menu_item():
    time.sleep(10)
    span_xpath = "//span[text()='7-Select Ready-to-Eat']"
    span_element = driver.find_element(By.XPATH, span_xpath)
    actions = ActionChains(driver)
    actions.move_to_element(span_element).perform()
    # print("Hovered over the span element.")
    time.sleep(2)
    dynamic_div_xpath = "//div[contains(@class, 'absolute hidden h-[50px]')]"
    dynamic_div = driver.find_element(By.XPATH, dynamic_div_xpath)
    dynamic_div.click()
    print('Test : Product Item Link Click Success')


def learn_more_button_click():
    button_xpath = "//button[contains(@class, 'rounded-[40px]') and text()='Learn more']"
    learn_more_btn = driver.find_element(By.XPATH, button_xpath)
    learn_more_btn.click()
    print("Test : Learn More Button clicked successfully.")


def print_item_information():
    table = driver.find_element(By.XPATH, "//table")
    rows = table.find_elements(By.XPATH, ".//tr")
    table_data = []
    for row in rows:
        cells = row.find_elements(By.XPATH, ".//th | .//td")
        row_data = [cell.text.strip() for cell in cells]
        table_data.append(row_data)
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
    print('Test : Print Item Information Success')

def back_to_product_list():
    back_to_products_xpath = (
        "//button[contains(@class, 'rounded-[40px]') and contains(., 'Back To Products')]"
    )
    back_to_products_button = driver.find_element(By.XPATH, back_to_products_xpath)
    back_to_products_button.click()
    print("Test: 'Back To Products' button clicked successfully.")

def main():
    browser_open()
    product_menu_link()
    product_menu_item()
    time.sleep(30)
    learn_more_button_click()
    time.sleep(20)
    print_item_information()
    time.sleep(10)
    back_to_product_list()



main()


# pip3 install tabulate




