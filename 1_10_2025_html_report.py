
from typing import  Dict
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import  datetime
class ReportGenerator:
    def __init__(self,report_title="Automation Test",outuput_file="report.html"):
        self.report_title=report_title
        self.output_file=outuput_file
        self.test_results:Dict[str,Any]={"passed":0,"failed":0,"total":0,"tests":[]}
        self.start_time:float=0

    def start_timer(self):
        self.start_time=time.time()

    def generate_report(self):
        end_time=time.time()
        duration=end_time - self.start_time
        total_tests=self.test_results["total"]
        passed_tests=self.test_results["passed"]
        failed_tests=self.test_results['failed']

        pass_percentage=(passed_tests/total_tests)*100 if total_tests>0 else 0
        fail_percentage=(failed_tests/total_tests)*100 if total_tests>0 else 0

        progress_bar_width=f"{pass_percentage:.2f}"

        html=f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <title>{self.report_title}</title>
                <style>
                body{{font-family: Cambria;}}
                .container{{
                    width: 80%;
                margin: auto;
                }}
                .summary{{
                    display: flex;
                justify-content: space-around;
                margin-bottom: 20px;
                }}
                .progress{{
                    width: 100%;
                height: 15px;
                background-color: #eee;
                border-radius: 5px;
                margin-bottom: 20px;
                }}
                .progress-bar{{
                    height: 100%; background-color:green ;width:{progress_bar_width}%;border-radius: 5px;
                }}
                .test-list{{
                    border-collapse: collapse;
                width: 100%;
                }}
                .test-list th,.test-list td{{
                    border:1px solid #ddd;padding: 8px ;text-align: left;vertical-align: top;
                }}
                .passed{{
                    color: green;
                }}
                .failed{{
                    color:red
                }}
                </style>
                </head>
                <body>
                <div class="container">
                <h1>progress_bar_width {progress_bar_width}</h1>
                <p>Generated on :{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p>Total Duration :{duration:.2f}</p>
                <div class="summary">
                <div>Total Tests : {total_tests}</div>
                <div class="passed">Passed : {passed_tests} (<span class="percentage">{pass_percentage:.2f}</span>)</div>
                <div class="failed">Failed : {failed_tests}(<span class="percentage">{fail_percentage:.2f} </span>)</div>
                </div>
                
                <div class="progress">
                <div class="progress-bar"></div>
                </div>
                
                <h2>Test Results</h2>
                <table class="test-list">
                <tr>
                <th>Test Name</th>
                <th>Status</th>
                <th>Error</th>
                </tr>"""
        for test in self.test_results["tests"]:
            html+=f'''<tr>
            <td>{test['name']}</td>
            <td class={test['status']}>{test['status']}</td>
            <td class="error-message">{test.get("error",'')}</td>
            </tr>'''
        html+='''</table>
            </div>
            </body>
            </html>'''

        with open(self.output_file,'w',encoding='utf-8') as f:
            f.write(html)
        print(f'Report generated :{self.output_file}')

    def add_test_result(self,name,status,error=None):
        self.test_results["total"]+=1
        if status=="passed":
            self.test_results["passed"]+=1
        if status=="failed":
            self.test_results["failed"]+=1
        self.test_results["tests"].append({"name":name,"status":status,"error":str(error) if error else ""})

class SwagTest:
    def __init__(self,report_generator:ReportGenerator):
        self.driver = webdriver.Firefox()
        self.report_generator=report_generator

    def open_browser(self):
        try:
            self.driver.get("https://www.saucedemo.com/")
            print("Test 1 : Open browser success!")

            assert  "Swag Labs" in self.driver.title , f'Expected title is Swag Labs, but got {self.driver.title}  '
            self.report_generator.add_test_result("Test 1","passed")
        except AssertionError as e:
            self.report_generator.add_test_result("Test 1","failed",str(e))
        except Exception as e:
            self.report_generator.add_test_result("Test 1","failed",str(e))


    def login_test(self):
        try:
            self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce", Keys.RETURN)
            assert  "Swag Labssss" in self.driver.title , f'Expected title is Swag Labsss, but got {self.driver.title}  '
            self.report_generator.add_test_result("Test 2","passed")
            print("Test 2 : Login Success!")
        except AssertionError as e:
            self.report_generator.add_test_result("Test 1","failed",str(e))
        except Exception as e:
            self.report_generator.add_test_result("Test 1","failed",str(e))

    def check_page_go(self):
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.driver.current_url

        assert expected_url == actual_url
        assert "Swag Labs" in self.driver.title
        print("Test 3 : Verification Success!")

    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        print("Test 4 : Add item to Cart")

    def remove_item(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
        print("Test 5 : Remove 1 item")

    def view_order_items(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("Test 6 : View Order Item")

    def check_cart_page_go(self):
        expected_url = "https://www.saucedemo.com/cart.html"
        actual_url = self.driver.current_url

        assert expected_url == actual_url
        assert "Swag Labs" in self.driver.title
        print("Test 7 : check cart page success")

    def view_cart_ditail(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").click()

        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div").click()

        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("Test 8 : view cart ditail Success!")

    def check_out(self):
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("QA")
        time.sleep(2)
        self.driver.find_element(By.ID, "last-name").send_keys("Wai Wai")
        time.sleep(2)
        self.driver.find_element(By.ID, "postal-code").send_keys("11111")
        time.sleep(2)
        self.driver.find_element(By.ID, "continue").click()
        print("Test 9 : Check Out Success!")

    def check_checkout(self):
        item_total = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        tax = self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        print(f"{item_total}.")
        print(f"{tax}.")
        print(f"{total}")
        print("="*30)

    def finish(self):
        self.driver.find_element(By.ID, "finish").click()
        complete = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        print(complete)
        self.driver.find_element(By.ID, "back-to-products").click()
        print('Test 10 : Finish Success')
        print("="*50)

    def main(self):
        self.report_generator.start_timer()
        self.open_browser()
        self.login_test()
        # self.check_page_go()
        # self.add_to_cart()
        # self.remove_item()
        # self.view_order_items()
        # self.check_cart_page_go()
        # self.view_cart_ditail()
        # self.check_out()
        # self.check_checkout()
        # self.finish()
        self.report_generator.generate_report()


SwagTest(ReportGenerator(report_title="Report By Wai Wai")).main()





