import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', database='py_mysql_demo', port=3306)
cursor = conn.cursor()
sql = """
insert into position_demo(id,position_name,position_salary,position_city,position_experience,position_form,job_detail) values(2,'xiaoli','20k','zz','wu','quanzhi','www')
"""
cursor.execute(sql)  # 执行   第二个参数以元组的方式传入
conn.commit()
conn.close()
