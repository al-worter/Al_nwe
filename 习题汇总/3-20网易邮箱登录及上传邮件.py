# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/20 下午 10:18
# @Author   : liang yuyu
# @Site     : http://www.cdtest.cn/
# @File     : 3-20网易邮箱登录及上传邮件.py
# @Software : PyCharm
''''''
#
'''
登录网易邮箱 https://mail.163.com
1. 输入账号和密码,点击登录,判断是否登录成功.
2. 点击写信-输入收件人-输入主题(自己的名字)-上传附件(代码截图)-输入正文(内容任意)-点击提交-判断是否发送成功.
先用自己的邮箱调试,调试通过之后把收件人写我的邮箱交作业. -- 471132563@qq.com

如果邮箱验证,就等半个小时左右就能恢复.实在不行就重新注册一个.
注意: 如果元素定位的过程中遇到了问题,一个个排查下列情况!!!
1. 元素定位方式是否正确?
2. 是否需要等待时间?  ********
3. 是否打开新窗口?
4. 是否需要定位的元素在页面靠下的位置? -- 操作滚动条
5. 是否嵌套在frame里面?
'''
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://email.163.com/")
sleep(2)
bieber = driver.find_element_by_css_selector('#urs163Area>iframe')  # 由于该表属于动态,先定位到这个表单
driver.switch_to.frame(bieber)  # 然后进行表单切换到该表单

driver.find_element_by_css_selector('#account-box input').send_keys('liangguiyu0807')  # 使用CSS的后代选择器，通过父找子,用空格表示,可以忽略中间的层级直接定位到需要的标签.在需要找到的标签后面最好加上一个属性.用来精确定位

driver.find_element_by_name('password').send_keys('LGYlgy123..')  # class_name  与 by_name  的区别是,其 class 后面有属性值的就用
driver.find_element_by_id('dologin').click()  # 点击登录
sleep(2)

driver.find_element_by_id('_mail_component_149_149').click()
sleep(2)
driver.find_element_by_class_name("nui-editableAddr-ipt").click()
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys('471132563@qq.com')

sleep(2)

driver.find_element_by_css_selector('.fu0 input').click()
driver.find_element_by_css_selector('.fu0 input').send_keys('周姐,这是作业，晚安哟~')

sleep(2)

# driver.find_element_by_css_selector('input[type="file"]').click()  # 添加附件。
# sleep(2)

driver.find_element_by_css_selector('input[type="file"]').send_keys(r'D:\pycharm\zhouwork\clovershrub.png')
sleep(2)
hailey = driver.find_element_by_css_selector('.APP-editor-iframe')  # 由于是iframe 表单会跳动,需要定位到表单.
driver.switch_to.frame(hailey)  # 然后进行表单切换到该表单
sleep(2)
driver.find_element_by_class_name('nui-scroll').send_keys('Good evening, Zhou Jie. This is my homework. Please read it. Thank you very much! My name is : 梁桂瑜')  # 正文内容
driver.switch_to.default_content()  # 返回之前的表单 因为该正文也是 iframe
sleep(1)
driver.find_element_by_css_selector('.jp0>div').click()
sleep(2)
result = driver.find_element_by_css_selector('h1[class="tk1"]').text
if "邮件发送成功" == result:
    print("发送成功")
else:
    print("发送失败")

sleep(5)
driver.quit()
