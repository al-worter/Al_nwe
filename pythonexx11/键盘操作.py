# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 16:21
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 键盘操作.py
# @Software : PyCharm

''''''
'''
学习目标:
    1．操作键盘需要先导入ActionChains类,并且使用send_keys方法
    from selenium. webdriver. commnon. action_chains import ActionChains
    send_keys(Keys.BACK_SPACE) 删除键(BackSpace)
    send_keys (Keys.SPACE) 空格键(Space)
    send_keys (Keys.TAB) 制表键(Tab)
    send_keys(Keys.ESCAPE) 回退键(Esc)
    send_keys(Key4 ENTER) 回车键（Enter)
    send_keys(Keys.CONTROL, 'a')全选(Ctr1+A)
    send_keys(Keys.CONTROL,'c'）复制(Ctr11C)
    send keys(Keys.CONTROL, 'x')剪切(Ctr1+X)
    send_keys(Keys.CONTROL,'v)粘贴(Ctrl+V)

'''

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
ele = driver.find_element_by_id('kw')  # 在百度首页输入框
sleep(1)
# ele.send_keys('12345')
# ele.send_keys(Keys.BACK_SPACE)  # 删除写法
# ele.send_Keys(Keys.SPACE)  # 空格

ele.send_keys('123456')
ele.send_keys(Keys.BACK_SPACE)  # 删除
ele.send_keys(Keys.SPACE)