# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/22 10:00
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 重要.py
# @Software : PyCharm
#
''''''
import unittest
from time import sleep
from selenium import webdriver

'''
    学习要义:
            1.seleniumIDE是火狐浏览器的插件,可以录制自动化脚本.辅助元素定位.
            2.安装seleniumIDE:右上角菜单-更多工具-面向开发者的扩展-找到seleniumIDE-添加到浏览器.2.使用seleniumIDE:
            3.1)右上角SE图标打开-新建一个项目-给项目取名字-确定.
              2)在地址栏输入被测网址,点击右边的红色rec按钮开始录制.
              3)开始进行测试操作,录制脚本，
              4)测试结束,关闭网页后,点击地址栏右边的停止录制按钮,-给本条用例取名字.
              5)在用例右键-点击export-选择python-导出.
              6）录制的脚本使用的是pytest单元测试框架，在终端输入pytest xx.py运行该脚本.
                   
              
'''