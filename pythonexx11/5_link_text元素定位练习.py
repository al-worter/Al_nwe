# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 17:06
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 5_link_text元素定位练习.py
# @Software : PyCharm


'''
学习目标:   1 . link_text通过超链接(a标签)的文本来进行定位.必须要完全匹配文本.
            2. partial_link_text(也只能够定位a标签,可以通过部分文本模糊匹配


'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

driver.find_element_by_link_text('图片').click()  # 直接通过a标签的文本来进行定位.
driver.find_element_by_partial_link_text('片').click()  # 意为指可以模糊匹配文本包含'片'的a 标签

sleep(5)
driver.quit()