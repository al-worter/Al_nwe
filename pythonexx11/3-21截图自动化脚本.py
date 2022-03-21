# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 14:17
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-21截图自动化脚本.py
# @Software : PyCharm
#
''''''
'''
 学习要义:
    1).当用例不通过时,可以对页面进行截图.
       get screenshot_as_fileo进行截图.

 
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
driver.implicitly_wait(5)
driver.find_element_by_id('kw').send_keys('python自动化')
driver.find_element_by_id('su').click()
if 'java' in driver.title:  # 判断当前页面的title 是否包含java
    print("ok")
else:
    print("faild")
    driver.get_screenshot_as_file('faild.png')  # 进行截图,并保存在当前路径
sleep(2)
driver.quit()
