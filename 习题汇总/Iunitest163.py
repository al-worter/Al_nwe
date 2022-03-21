# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 17:39
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 使用unitest 框架163邮箱.py
# @Software : PyCharm
''''''
#
'''
 学习要义:
    1.
    2.
    
'''
import unittest
from time import sleep
from selenium import webdriver


class TestMai163(unittest.TestCase):
    def setUp(self):  # 由于参数是局部的话,需要调用其他函数可就得 用self 实例化
        self.driver = webdriver.Chrome()  # 实例化浏览器对象,
        self.driver.get('http://www.mail.163.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def tearlogin(self):
        hailey = self.driver.find_element_by_css_selector('#loginDiv>iframe')  # 先找到表单
        self.driver.switch_to.frame(hailey)  # 然后进行表单切换到该表单
        self.driver.find_element_by_name('email').send_keys('liangguiyu0807')
        self.driver.find_element_by_name('password').send_keys('LGYlgy123..')
        self.driver.find_element_by_id('dologin').click()  # 点击登录
        sleep(3)
        result = self.driver.find_element_by_id('spnUid').text  # 获取登录成功后的文本
        self.assertIn('liangguiyu0807', result)


if __name__ == '__main__':
    unittest.main()
