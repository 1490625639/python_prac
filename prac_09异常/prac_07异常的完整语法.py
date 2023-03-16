"""try:
    可能错误的语句
except   错误类型一 as st:

    当出现异常时.想要执行的语句

except (错误类型二, 错误类型三) as something:
    一次捕获多种异常

except Exception as st:
    捕获任意异常
else:
    没有异常时, 该药执行的语句
finally:
    最终要执行的语句
    无论是否有异常, 都会执行的语句"""

# 应用场景,再打开文件像文件写入数据时程序崩溃
# 此时可以在finally部分添加关闭文件资源的操作,避免系统资源浪费

open("prac_08异常的传递.py","w","utf-8")

try :
    file=open("new.txt",'w',encoding="utf-8")
    file.write([12,2341,453242])#列表不能写入文件,这里是一个异常

except NameError:
    print("捕捉`名字错误异常")
except Exception:
    print("ren")
else:
    print()
finally:
    print("在finally中无论是否有异常,都会执行")
    print("--0------")
    file.close()
    print("--1----")
