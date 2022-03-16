# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 16:03
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3_元素定位练习.py
# @Software : PyCharm

'''
学习目标:
    1. classname 就是元素的class 属性的值, 如果在定位的时候发现有多个class的值,只取其中一个进行定位, 搜索看是否唯一,尽量取最少的.

'''

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_class_name('s_ipt').send_keys(123)   # send_keys('')是给该输入框输入内容
# driver.find_element_by_class_name('s_btn').click() # r如果在定位的时候发现这个元素有多个classz值,只取其中一个进行定位.

# 练习:
driver.get('file:///D:/python1/%E5%91%A8%E5%A7%90%E8%AF%BE%E7%A8%8B/pages/s1.html')
eles = driver.find_elements_by_class_name('cheese')  # 通过赋值变量,遍历找到定位该文本的 元素
for i in eles:
    if i.text == 'Gouda':
        print('找到了')

sleep(5)
driver.quit()
