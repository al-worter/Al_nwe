# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 11:36
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 多窗口切换脚本实现.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
# 多窗口运行
'''
  可能出现的问题:
        1.1.程序运行得太快,需要进行元素等待，
        2有些输入框必须先点击,再输入.
        3．有些元素是动态元素.(每次刷新后的值都跟上一次不同.)
        4.要查找的元素在新窗口,需要切换
        5·要查找的元素嵌套在frame/iframe标签里.
        6.需要定位的元素在页面靠下的位置,需要操作滚动条.
        
'''

'''
学习目标:
    1.多窗口的切换是通过切换窗口的句柄来实现的.句柄是窗口的唯一身份标识
    切换方式:
        1. 获取所有窗口的句柄:driver.window_handles  通过索引 -1 来进行切换.
        2. 提前获取某个窗口的句柄: driver.current_window_handle  下次直接通过这个句柄切换回来
        3. 切换到指定窗口，先获取所有窗口的句柄,通过遍历，,一边切换一边到断,如果是目标窗口,则停止循环.

'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.find_element_by_link_text('贴吧').click()   # 点击
driver.find_element_by_link_text('地图').click()   # 点击
driver.find_element_by_link_text('视频').click()   # 点击



# 1.先获取所有窗口的句柄.
''' 获取当前窗口的句柄,下次直接可以切换回来'''
home = driver.current_window_handle  # 获取百度首页的句柄
sleep(2)
''' 切换到最新的窗口'''
# 1. 先获取所有窗口的句柄
windows = driver.window_handles
print(windows)
driver.switch_to.window(windows[-1])   # 通过切换到列表的-1 索引对应的句柄,就是最新窗口
driver.find_element_by_id('wd1').send_keys('uzi')
driver.find_element_by_link_text('进入贴吧').click()

driver.switch_to.window(home) # 通过上面获取的主页句柄,直接切换回去.
driver.find_element_by_id('kw').send_keys('回到主页了')
driver.find_element_by_link_text('图片').click()
''' 切换到指定窗口'''
windows = driver.window_handles
# 通过遍历去判断是否切换到指定窗口 ,
for i in windows: # 每次获取到i 是一个窗口的句柄
    driver.switch_to.window(i) # 先直接切换到这个窗口,
    if '图片' in driver.title: # 判断切换过去后的窗口标题是不是自己想要切换到的窗口/
        break                  # 即停止循环
driver.find_element_by_id('kw').send_keys('切换到了图片')

sleep(5)
driver.quit()

# 练习网易云音乐
'''
学习要点: 
    1.
'''













