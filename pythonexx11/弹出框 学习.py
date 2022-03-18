# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 17:21
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 弹出框 学习.py
# @Software : PyCharm
#
#
''''''
''''''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///D:/python1/%E5%91%A8%E5%A7%90%E8%AF%BE%E7%A8%8B/pages/al.html')
driver.find_element_by_id('b2').click()  # 先点击元素,使弹出框出现

# 1.切换到弹出框
al = driver.switch_to.alert
al.accept()

driver.find_element_by_id("b2").click()
al.dismiss() # 点击取消

driver.find_element_by_id('b3').click()
al.send_keys('哈哈哈')  # 往弹出框输入内容
print(al.text)  # 获取弹出框的文本
al.accept()  # 点击确定
sleep(3)
driver.quit()