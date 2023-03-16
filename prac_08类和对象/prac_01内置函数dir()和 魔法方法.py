import os
for i in range(1,10):
  file=  open("prac_%s面向对象.py"%i,"w",encoding="utf-8")
# 特征--属性--方法
# 行为--方法--函数
# dir()是python中内置的函数
# 可以查看变量/对象/数据的 所有属性和方法

"""_new_方法  创建对象时 会被自动调用
_init_方法 对象被初始化时，会被自动调用
—del_方法  对象从内存销毁前，会被自动调用
_str_方法  返回对象的描述信息 print()函数输出使用"""
file.close()