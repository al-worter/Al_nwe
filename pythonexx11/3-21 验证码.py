# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/21 14:29
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-21 验证码.py
# @Software : PyCharm
#
''''''
'''
    测试中的验证码解决方式:
        1.去掉验证码.(只适用测试环境.)
        2.设置一个万能验证码.(常用)
        3.验证码识别技术,(过时)
        4.利用浏览器的加载项配置跳过验证.
            步骤: 
                1.一定需要用脚本打开一次被测网址.
                2.手动登录一次,并且勾选上免登录
                3. 并在浏览器, chrome://version 复制下面的个人资料路径
                    比如:我们就只要C:\\Users\\Administrator\\AppData\\Local\\Temp\\scoped_dir9520_1055425087不要后面的default
                4.实例化加载项配置
                5.把个人的资料,加到配置对象里
                6.实例化浏览器对象,同时把配置对象传入.
                7.打开被网址.(一定要确保将之前的网页全部关闭)        
'''
from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.mail.163.com')
# # 获取个人资料路径
user = r'--user-data-dir=C:\Users\Administrator\AppData\Local\Temp\scoped_dir9520_1055425087'
# 实例化加载项配置
option = webdriver.ChromeOptions()
# 往加载项配置对象里面添加个人信息
option.add_argument(user)
#实例化浏览器对象,同时把配置对象传入
driver = webdriver.Chrome(chrome_options=option)
driver.get('http://www.mail.163.com')



