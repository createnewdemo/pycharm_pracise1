import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', database='py_mysql_demo', port=3306)
cursor = conn.cursor()
# 插入数据
sql = """
update user set username='aaa' where id=2
"""

# select * from user  表示取出所有数据
# username = 'spider'
# age = 21
# password = '12345'
cursor.execute(sql)  # 执行   第二个参数以元组的方式传入
conn.commit()
# result = cursor.fetchone()
# print(result)
# conn.commit()#提交数据
conn.close()
# cursor.execute("select 1")#执行语句
# result = cursor.fetchone()
# print(result)
