# # coding=utf-8
# # QQ2737499951
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
import xlwt
#
# # 在内存中创建一个workbook对象，而且会至少创建一个 worksheet
# wb = Workbook()
#
# # 获取当前活跃的worksheet,默认就是第一个worksheet
# ws = wb.active
#
# # 设置单元格的值，A1等于6(测试可知openpyxl的行和列编号从1开始计算)，B1等于7
# ws.cell(row=1, column=1).value = 6
# ws['B1'].value = 7
#
# # 从第2行开始，写入9行10列数据，值为对应的列序号A、B、C、D...
# for row in range(2, 11):
#     for col in range(1, 11):
#         ws.cell(row=row, column=col).value = get_column_letter(col)
#
# # 可以使用append插入一行数据
# ws.append(["我", "你", "她"])
#
# # 保存
# wb.save("TEST.xlsx")
# print('保存完毕')
#
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('xiangxin')
# sheet.write(0,0,'name')  #行,列,内容

title = ['姓名', '班级', '住址', '手机号']

shuzu = [
    ['bred', 'class1', 'mingdong', 188109],
    ['shade', 'class2', 'gugong', 3332],
    ['dd', 'class3', 'changcheng', 6666]
]
# 写入表头
i = 0
for j in title:
    sheet.write(0, i, j)
    i += 1
# 写入表内容
l = 1
for d in shuzu:
    c = 0
    for dd in d:
        sheet.write(l, c, dd)
        c += 1
    l += 1
# 保存
book.save('嵌套循环.xls')
