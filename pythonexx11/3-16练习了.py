# _*_ coding: UTF-8 _*_
# @Time     : 2022/3/16 18:48
# @Author   : Jing wen
# @Site     : http://www.cdtest.cn/
# @File     : 3-16练习了.py
# @Software : PyCharm

# 1. 打开百度首页,输入'汇智动力',点击搜索,判断是否跳转到结果页. (通过获取页面的标题来判断)
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
eles = driver.find_element_by_id('kw')
eles.send_keys("汇智动力")
print(driver.current_url)
driver.find_element_by_id('su').click()
sleep(3)
result = driver.title
print(result)
if "汇智动力" in result:
    print('跳转成功')
else:
    print("跳转失败")
driver.quit() #关闭浏览器
# 2. 获取练习页面的's1'文件的所有class ='vegetable'的元素,并把它们的文本写入到一个文件内.
driver = webdriver.Chrome()
driver.get('file:///D:/python1/%E5%91%A8%E5%A7%90%E8%AF%BE%E7%A8%8B/pages/s1.html')
driver.maximize_window()
eles = driver.find_elements_by_class_name('vegetable')  # 通过赋值变量,遍历找到定位该文本的 元素
with open('./vag.txt', mode='w', encoding='utf8') as file:
    for i in eles:
        str1 = i.text + '\n'
        file.write(str1)

sleep(5)
driver.quit()

# 3. 打开 http://www.weather.com.cn/html/province/sichuan.shtml 获取所有城市的名称和最低温度,
#    最终得到一个列表[['成都',16],['攀枝花',14]............]
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.weather.com.cn/html/province/sichuan.shtml")
# # 找到父标签
father = driver.find_element_by_id('forecastID')
# # 找出下面所有的dl标签
citys = father.find_elements_by_tag_name('dl')
city_infor = []  # [['成都',16],['攀枝花',14]............]
for i in citys:
    print(i.text)  # 每次遍历都获取元素的文本
    print('----------------')
    cityname = i.text.split('\n')[0]  # i.text 通过\n切割['成都','26℃/16℃']  通过索引0来取值,
    loweather = str(i.text.split('/')[1].strip("℃"))  # i.text 通过/切割 ['成都\n26℃','16℃'] 通过索引1来取值, 通过strip("℃") 去掉符号
    city_infor.append([cityname, loweather])
print(city_infor)
sleep(5)
driver.close()
