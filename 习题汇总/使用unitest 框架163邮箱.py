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
from selenium import webdriver
from time import sleep

class TestMai163(unittest.TestCase):
    def setUp(self):  # 由于参数是局部的话,需要调用其他函数可就得 用self 实例化
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.mai.163.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def tearlogin(self):
        hailey = self.driver.find_element_by_css_selector('#loginDiv>iframe')  # 先找到表单
        self.driver.switch_to.frame(hailey)  # 然后进行表单切换到该表单
        self.driver.find_element_by_css_selector('#account-box input').send_keys('liangguiyu0807')  # 使用CSS的后代选择器，通过父找子,用空格表示,可以忽略中间的层级直接定位到需要的标签.在需要找到的标签后面最好加上一个属性.用来精确定位
        self.driver.find_element_by_name('password').send_keys('LGYlgy123..')  # class_name  与 by_name  的区别是,其 class 后面有属性值的就用
        self.driver.find_element_by_id('dologin').click()  # 点击登录
        sleep(3)
        result = self.driver.find_element_by_id('spnUid').text  # 获取登录成功后的文本
        self.assertIn('liangguiyu0807', result)

if __name__ == '__main__':
    unittest.main()
