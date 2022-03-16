# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 16:52
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 4_tagname元素定位练习.py
# @Software : PyCharm

'''
学习目标:

'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

# eles = driver.find.elements_by_tag_name('a')  # 找出页面上所有的a标签, 该方式效率比较低,.同时找出的a标签元素会很多.父标签以外的也会搜出来

# 1.先找出目标a标签的父标签
father = driver.find_element_by_id('s-top-left')  # 该id是在网页上DIV这个模块的这个ID定位属性
# 2. 再找出这个父标签下面所有的a标签.
eles = father.find_elements_by_tag_name('a')
print(eles)
for i in eles:
    if i.text == '视频':  # 如果当前元素的 文本 是地图
        i.click()  # 就点击
        break  # 循环找到之后就停止该循环遍历
sleep(5)
driver.quit()