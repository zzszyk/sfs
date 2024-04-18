import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',password='1235649Yuky',database='dbsclab2018',charset='utf8')
cursor=conn.cursor()
sql='select name,salary,rank() over(order by(salary)) as s_rank from instructor order by salary'
cursor.execute(sql)
redat=cursor.fetchall()
for row in redat:
	print(row[0],':',row[1],':',row[2])
cursor.close()
conn.close()
