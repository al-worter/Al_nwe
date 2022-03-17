# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 14:34
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 1_元素定位方式.py
# @Software : PyCharm

'''
学习目标:
1. id是元素的唯一身份标识,在元素id的情况下,优先使用id进行定位.
2 .掌握常用方法 :
    1) send_keys() 对元素进行输入
    2  click()    点击
    3) driver.title  获取页面标题
    4) driver.current_url  获取页面的url地址
    5) get_attribute() 获取元素的其他属性的值, 通过元素调用方法
    6) text 获取元素的文本,通过元素调用方法
    7)  _clear() 即把元素里面的内容清空
'''
from selenium import webdriver
from time import sleep  # time 标准库,sleep 是一个函数,用来实现脚本等待.

# 2. 实例化一个谷歌浏览器对象,用来获取一个空白页面的谷歌浏览器
driver = webdriver.Chrome()
# 3.使用get 方法打开被测网址
driver.get("https://www.baidu.com/")
driver.maximize_window()

# 通过对id 对输入框进行元素定位
ele = driver.find_element_by_id('kw')  # 1 先找到这个元素, ele 现在就代表这个输入框的元素.
ele.send_keys('python自动化,入门到精通')  # 2 . 对元素进行输入

print(driver.current_url)  # 获取页面url网页地址

# 对元素进行操作
print(ele.size)   # 获取元素的尺度
print(ele.get_attribute("class"))  #获取元素其他属性的值,这里获取的是class属性的值
print(ele.text) # 获取元素的文本,这个元素没有文本,所以会获取到一个空行.
ele.clear() # 意思是把元素里面的内容清空
sleep(3)
ele.send_keys('超凡蜘蛛侠')

driver.find_element_by_id('form').submit() # submit( ) 类似于 回车键的作用 只适用于标签的父标签是form的情况下

driver.back()  # 回退页面

# driver.find_element_by_id('su').click()  # 对搜索按钮进行点击
# # 如果需要验证那么可以让程序暂缓 给跳转进行验证
# sleep(3)  ##因为点击搜索后,页面跳转需要时间,所以需要写一个sleep,否则获取的是搜索前的页面的标题.
# # 4 如何知道获取该页面,通过该页面标题文本判断是否跳转到结果页面
# result = driver.title  # 通过给一个变量 result 判断页面标题文本
# print(result)
# if 'python自动化,入门到精通' in result:
#     print('跳转成功')
# else:
#     print('跳转失败')








# driver.quit() #关闭浏览器
# driver.close()#脚本写完关闭窗口
