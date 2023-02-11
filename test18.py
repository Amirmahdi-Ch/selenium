import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


class ract(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:3000/calculator")
    
    def test_add(self):
        driver = self.driver
        x = 5
        y = 3
        sum = x + y
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[4]/div[3]/button').click()
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[4]/div[4]/button').click()
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[3]/div[2]/button').click()
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[5]/div[3]/button').click()
        elem = driver.find_element("xpath",'//*[@id="root"]/div/div[1]/div')
        self.assertEqual(int(elem.text),sum,"plus test failed")
        print("*********************************")
        print("plus test passed")
        print("*********************************")
        
    def test_minus(self):
        driver = self.driver
        x = 6
        y = 4
        minus = x - y
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[3]/div[3]/button').click()
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[3]/div[4]/button').click()
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[3]/div[1]/button').click()
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[5]/div[3]/button').click()
        elem = driver.find_element("xpath",'//*[@id="root"]/div/div[1]/div')
        self.assertEqual(int(elem.text),minus,"minus test failed")
        print("*********************************")
        print("minus test passed")
        print("*********************************")
    
    def test_multiple(self):
        driver = self.driver
        x = 2
        y = 1
        minus = x * y
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[4]/div[2]/button').click()
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[2]/div[4]/button').click()
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[4]/div[1]/button').click()
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[5]/div[3]/button').click()
        elem = driver.find_element("xpath",'//*[@id="root"]/div/div[1]/div')
        self.assertEqual(int(elem.text),minus,"multiple test failed")
        print("*********************************")
        print("multiple test passed")
        print("*********************************")
    
    def test_divide(self):
        driver = self.driver
        x = 6
        y = 4
        minus = x / y
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[3]/div[3]/button').click()
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[1]/div[4]/button').click()
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[3]/div[1]/button').click()
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[5]/div[3]/button').click()
        elem = driver.find_element("xpath",'//*[@id="root"]/div/div[1]/div')
        self.assertEqual(float(elem.text),minus,"divide test failed")
        print("*********************************")
        print("divide test passed")
        print("*********************************")
        
        
    
    def tearDown(self) -> None:
         self.driver.close()
        
if __name__ == '__main__':
	unittest.main()

        