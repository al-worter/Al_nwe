# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 10:52
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-21 下拉框练习.py
# @Software : PyCharm
#
''''''
'''
点击高级搜索,搜索关键词 python，智能类别选择 自动化测试,  公司性质选择 民营公司,
点击搜索， 获取最新发布职位的公司名称.
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.51job.com/')
sleep(1)
driver.find_element_by_class_name('more').click()
sleep(1)
driver.find_element_by_css_selector('kwdselectid').send_keys('python')
driver.find_element_by_id('funtype_click').click()
sleep(1)
driver.execute_script('document.getElementById("KwdSearchResult").style.display="none"')  # 把该元素的display属性的值改成none,该元素则隐藏
# driver.execute_script('document.getElementById("KwdSearchResult").style.display="block"') # 把该元素的display属性的值改成block,该元素则可见
sleep(1)
driver.find_element_by_id('funtpe_click').click()  # 点击+ 号
driver.find_element_by_id('funtpe_click_center_right_list_category_0100_2700').click()  # 点击测试
driver.find_element_by_id('funtpe_click_center_right_list_sub_category_each_0100_2720').click()  # 点击自动化测试
driver.find_element_by_id('funtpe_click_button_save').click()  # 点击确定
driver.find_element_by_id('cottype_list').click()  # 点击下拉框
driver.find_element_by_css_selector("span[title='民营公司']").click()  # 点击民营公司
driver.find_element_by_class_name("p_put").click()  # 点击搜索
sleep(1)
driver.find_element_by_xpath("//span[text()='最新发布']").click()
sleep(1)
print(driver.find_element_by_class_name("cname").text)
