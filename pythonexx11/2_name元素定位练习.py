# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 15:45
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 2_元素定位方式练习.py
# @Software : PyCharm
'''
学习目标:
1. id是元素的唯一身份标识,在元素id的情况下,优先使用id进行定位.
2 .掌握常用方法 :
    1) send_keys() 对元素进行输入
    2  click()    点击
    3) driver.title  获取页面标题
    4) driver.current_url  获取页面的url地址
    5) get_attribute() 获取元素的其他属性的值, 通过元素调用方法
    6) text 获取元素的文本,通过元素调用方法
    7)  _clear() 即把元素里面的内容清空
'''

from selenium import webdriver
from time import sleep  # time 标准库,sleep 是一个函数,用来实现脚本等待.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///D:/python1/%E5%91%A8%E5%A7%90%E8%AF%BE%E7%A8%8B/pages/s1.html')

# driver.find_element_by_name('button').click() ##如果页面上存在多个同名的元素,默认是找第一个，

# 如果想要点击第二个按钮
eles = driver.find_elements_by_name('button') #找出页面上所有name=button的元素
# print(eles)  # find_elements 会以列表的形式返回出页面所有满足的元素
# for i in eles:   # 遍历这个装着所有name = button 的元素
#     if i.text == "按钮2":  # 判断如果当前遍历到的元素是文本 按钮2
#         i.click()  # 就点击



