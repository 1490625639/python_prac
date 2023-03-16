# return 返回值 1  提前终止函数的运行
#              2  把函数的结果 返回到 源程序中函数调用的地方
# 函数没有返回值 ，但是函数调用的地方偏偏需要返回值，会返回一个none

def sumnum(num1, num2):
    num3 = num1 + num2
    print("%d+%d=%d" %(num1, num2, num3))
    return num3
info=12
infon=21

# return返回值返回到了这里 赋给了res
res=sumnum(info,infon)
print(res)


