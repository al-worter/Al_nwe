# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 16:21
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 键盘操作.py
# @Software : PyCharm

''''''
'''
学习目标:
    1. 操作键盘需要先导入Keys类,并且使用send_keys方法
       from selenium.webdriver.common.keys import Keys
       常用方法:
        send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
        send_keys(Keys.SPACE) 空格键(Space)
        send_keys(Keys.TAB) 制表键(Tab)
        send_keys(Keys.ESCAPE) 回退键（Esc）
        send_keys(Keys.ENTER) 回车键（Enter）
        send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
        send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
        send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
        send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）


'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
ele = driver.find_element_by_id('kw')   # 百度首页的输入框

ele.send_keys('12345')
ele.send_keys(Keys.BACK_SPACE)  # 删除
ele.send_keys(Keys.SPACE)  # 空格
sleep(5)
driver.quit()
