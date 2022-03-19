# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 17:38
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 文件上传脚本.py
# @Software : PyCharm

# 文件上传 的学习
''''''
'''
学习目标:
    文件上传通过定位到上传的按钮,直接把文件的路径传入.
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.find_element_by_class_name('soutu-btn').click()  # 先点击照相机

driver.find_element_by_class_name('upload-pic').send_keys(r'C:\Users\Administrator\Desktop\777.png')
sleep(5)
driver.quit()