# """完成数据库相关的工具类封装
#     1.主要方法
#     2.辅助方法
#         获取连接对象
#         获取游标对象
#         关闭游标对象方法
#         关闭连接对象方法
#     """
# import pymysql
#
#
# # 定义一个类方法
# class ReadDB:
#     conn = None
#     #获取连接对象
#     def get_conn(self):
#         if self.conn is None:
#             self.conn = pymysql.connect(
#                 host="localhost",
#                 database="hmtt",
#                 user='root',
#                 password='123456',
#                 charset='utf8'
#             )
#         return self.conn
#     #获取游标对象
#     def get_cursor(self):
#         # 调用获取连接对象方法，
#         return self.get_conn().cursor()
#     #关闭游标对象
#     def close_cursor(self, cursor):
#         #        self.get_cursor().close()
#         if cursor:
#             cursor.close()
#     #关闭连接对象
#     def close_conn(self):
#         #        return self.get_conn().close()
#         if self.conn:
#             self.conn.close()
#             # 注意，关闭连接对象后，对象害存在内存中，需要手动设置为none
#             self.conn = None
#
#     # 主要执行方法----在外界调用一次就可以实现数据的操作
#     def get_sql_one(self,sql):
#         #定义游标对象和数据变量
#         sursor=None
#         data=None
#         try:
#             #获取游标对象
#             sursor=self.get_cursor()
#             #调用执行方法
#             sursor.execute(sql)
#             #获取结果
#             data=sursor.fetchone()
#         except Exception as  e:
#             print("get_sql_error",e)
#         finally:
#             #关闭游标对象
#             self.close_cursor(sursor)
#             #关闭连接对象
#             self.close_conn()
#             #返回执行结果
#             return data
#     #获取所有数据库数据集
#     def get_sql_all(self,sql):
#         # 定义游标对象和数据变量
#         sursor = None
#         data = None
#         try:
#             # 获取游标对象
#             sursor = self.get_cursor()
#             # 调用执行方法
#             sursor.execute(sql)
#             # 获取结果
#             data = sursor.fetchall()
#         except Exception as  e:
#             print("get_sql_all", e)
#         finally:
#             # 关闭游标对象
#             self.close_cursor(sursor)
#             # 关闭连接对象
#             self.close_conn()
#             # 返回执行结果
#             return data
#     #修改删除新增
#     def update_sql(self,sql):
#
#         # 定义游标对象和数据变量
#         sursor = None
#         data = None
#         try:
#             # 获取游标对象
#             sursor = self.get_cursor()
#             # 调用执行方法
#             sursor.execute(sql)
#             #无论是新增删除还是修改，都要通过事务进行操作
#             self.conn.commit()
#         except Exception as  e:
#             self.conn.roolback()
#             print("get_sql_error", e)
#         finally:
#             # 关闭游标对象
#             self.close_cursor(sursor)
#             # 关闭连接对象
#             self.close_conn()

# 导包
from pymysql import *
# 创建数据库的连接
conn=connect(host="localhost",user="root",password="123456",database="prac")

# 创建游标对象
cur=conn.cursor()

cur.execute("select * from a")
print(cur.fetchall())