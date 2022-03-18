# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 14:38
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 表单切换练习3-18.py
# @Software : PyCharm


# 网易云音乐表单练习切换
'''
    学习要点:
        1.当需要定位的元素嵌套在frame/iframe里面的时候,就需要先切换表单,
          才能定位到该元素.使用switch_to.frame()进行切换.
    切换问题1:  如果这个frame/iframe标签有id或name属性,就可以直接切换过去.
    切换问题2: 如果这个frame/iframe标签没有id和name,就需要先定位到这个标签,再进行切换.
                如果进入表单后,需要操作表单外面的元素.还需要先从表单里切换出去:driver.switch_to.default_content()


'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://music.163.com/#/discover/toplist")
sleep(1)
# driver.switch_to.fram('g_iframe')  # 通过id的值进行切换
# driver.switch_to.frame('contentFrame') # 通过name 的值直接切换
''' 如果这个frame / iframe 没有标签id 和name '''
biaodan = driver.find_element_by_class_name('g-iframe') # x先定位到这个表单
driver.switch_to.frame(biaodan) # 再进行切换                                  上面这两步是跟上面意义
driver.find_element_by_css_selector('b[title="爱丫爱丫"]').click()
sleep(4)
# 如果进入表单后,需要操作表单外面的元素,还得从之前的表单切换出去
driver.switch_to.default_content()  # 从之前的表单切换出来
driver.find_element_by_id('srch').send_keys('七里香')
driver.back()  # 回退页面
biaodan = driver.find_element_by_class_name('g-iframe') # x先定位到这个表单
driver.switch_to.frame(biaodan) # 再进行切换
driver.execute_script('window.scrollTo(0,10000)')   # execute_script()  用来操作js代码,这一行的意思
driver.find_element_by_css_selector('b[title="与你到永久"]').click()

sleep(5)
driver.quit()