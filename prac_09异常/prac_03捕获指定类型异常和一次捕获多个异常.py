import os
if os.path.exists("prac_03异常.py"):
    os.rename("prac_03异常.py","prac_03捕获指定类型异常和一次捕获多个异常.py")
# 知识:报错信息最后一行第一个值就是类型错误提示

# 有点像是ifelse语句,但是ifelse会报错误,但是异常可以继续执行
# 对同一个异常捕获多次,只能捕获第一次
# try部分捕捉到有多个异常,只会捕捉到第一个异常

# 捕获指定异常,在except后面添加异常类型
#     格式:except 异常类型:

try :
    # int1
    # str=we
    a=1/0
except NameError :
    print("nameerror")
except SyntaxError:
    print("出现了SyntaxError异常")
except ZeroDivisionError:
    print("出现了ZeroDivisionError异常")