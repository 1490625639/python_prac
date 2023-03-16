def jv():
    num=2
    print(num)
# print(num)
# 局部变量只能在函数内使用，在函数外边会出错没有定义
# 在函数执行时被创建，函数执行后被回收
"""全局变量 glob
在函数外部定义的变量，所有函数都能使用这个变量
"""
g_num=12
def oi():
    print(g_num)
def ooo():
    # 全局变量修改使用global 变量名来告诉系统要修改一下全局变量
    global g_num
    g_num=122
    print(g_num)
oi()
ooo()