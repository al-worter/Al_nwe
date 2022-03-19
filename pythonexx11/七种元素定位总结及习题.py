# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/17 下午 10:30
# @Author   : liang yuyu
# @Site     : http://www.cdtest.cn/
# @File     : 七种元素定位方式总结.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep

# d第一种元素定位方式 时通过id
'''
 id方式定位：1.在元素有id的情况下首先使用id 来进行定位。
            2.常用的方法有：
                1）.send_keys('') 对元素 属性 Input类输入框进行输入.
                2）.click() 是对该botton进行 点击操作
                3） driver.title  是获取该网页的标题
                4）driver.current_url  获取页面的URL地址 可以通过print打印
                5）对该位置的元素操作：
                5) get_attribute()  获取元素的其他属性的值 通过元素调用方法.
                6) text 获取元素的文本,通过元素调用方法.
                7) clear() 把元素的内容清空
                    1.print(ele.size)   # 获取元素的尺度
                    print(ele.get_attribute("class"))  #获取元素其他属性的值,这里获取的是class属性的值
                    print(ele.text) # 获取元素的文本,这个元素没有文本,所以会获取到一个空行.
                    ele.clear() # 意思是把元素里面的内容清空
                6）driver.back()  # 回退页面
                7) driver.forward()  # 前进页面
                8) driver.refresh()  # 页面刷新
                9) driver.set_window_size(600,800)  # 将窗口设置成600x800大小
                10)# driver.quit() #关闭浏览器
                   # driver.close()#脚本写完关闭窗口 
'''
# 例如：
# 2. 实例化一个谷歌浏览器对象,用来获取一个空白页面的谷歌浏览器
driver = webdriver.Chrome()
# 3.使用get 方法打开被测网址
driver.get("https://www.baidu.com/")
driver.maximize_window()
# 通过对id 对输入框进行元素定位
ele = driver.find_element_by_id('kw')  # 1 先找到这个元素, ele 现在就代表这个输入框的元素.
ele.send_keys('python自动化,入门到精通')  # 2 . 对元素进行输入
driver.find_element_by_id('form').submit()  # submit( ) 类似于 回车键的作用 只适用于标签的父标签是form的情况下
driver.back()  # 回退页面
# driver.find_element_by_id('su').click()  # #如果不是form标签就用该click（）
# 4 如何知道获取该页面,通过该页面标题文本判断是否跳转到结果页面， 可以给一个形参 对该参数赋值如下
result = driver.title  # 通过给一个变量 result 判断页面标题文本
print(result)
if 'python自动化,入门到精通' in result:
    print('跳转成功')
else:
    print('跳转失败')

#  第二种元素定位的方式 _name 的方式 。即为属性例如： class  name type value 等
'''
学习要点：
    1.name元素的属性，在页面上除了id 不会重复，其他的属性都有可能重复
      如果存在多个重名的元素，默认找第一个.name 或者其他的
    2..find_element_ ...  : 是找一个元素。 
        find_elements_    : 是找多个元素 。  即如果该属性重复，检索为多个就需要加S 
'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///D:/pycharm/zhouwork/pages/pages/s1.html')
driver.find_element_by_name('botton').click()  # 如果存在多个相同同名的元素不判断选择哪一个，即默认选择第一个。
# 如需判断则 设对象赋值。
eles = driver.find_element_by_name('botton')  # 找出所有页面name = botton 的元素
print(eles)  # find_elements会以列表的形式返回出页面所有满足的元素
for i in eles:  # 遍历这个装着所有name=button的元素的列表
    if i.text == '按钮2':  # 判断如果当前遍历到的元素的文本是按钮2
        i.click()  # 就点击.

# 第三种 通过classname 即class的属性值来判断定位  _class_name
'''
    学习要点：1. classname就是元素的class属性的值,如果在定位的时候发现这个元素有多个class的值,只取其中一个进行定位. 即也可通过判断该点的文本内容
            
