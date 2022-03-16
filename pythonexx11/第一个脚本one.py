# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 11:46
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 第一个脚本one.py
# @Software : PyCharm
'''
# 学习目标:

'''



'''
1.掌握浏览器打开的方式
2. 掌握浏览器常用的操作方法:
    所有的方法都是用driver来操作
    1) get() 用来打开被测网址
    2) maximize_window()    把窗口最大化
    3 )
'''

# 1 . 导入webdriver
from selenium import webdriver
from time import sleep  # time 标准库,sleep 是一个函数,用来实现脚本等待.
#2. 实例化一个谷歌浏览器对象,用来获取一个空白页面的谷歌浏览器
driver = webdriver.Chrome()
# 3.使用get 方法打开被测网址
driver.get("http://www.baidu.com")
driver.maximize_window()    # 将窗口最大化
sleep(3)
driver.set_window_size(600,800)  # 将窗口设置成600x800大小
driver.get('http://www.4399.com')
sleep(1)
driver.back()  # 回退页面
sleep(1)
driver.forward()  # 前进页面
sleep(1)
driver.refresh()  # 页面刷新


sleep(2)
# driver.quit() #关闭浏览器
driver.close()#脚本写完关闭窗口


