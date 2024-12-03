from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from selenium import  webdriver
import time


class PDFReport:

    def __init__(self):
        self.results = []

    def add_test_result(self,test,msg):
        self.results.append([test,msg])

    def save_pdf(self, file_name="WaiWai.pdf"):
        doc = SimpleDocTemplate(file_name, pagesize=A4)
        elements = []
        data = [["Test", "Result"]] + self.results
        table = Table(data)
        style = TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.brown)
        ])
        table.setStyle(style)
        elements.append(table)
        doc.build(elements)

pdf_report = PDFReport()

class TestSwagTst:


    driver = webdriver.Firefox()

    def test_open_browser(self):
        self.driver.get("https://www.saucedemo.com/")
        pdf_report.add_test_result("Test 1 :"," Open browser success!")

    def test_login_test(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce", Keys.RETURN)
        pdf_report.add_test_result("Test 2 :"," Login Success!")

    def test_check_page_go(self):
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.driver.current_url

        assert expected_url == actual_url
        assert "Swag Labs" in self.driver.title
        pdf_report.add_test_result("Test 3 :"," verify success")

    def test_add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        pdf_report.add_test_result("Test 4 :"," Add item to Cart")

    def test_remove_item(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
        pdf_report.add_test_result("Test 5 :"," Remove 1 item")

    def test_view_order_items(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        pdf_report.add_test_result("Test 6 :"," View Order Item")

    def test_check_cart_page_go(self):
        expected_url = "https://www.saucedemo.com/cart.html"
        actual_url = self.driver.current_url

        assert expected_url == actual_url
        assert "Swag Labs" in self.driver.title
        pdf_report.add_test_result("Test 7 :"," check cart page success")

    def test_view_cart_ditail(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").click()

        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div").click()

        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        pdf_report.add_test_result("Test 8 :"," view cart ditail Success!")

    def test_check_out(self):
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("QA")
        time.sleep(2)
        self.driver.find_element(By.ID, "last-name").send_keys("Wai Wai")
        time.sleep(2)
        self.driver.find_element(By.ID, "postal-code").send_keys("11111")
        time.sleep(2)
        self.driver.find_element(By.ID, "continue").click()
        pdf_report.add_test_result("Test 9 :"," Check Out Success!")

    def test_check_checkout(self):
        item_total = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        tax = self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        pdf_report.add_test_result(f"{item_total}.","")
        pdf_report.add_test_result(f"{tax}.","")
        pdf_report.add_test_result(f"{total}","")

    def test_finish(self):
        self.driver.find_element(By.ID, "finish").click()
        complete = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        pdf_report.add_test_result(complete,"")
        self.driver.find_element(By.NAME, "back-to-products").click()
        pdf_report.add_test_result('Test 10 :',' Finish Success')

    def test_main(self):
        pdf_report.save_pdf()