# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 17:21
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 弹出框 学习.py
# @Software : PyCharm
#
#
''''''
'''
学习目标:
    1. alter弹出框,这种弹出框不能通过元素定位的方式操作.
        使用driver.switch_to.alert切换到弹出框
        accept() 点击确认
        dismiss() 点击取消
        send_key() 输入内容.
        text        获取弹出框的文本
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///H:/a%E6%B1%87%E6%99%BA%E8%AF%BE%E4%BB%B6/python/SeleniumPPT/PPT/pages/pages/al.html")

driver.find_element_by_id('b2').click()   # 先点击元素,使弹出框出现.

# 1.切换到弹出框
al = driver.switch_to.alert
al.accept() # 点击确定.

driver.find_element_by_id('b2').click()   # 先点击元素,使弹出框出现.
al.dismiss()    # 点击取消.

driver.find_element_by_id('b3').click()
al.send_keys('哈哈哈') # 往弹出框输入内容
print(al.text)          # 获取弹出框的文本
al.accept()     # 点击确定.
sleep(5)
driver.quit()