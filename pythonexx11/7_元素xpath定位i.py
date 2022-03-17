# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/17 16:18
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 7_元素xpath定位i.py
# @Software : PyCharm


"""
学习目标: 1)  xpath 是根据元素的路径来定位
                绝对路径: /开头 ,从htlm 标签开始,
                相对路径:  // 开头,可以从任意一个目录开始,一层层往下写.
         2) xpath 的定位方式:
                1.通过元素的属性,属性名前面必须加@符号.
                2.通过元素的文本,使用 text()= "  "  (xpath 可以通过文本定位任意标签,而link_text只能定位a标签)

         3)

"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')

# driver.find_element_by_xpath('/htlm/body/div/div/div/div[5]/.....')  #绝对路径的写法
# driver.find_element_by_xpath('//form[@id="form"]/span/input').send_keys(123)  # 相对路径 通过元素的属性来找子标签
# driver.find_element_by_xpath('//div[@id="s-top-left"]/a').click()  # 相对路径 通过元素的属性来找子标签

# driver.find_element_by_xpath('//span[text()="设置"]').click()  # 通过文本来定位,使用text()= "...."

# driver.find_element_by_xpath('//a[contains(@href,"hao123")]').click() # 通过模糊匹配元素的属性href属性,包含hao123
# driver.find_element_by_xpath('//span[contains(text(),"商务部")]').click() # 通过匹配文本包含"商务部"的方式
# driver.find_element_by_xpath('//span[starts-with(text(),"茅台")]').click() # 通过匹配开头,文本包含"茅台"


sleep(5)
driver.quit()





















