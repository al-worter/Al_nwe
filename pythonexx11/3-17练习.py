# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/17 18:19
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-17练习.py
# @Software : PyCharm
'''
进入网站 https://kyfw.12306.cn/otn/leftTicket/init
出发地输入 nanjingnan\n (注意,这两个输入框比较特殊,必须先click,再send_keys,不然输入不进去.)
目的地输入 hangzhoudong\n
出发日期选择第二天(是点击出发地下面的第二天的元素,不是选择出发日的日历)
    1.判断是否搜索出结果页(找一个搜索结果页之前没有的元素来进行判断.)
    2.找出当天所有的车次编号.写入文件.
    3.找出所有有二等座的车次,写入文件.(注意观察有二等座的元素和没有二等座的元素的区别.)
'''

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.find_element_by_css_selector('#fromStationText').click()
driver.find_element_by_css_selector('#fromStationText').send_keys('南京南\n')
driver.find_element_by_css_selector('#toStationText').click()
driver.find_element_by_css_selector('#toStationText').send_keys('杭州东\n')
driver.find_element_by_css_selector('#date_range>ul>li:nth-child(2)').click()
sleep(1)
#
# 方法一: result = driver.find_element_by_css_selector('#sear-result>p>strong').text  # 获取结果页的文本.,
#1. 判断是否搜索成功
# if '南京南 --> 杭州东' in result: # 判断结果包含'南京南 --> 杭州东'
#     print('搜索成功')
# else:
#     print('搜索失败')
# #
# result = str(driver.find_element_by_css_selector('#trainum'))  # 通过检验 显示车次大于0极为成功
# if result != 0:
#     print('搜索成功')
# else:
#     print("搜索失败")
# 2.找出当天所有的车次编号.写入文件.
# all = driver.find_elements_by_css_selector('a[title="点击查看停靠站信息"]')  # 找出所有的车次编号的元素.
# 也可以用 css_ 的兄弟标签 例如任意标签 a[ ]
# with open('123061.txt', mode='w', encoding='utf8') as file:
#     infor = driver.find_elements_by_class_name('bgc')
#     for i in infor:
#         list1 = i.find_element_by_class_name('number').text
#         file.write(f'{list1}\n')
# 3.找出所有有二等座的车次,写入文件.(注意观察有二等座的元素和没有二等座的元素的区别.)
# 有二等座和没有二等座的区别是,有没有class属性.
# 先找到所有的车次信息,
all_info = driver.find_elements_by_css_selector('tr[id^="ticket"]')  # 通过找id是以ticket开头的所有tr标签
with open('二等座车次.txt', 'w', encoding='utf8') as file:
    for i in all_info:  # 循环所有的车次信息,每次遍历到的i就是一个tr标签
        second = i.find_element_by_css_selector('td:nth-child(4)').get_attribute('class')  # 通过这个tr标签,去找下面的第4个td标签,然后获取class属性.,如果这个元素有class属性会返回属性的值,如果没有class属性会返回空.
        print(second)
        if second:  # 如果这个元素获取的second是True,就说明是一个有二等座的车次.
            info = i.find_element_by_css_selector('a[title="点击查看停靠站信息"]').text  # 那么就获取这个车次的编号.
            file.write(info + '\n')
sleep(5)
driver.quit()
