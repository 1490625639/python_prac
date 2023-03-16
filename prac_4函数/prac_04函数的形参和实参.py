# 函数参数的使用
# 在函数（）括号里边加参数
# def 函数名（变量一，变量二 ）
#             形参一  形参二
def sumnum(num1, num2):
    num3 = num1 + num2
    print("%d+%d=%d" %(num1, num2, num3))
# 定义函数时 ，用来接收数据的形式参数叫做形参
# 调用函数时候，保存数据的实际参数，把数据传递个形参
sumnum(12,2)
# 实参例子
info=12
infon=21
sumnum(info,infon)

def dici():
    """
    函数解释区域
    :return:
    """
    print('woshihanpi')
# 函数调用区域
dici()