'''
driver.get('file:///H:/a%E6%B1%87%E6%99%BA%E8%AF%BE%E4%BB%B6/python/SeleniumPPT/PPT/pages/pages/s1.html')
eles = driver.find_elements_by_class_name('cheese')  # 先找到页面上所有class=cheese的元素, 即通过该元素再判断文本是什么。
for i in eles:
    if i.text == 'Gouda':
        print('找到了.')
sleep(5)
driver.quit()

# 第四种通过 tagname元素进行定位  find_element_tag_name()
'''
学习要点： 1，tagname值的时元素的标签，标签名肯定会重复，所以一般用 find_elements 来定位，element 后加了个s 因为时多元素。
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
# eles = driver.find.elements_by_tag_name('a')  # 找出页面上所有的a标签, 该方式效率比较低,.同时找出的a标签元素会很多.父标签以外的也会搜出来
# 1.先找出目标a标签的父标签
father = driver.find_element_by_id('s-top-left')  # 该id是在网页上div这个模块的这个ID定位属性   r如百度导航框上的视频贴吧 图片。
# 2. 再找出这个父标签下面所有的a标签.
eles = father.find_elements_by_tag_name('a')
print(eles)
for i in eles:
    if i.text == '视频':  # 如果当前元素的文本 是视频
        i.click()  # 就点击
        break  # 循环找到之后就停止该循环遍历
sleep(5)
driver.quit()

# 第五种 通过_link_text 元素定位 ，拟用在超链接的标签上 模糊匹配或者完全匹配
'''
学习要义:   1 . link_text通过超链接(a标签)的文本来进行定位.必须要完全匹配文本.
            2. partial_link_text(也只能够定位a标签,可以通过部分文本模糊匹配
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
driver.find_element_by_link_text('图片')  # 直接通过a标签的文本进行丁文 ，要完全匹配
driver.find_element_by_partial_link_text('片')  # 多加个_partial 是模糊匹配文本包含有片的a标签
sleep(3)
driver.quit()

# 第六种 元素定位： _css_selector
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
driver.get('http://www.baidu.com')
driver.find_element_by_css_selector('#kw').send_keys(123)  # 通过元素的id属性来直接定位.id用#表示   即该网页的输入框 input标签的ID
driver.find_element_by_css_selector('.s_ipt').send_keys(456)  # 通过元素的class属性来直接定位.class用.表示
driver.find_element_by_css_selector('input[name="wd"]').send_keys(
    789)  # 如标签名没有任何符合，直接写标签名。 通过元素的标签来定位,因为重名的标签很多,所以在标签名后面指定一个属性
sleep(1)
# css 1）子选择器 ，通过父标签找子标签，并且一层一层往下写 输入框
driver.find_element_by_css_selector('#form>span>input').send_keys(111)
# 还有一种方式是 ：如下
driver.find_element_by_css_selector('#s-top-left>a:nth-child(4)').click()  # 通过父标签找第四个a子标签
driver.find_element_by_css_selector(
    '*[href="http://map.baidu.com"]').click()  # *如果出现在=前面.才是包含匹配,如果出现在本来应该写标签名的位置,代表任意标签.
# css 2) 后代选择器,用空格表示,后代选择器可以忽略中间的层级,直接定位到需要的标签.
driver.find_element_by_css_selector('#form input[maxlength="255"]').send_keys(222)
# css 3) 兄弟选择器: 使用+来表示,+后面写标签名
# 需求通过地图找贴吧,
driver.find_element_by_css_selector('a[href="http://map.baidu.com"] +a').click()  # 通过地图找第一个弟弟 --贴吧.
driver.find_element_by_css_selector('a[href="http://map.baidu.com"] +a +a').click()  # 通过地图找第二个弟弟 --视频

# css的模糊匹配.
# 1.匹配包含   使用 *=
driver.find_element_by_css_selector('a[href*="image"]').click()  # 找一个href包含image的a标签.
# 2.匹配开头  使用 ^=
driver.find_element_by_css_selector('a[href^="https://pan"]').click()  # 找一个href是以https://pan开头的a标签.
# 3.匹配结尾 使用 $=
driver.find_element_by_css_selector('a[href$="from=1026962h"]').click()  # 找一个href是以from=1026962h结尾的a标签.

# 父标签找子标签 的用义解析如下：
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
driver.find_element_by_css_selector('inputmaxlength="255"').send_keys(123)  # 如果给标签指定一个属性,特征还不够明显.可以在后面再加一对括号,指定第二个属性。

# 第七种 xpath元素定位方式
'''
学习要义：
    1. xpath是根据元素的路径来定位的：
        绝对路径: /开头,从html标签开始,一层层往下写  
        相对路径: //开头,可以从任意一个目录开始,一层层往下写,
    2. xpath的定位方式:
        1) 通过元素的属性,属性名前面必须要加@符号.
        2) 通过元素的文本,使用text()= " " . (xpath可以通过文本定位任意标签,而link_text只能定位a标签.)
    3. xpath的模糊匹配.：
        1) 匹配包含, 使用contains()函数, 里面需要传入两个参数,第一个是匹配的方式,@属性名或者text() 第二个是模糊匹配的值.
        2) 匹配开头, 使用starts-with()函数, 里面需要传入两个参数,第一个是匹配的方式,@属性名或者text() 第二个是模糊匹配的值.
    4.xpath 的选择器:
        1) xpath 必须一层层的写路径,没有后代选择器.
        2) 从上往下找:例如百度页面上的 从地图 找 贴吧  .后面有folloing-sibling::标签
        3) 从下往上找:  ..... 后面有preceding-sibling::标签
        4) 通过子标签找父标签: 使用 .. 返回上一层目录.即可找到父标签.

