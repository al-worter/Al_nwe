# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/17 10:35
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 6_元素定位方式_css.py
# @Software : PyCharm

'''
学习目标:
        1. css可以通过元素的三种属性直接定位到:
        id    使用 # 来表示.
        class 使用 . 来表示.
        标签名 没有任何符号,直接写标签名.
    2. css的选择器:
        1)子选择器:通过父找子,用>符号表示,必须一层一层的往下写
        2)后代选择器:通过父找子,用空格表示,可以忽略中间的层级直接定位到需要的标签.在需要找到的标签后面最好加上一个属性.用来精确定位.
        3)兄弟选择器:通过兄找弟,使用+来表示,+后面写标签名
    3.css的模糊匹配:
        1) 匹配包含 使用*=
        2) 匹配开头 使用^=
        3) 匹配结尾 使用$=
    :nth-child() 通过父标签指定定位第n个子标签
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
# driver.find_element_by_css_selector('#kw').send_keys(123)   #通过元素的id属性来直接定位.id用#表示
# driver.find_element_by_css_selector('.s_ipt').send_keys(456) #通过元素的class属性来直接定位.class用.表示
# driver.find_element_by_css_selector('input[name="wd"]').send_keys(789)  #通过元素的标签来定位,因为重名的标签很多,所以在标签名后面指定一个属
#


# 通过父标签找输入框
# # 1.子选择器,用>表示,子选择器必须一层一层进行往下写.
# driver.find_element_by_css_selector('#form>span>input').send_keys(1111)
# #2. 都带选择器,用空格表示,后代 选择器可以忽略中间层的层级,直接定位到需要的位置的一些需要的标签
# driver.find_element_by_css_selector('#form input[autocomplete="off"]').send_keys(5555)
#
# # 兄弟选择器 使用 + 来表示,+后面写标签名
# driver.find_element_by_css_selector('a[href="http://map.baidu.com"] +a').click()  #通过地图找第一个弟弟——贴吧.
# driver.find_element_by_css_selector('a[href="http://map.baidu.com"] +a +a').click() # 通过地图找第二个弟弟--视频
#
#css模糊匹配
#1. 匹配包含 使用 *=
driver.find_element_by_css_selector('a[href*="image"]').click() #找一个href包含image的a标签

#2. 匹配开头   使用 ^=
driver.find_element_by_css_selector('a[href^="https://pan"]').click()   #找一个href是以https: // pan开头的a标签.
#3 . 匹配结尾 使用$=
driver.find_element_by_css_selector('a[href$="from=baidu-top"]').click()   #找一个href是以from=baidu-top结尾的a标签

# driver.find_element_by_css_selector('#s-top-left>a:nth-child(4)').click()  # 通过父标签找到第四个a子标签
driver.find_element_by_css_selector('#s_menus_wrapper>span:nth-child(3)').click()  # 通过父标签找到第四个a子标签

driver.find_element_by_css_selector('*[href="http://map.baidu.com"]').click()  # *如果出现在=前面.才是包含匹配,如果出现在本来应该写标签名的
driver.find_element_by_css_selector('*["class="s-menu-item"]').click()  # *如果出现在=前面.才是包含匹配,如果出现在本来应该写标签名的


sleep(5)
driver.quit()

'''
 []中括号里面 写标签里的属性
<div id = 'kk'>
    <a>
    <inpput>
    <a>
</div>

#kk>a:nth-child(2)    找一个id=kk的元素下面的第二个子标签a,那么找到就是上面的第三个子标签
#kk>*:nth-child(2)  找一个id=kk的元素下面的第二个子标签,那么找到就是上面的第二个子标签

'''
# driver.find_element_by_css_selector('input[maxilength="255"][name="wd"]').send_keys('好莱坞大片')


