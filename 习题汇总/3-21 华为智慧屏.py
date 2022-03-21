# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 下午 10:22
# @Author   : liang yuyu
# @Site     : http://www.cdtest.cn/
# @File     : 3-21 华为智慧屏.py
# @Software : PyCharm
#
''''''
import unittest
from selenium import webdriver
from time import sleep

class TestMail63(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # 实例化浏览器对象,
        self.driver.maximize_window()
        self.driver.get('https://www.vmall.com/')
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def testlogin(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector('a[href="https://consumer.huawei.com/cn/"]').click()
        windowe = self.driver.window_handles
        self.driver.switch_to.window(windowe[-1])
        result = self.driver.find_element_by_link_text('智慧屏').text
        self.assertIn('智慧屏', result)


if __name__ == '__main__':
    unittest.main()
