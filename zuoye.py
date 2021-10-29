from unittest import TestCase
from selenium import webdriver
import time
class TesHKR(TestCase):

    def testLogin(self):
        #造数据
        username = "wzh"
        password = "981108"
        # expect = "Student Login"

        #执行用例
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR/")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//*[@id='img']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//*[@src='img/picture/dog.jpg']").click()
        time.sleep(2)
        # #获取实际结果
        # result = driver.title
        # self.assertEqual(result,expect)
