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
1.鼠标操作需要使用ActionChains类.
from selenium.webdriver.common.action_chains import ActionChains

'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///D:/python1/%E5%91%A8%E5%A7%90%E8%AF%BE%E7%A8%8B/pages/move_on.html')
ele = driver.find_element_by_id('aim')  # 先找到需要悬停的元素
ActionChains(driver).move_to_element(ele).perform()
# ActionChains(driver)代表实例化一个ActionChains对象，并且把driver传入
# move_to_element（ele）代表对元素进行悬停，需要传入元素位置
# perform（）代表执行。
al = driver.switch_to.alert
al.accept()  # 点击弹窗的确定
sleep(2)

ele1 = driver.find_element_by_id('out')
ActionChains(driver).double_click(ele1).perform()  # 双击
al.accept()
sleep(2)

ActionChains(driver).context_click(ele1).perform()  # 右击
al.accept()
sleep(3)

ele2 = driver.find_element_by_id('two')
ActionChains(driver).click_and_hold(ele2).perform()  # 左击悬停,并按住左键不松开
al.accept()
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.switch_to.frame('iframeResult')
begin = driver.find_element_by_id('draggable')  # 找到起始的元素
end = driver.find_element_by_id('droppable')  # 找到目标的元素
ActionChains(driver).drag_and_drop(begin, end).perform()

sleep(4)
driver.quit()
