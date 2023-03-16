open("prac05匿名函数_.py", "w", encoding="utf-8")
# *args和*kwargs作为形参时的核心功能就是组包
# 函数名就是一个变量名，保存了当前函数体的引用地址
"""lambda 表达式能创建小型匿名函数

lambda  args参数：表达式
特点 匿名函数把表达式作为整个返回值进行返回
"""
# 不带参数的匿名函数
tet = lambda: 1234
print(lambda: 1234)
print(tet())
# 带参数的匿名函数
ret = lambda x: x + 12
print(ret(23))
print((lambda x: x + 100)(20))

# 定义两个参数的匿名函数
print((lambda x, y: x + y)(20, 12))

# 匿名函数可以作为函数的参数
def sum(a,b,ret):
    print(a)
    print(b)
    print("%d,%d,ret=%d"%(a,b,ret(a,b)))
sum(1,2,lambda x,y:x+y)
lambda x:x+10
print((lambda x:x+10)(12))