'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
# 1). 绝对路径的开头是以 / htlm开始
driver.find_element_by_xpath('/html/body/div/div/div[5]/......')  # 绝对路径的写法.   很麻烦，一般用不着
# 2)  相对路径 是以 // 开头，可以从任意标签开始写起
driver.find_element_by_xpath('//form[@id="form"]/span/input').send_keys(123)  # 相对路径,通过元素的属性来找到子标签.
driver.find_element_by_xpath('//div[@id="s-top-left"]/a').click()  # 相对路径 通过元素的属性/来找子标签
driver.find_element_by_xpath('//span[text()="设置"]').click()  # 通过文本来定位,使用text()= "...."
driver.find_element_by_xpath('//a[contains(@href,"hao123")]').click()  # 通过匹配元素的href属性,包含hao123
driver.find_element_by_xpath('//span[contains(text(),"商务部")]').click()  # 通过匹配文本包含'商务部'的方式,
driver.find_element_by_xpath('//span[starts-with(text(),"茅台")]').click()  # 匹配开头, 文本包含'茅台'

# xpath 兄弟选择器
#  例如 在百度页面: 从地图找贴吧
driver.find_element_by_xpath('//a[text()="地图"]/folloing-sibling::a').click()  # 找第一个弟弟标签
driver.find_element_by_xpath('//a[text()="地图"]/folloing-sibling::a[2]').click()  # 找第二个弟弟标签
# 从下往上找
driver.find_element_by_xpath('//a[text()="贴吧"]/preceding-sibling::a').click()  # 标签名后面不写数字,默认找第一个哥哥标签
driver.find_element_by_xpath('//a[text()="贴吧"]/preceding-sibling::a[1]').click()  # 标签名后面写数字,代表从自己开始往上找
# 通过子标签找父标签 ,使用
print(driver.find_element_by_xpath('//a[text()="贴吧"]/..').get_attribute('id'))  # 找到父标签后,获取父标签的id

sleep(3)
driver.quit()

'''
一 > xpath 和 css 的区别:
    1: xpath 比css更加灵活
    2: 性能比css较差 , 效率不及css
    3: xpath稳定性较差, 因为xpath必须通过路径一层层定位,有可能因为前端页面的改变导致脚本出现问题.
    4: xpath在不同的浏览器表现方式可能不同.  
二 > 常见的
     有id 元素的优先使用id来定位
     如果css定位不到的可以用xpath
     a 标签 ,用文本标签 定位
'''

'''
练习题: 使用脚本,自动化搜索12306 从出发地址 -目的地  再点昨天
'''
