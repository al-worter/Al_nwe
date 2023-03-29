#
''''''
'''xlwt python中的execel表格标准库
1. 练习
'''
import xlwt
# 导入模块库
# 创建 workbook()
wb  = xlwt.Workbook()
# 创建wokesheet
ws = wb.add_sheet("test_sheet")
# 写入第一行内容，ws.write(a,b,c)   a 行， b 列 ，c 内容
ws.write(0,0,"球队")
ws.write(0,1,"号码")
ws.write(0,2,"姓名")
ws.write(0,3,"wei'zhi")

wb.save("./myexcel.xls")