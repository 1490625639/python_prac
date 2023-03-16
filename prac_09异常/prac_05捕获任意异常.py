# 异常类型很多时候,总不能天天写异常,一次捕捉多个异常是因为人家有相同的处理结果
# 而我们希望这个异常有独自的处理结果     于是用到了exception
try :
   # 函数形参不传调用了任意类型错误,列表索引错误也带哦用任意类型错误
    # a=1/0
    def num(ok):
        print("函数")
    num()
    list[1,2]
    print(list[3])
except( NameError,ZeroDivisionError) : #一次捕获多个异常
    print("已经出现异常了")
except Exception:
    print("捕捉到任意异常.对异常进行处理")

