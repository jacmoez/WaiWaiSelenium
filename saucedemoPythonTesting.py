from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce", Keys.RETURN)
time.sleep(2)
#time.sleep(2)
#driver.find_element(By.ID, "react-burger-menu-btn").click()
#time.sleep(2)
#driver.find_element(By.ID, "logout_sidebar_link").click()

# Verify login status
expected_url = "https://www.saucedemo.com/inventory.html"
actual_url = driver.current_url

assert expected_url == actual_url
assert "Swag Labs" in driver.title
print("Login is Successful")


def add_cat():
    time.sleep(2)
    #Add to cart items
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(2)
    #Click shopping icon
    shopping_cart = driver.find_element(By.ID, "shopping_cart_container")
    shopping_cart.click()
    time.sleep(2)

    #Verify item in shopping cart

    item1 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").text
    item2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div").text

    print(item1)
    print(item2)

    #cart_badge = driver.find_element(By.CLASS_NAME, )
    print("Add to Cart items successful!")

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").click()

    shopping_cart = driver.find_element(By.ID, "shopping_cart_container")
    shopping_cart.click()

    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div").click()

    shopping_cart = driver.find_element(By.ID, "shopping_cart_container")
    shopping_cart.click()

    driver.find_element(By.ID, "checkout").click()


def check_out():
    driver.find_element(By.ID, "first-name").send_keys("QA")

    driver.find_element(By.ID, "last-name").send_keys("Wai Wai")

    driver.find_element(By.ID, "postal-code").send_keys("11111")

    driver.find_element(By.ID, "continue").click()

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(10)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(2)
    page_source = driver.page_source

    if "Sauce Labs Backpack" in page_source and "Sauce Labs Bolt T-Shirt" in page_source:
        print("Sauce Labs Backpack and Sauce Labs Bolt T-Shirt Ok")
    else:
        print("Text not found.")

    driver.find_element(By.ID, "finish").click()
    time.sleep(2)
    page_source = driver.page_source

    if "Thank you for your order!" in page_source:
        print("Sauce Labs Thank you for your order! Ok")
    else:
        print("Text not found.")

    driver.find_element(By.ID, "back-to-products").click()


add_cat()
check_out()
