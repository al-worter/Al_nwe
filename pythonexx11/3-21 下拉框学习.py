# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 10:29
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-21 下拉框.py
# @Software : PyCharm
#
''''''
'''
学习目标:
    1). 只有 select 标签才是真正的下拉框 ,才可以使用Selec类.
    2).使用from selenium. webdriver. support.select import Sclect导入Sclect类步骤:
        1.找到下拉框
        ⒉实例化一个Select对象
        3.通过文本/value/索引来选择sclect_by_value(通过value属性的值.
        4.select_by_index() 通过索引,索引从0 开始计算
        5.select_by_visible_text() # 通过文本
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///D:/python1/%E5%91%A8%E5%A7%90%E8%AF%BE%E7%A8%8B/pages/s1.html')
sleep(1)
# 1. 先找到select 下拉框
ele = driver.find_element_by_id('choose_car')
sleep(1)
# 2. 在实例化一个select对象
tag = Select(ele)
sleep(1)
# 3. 选择
tag.select_by_value('corolla') # 通过value 属性的值选择
sleep(1)
tag.select_by_visible_text('菲亚特') # 通过文本选择
sleep(1)
tag.select_by_index(3) # 通过索引选择,索引从0 开始计算.

# 如果下拉框不是select 标签
# driver.find_element_by_id()
# driver.find_element_css_selector('option[value="audi"]').click()





'''
点击高级搜索,搜索关键词 python，智能类别选择 自动化测试,  公司性质选择 民营公司,
点击搜索， 获取最新发布职位的公司名称.
'''
from selenium import webdriver
from time import sleep
