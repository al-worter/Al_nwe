# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 16:03
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3_元素定位练习.py
# @Software : PyCharm

'''
学习目标:
    1. classname 就是元素的class 属性的值, 如果在定位的时候发现有多个class的值,只取其中一个进行定位, 搜索看是否唯一,尽量取最少的.

'''

from selenium import webdriver
from time import sleep

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_class_name('s_ipt').send_keys(123)   # send_keys('')是给该输入框输入内容
# driver.find_element_by_class_name('s_btn').click() # r如果在定位的时候发现这个元素有多个classz值,只取其中一个进行定位.

# 练习1:
# driver.get('file:///D:/python1/%E5%91%A8%E5%A7%90%E8%AF%BE%E7%A8%8B/pages/s1.html')
# eles = driver.find_elements_by_class_name('cheese')  # 通过赋值变量,遍历找到定位该文本的 元素
# for i in eles:
#     if i.text == 'Gouda':
#         print('找到了')

# 练习2
'''
http://www.51job.com
搜索关键词 python， 地区选择 杭州（注意，所在地已经选中，要取消）， 判断是否搜索出结果页.
'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.51job.com')

driver.find_element_by_css_selector('#kwdselectid').send_keys('python')  # 有id 的可以直接定位id到该
driver.find_element_by_css_selector('#work_position_input').click()  # dia点击地址

eles = driver.find_elements_by_css_selector('#work_position_click_multiple_selected>span')  # 先点击几个城市,会出现一行已选的城市,该位置是,通过检验脚本是否默认选中的所有城市标签
# 找出默认选中的所有城市标签
# 再通过报错检验 try except 判断 .在没有默认选中的城市情况下,那么就使用try来执行,如果报错就直接执行.
try:  # 在没有默认选中的情况下
    for i in eles:  # 遍历装着默认选中的城市的列表
        i.click()
except:
    pass

driver.find_element_by_css_selector('#work_position_click_center_right_list_category_000000_080200').click()  # 点击深圳
driver.find_element_by_css_selector('#work_position_click_bottom_save').click()  # 点击确定
driver.find_element_by_css_selector('.top_wrap>button').click()  # 点击 搜索
sleep(1)
result = driver.title  # 获取结果页面的标题  通过页面标题检验
if '【杭州,python招聘，求职】-前程无忧' == result:
    print('搜索成功')
else:
    print("搜索失败")

driver.find_element_by_css_selector('.tleft>span:nth-child(3)').click()
sleep(1.5)
info = driver.find_elements_by_css_selector('.j_joblist>div')  # 找出所有的职位信息元素,
with open('workjob.txt', mode='w', encoding='utf8') as file:
    for i in info:  # 遍历所有职位信息的列表
        jobname = i.find_element_by_css_selector('.jname').text  # 职位名称
        cname = i.find_element_by_css_selector('.cname').text  # 公司名称
        address = i.find_element_by_css_selector('.d').text.split('|')[0]  # 把地址写入的同时 用分割和索引进行写入
        sal = i.find_element_by_css_selector('.sal').text  # 工资
        time = i.find_element_by_css_selector('.time').text  # 发布时间
        file.write(f'{jobname}|{cname}|{address}|{sal}|{time}\n')

sleep(5)
driver.quit()
