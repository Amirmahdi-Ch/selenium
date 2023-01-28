from curses import tigetflag
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
        self.counter = 0;
    
    def test_add(self):
        driver = self.driver
        driver.get("http://localhost:3000/counter-app")
        driver.find_element("xpath", '//*[@id="root"]/div/main/div/div/div[2]/div/div[2]/button[1]').click()
        self.counter+=1
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/nav/div/span')
        self.assertEqual(int(elem.text),self.counter,"frist plus icon is broken")
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/div/div[2]/div/div[1]/span')
        self.assertEqual(int(elem.text),self.counter,"frist plus icon is broken")
        time.sleep(2)
        driver.find_element("xpath", '//*[@id="root"]/div/main/div/div/div[3]/div/div[2]/button[1]').click()
        self.counter+=1
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/nav/div/span')
        self.assertEqual(int(elem.text),self.counter,"second plus icon is broken")
        driver.find_element("xpath", '//*[@id="root"]/div/main/div/div/div[4]/div/div[2]/button[1]').click()
        self.counter+=1
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/nav/div/span')
        self.assertEqual(int(elem.text),self.counter,"third plus icon is broken")
        driver.find_element("xpath", '//*[@id="root"]/div/main/div/div/div[5]/div/div[2]/button[1]').click()
        self.counter+=1
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/nav/div/span')
        self.assertEqual(int(elem.text),self.counter,"fourth plus icon is broken")
        print("plus icon test passed!\n\n")
        time.sleep(5)
        
        
        
        
        driver.find_element("xpath", '//*[@id="root"]/div/main/div/div/div[2]/div/div[2]/button[2]').click()
        self.counter-=1
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/nav/div/span')
        self.assertEqual(int(elem.text),self.counter,"frist minus icon is broken")
        time.sleep(2)
        print("minus icon test passed!\n\n")
        time.sleep(5)
        
        driver.find_element("xpath", '//*[@id="root"]/div/main/div/div/div[5]/div/div[2]/button[3]').click()
        self.counter-=1
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/nav/div/span')
        self.assertEqual(int(elem.text),self.counter,"frist minus icon is broken")
        time.sleep(2)
        print("remove icon test passed!\n\n")
        time.sleep(5)
        
        
        driver.find_element("xpath", '//*[@id="root"]/div/main/div/div/div[1]/div/button[1]').click()
        self.counter = 0
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/nav/div/span')
        self.assertEqual(int(elem.text),self.counter,"frist minus icon is broken")
        elem = driver.find_element("xpath",'//*[@id="root"]/div/main/div/div/div[3]/div/div[1]/span')
        self.assertEqual(elem.text,"Zero")
        time.sleep(2)
        print("reset icon test passed!\n\n")
        time.sleep(5)
        
        
    
    def tearDown(self) -> None:
         self.driver.close()
        
if __name__ == '__main__':
	unittest.main()

        