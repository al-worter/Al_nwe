# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 11:47
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-21 元素等待脚本.py
# @Software : PyCharm
#
''''''
'''
    1.slccp等于是强制等待脚本休眠.设置了多少秒就会等待多少秒.
     隐式等待:等待全局元素加貌。如果在规定的时间内找到了这个元素,就继续运行,不会强制等祸时间.如果超过最大等待时长没找到元素则报错.
     显示等待:针对等待某一个元素加软,每隔多少秒检查一次,如果在规定的时间内找到了这个元素,就继续运行，
            不会强制等满时间.如i果超过最大等待时长没找到元素则报错.
     如果隐式等待和显示等待同时使用,以时间长的为准.       
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait   # 显示等待需要用到 WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///D:/python1/%E5%91%A8%E5%A7%90%E8%AF%BE%E7%A8%8B/pages/example.html')
driver.implicitly_wait(5) # 方法1 隐形等待,等待全局元素加载,如果在规定的时间的时间内找到这个元素,就继续运行,不会强制等满时间.如果超过最大等待时长没找到
driver.find_element_by_id('opendoor').click()  # 点击开启传送门
# driver.find_element_by_id("baidu").click() # 点击百度一下.

'''
显示等待:
    1) WebDriverWait(driver,5,0,2)代表: 实例化一个WebDriverWait对象,里面传入三个参数,第一个是driver,第二个是最大等待时长,
                                        第三个是每隔多少秒检查一次元素是否加载成功.
    2) 调用until 方法进行显示等待,匿名函数冒号右边是返回值,也就是需要进行等待的元素.|
'''
WebDriverWait(driver,5,0,2).until(lambda x:x.find_element_by_id("baidu")).click()

sleep(5)
driver.quit()

# 匿名函数/隐藏函数

# 定义一个普通函数,接收三个形参,函数体返回三个形参的和,
def he(a,b,c):
    return a+b+c
print(he(1,2,3))

# 定义匿名函数实现同样的功能.
hailey = lambda a,b,c:a+b+c  #  =左边是定义值  ,右边是设置形参值  .并且匿名函数使用lambda关键字声明,后面写函数的形参,形参后面 :冒号后面就是函数的返回值.
print(hailey(8,8,8)) # 匿名函数和普通函数一样调用