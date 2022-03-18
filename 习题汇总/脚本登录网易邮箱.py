# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 15:32
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 脚本登录网易邮箱.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://email.163.com/")
sleep(2)

biaodan = driver.find_element_by_css_selector('#urs163Area>iframe') # x先定位到这个表单
driver.switch_to.frame(biaodan) # 再进行切换

driver.find_element_by_css_selector('#account-box input').send_keys('liangguiyu0807')
# driver.find_element_by_css_selector('#form input[data-placeholder="邮箱帐号或手机号码"][style="width: 206px;"]').click()
# driver.find_element_by_css_selector('#form input[data-placeholder="邮箱帐号或手机号码"][style="width: 206px;"]').send_keys('liangguiyu0807')
driver.find_element_by_name('password').send_keys('LGYlgy123..')   # class_name  与 by_name  的区别是,其 class 后面有属性值的就用
driver.find_element_by_id('dologin').click()   # 点击登录
sleep(3)
result = driver.find_element_by_id('')
if "liangguiyu0807" in result:
    print('ok')
else:
    print('faild')

sleep(4)
driver.quit()