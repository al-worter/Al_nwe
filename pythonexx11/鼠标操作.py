# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/18 16:40
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 鼠标操作.py
# @Software : PyCharm
#
''''''
import compileall

'''
学习目标:
    1. 鼠标操作需要使用ActionChains类...
    from selenium.webdriver.common.action_chains import ActionChains
    步骤: 先实例化一个ActionChains对象,调用下面的方法,再调用perform()执行操作.
    move_to_element()  悬停
    double_click()     双击
    context_click()     右击
    click_and_hold()    左击悬停
    drag_and_drop()     拖动.
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///H:/a%E6%B1%87%E6%99%BA%E8%AF%BE%E4%BB%B6/python/SeleniumPPT/PPT/pages/pages/move_on.html")

ele = driver.find_element_by_id('aim')  # 先找到需要悬停的元素
ActionChains(driver).move_to_element(ele).perform()
# ActionChains(driver) 代表实例化一个ActionChains对象,并且把driver 传入.
# move_to_element(ele) 代表对元素进行悬停,需要把元素传入
# perform() 执行,
al = driver.switch_to.alert
al.accept() # 点击弹窗的确定.

sleep(2)

ele1 = driver.find_element_by_id('out') # 先找到需要双击的元素
ActionChains(driver).double_click(ele1).perform()   # 双击
al.accept()
sleep(2)

ActionChains(driver).context_click(ele1).perform()  # 右击,
al.accept()
sleep(2)

ele2 = driver.find_element_by_id('two')
ActionChains(driver).click_and_hold(ele2).perform() # 左击悬停,(按住左键不松开.)
al.accept()

driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')    # 进入新的练习页面
driver.switch_to.frame('iframeResult')
begin = driver.find_element_by_id('draggable')  # 找到起始的元素
end = driver.find_element_by_id('droppable')  # 找到目标的元素
ActionChains(driver).drag_and_drop(begin,end).perform()

sleep(5)
driver.quit()