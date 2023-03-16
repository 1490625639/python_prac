"""我们希望,在有了异常的捕获后,对于Exception中的捕获任意异常,
有时候还想看到,具体是因为什么类型的异常被捕捉到的 想调查出到底什么罪名
于是用到了 as"""
# 给异常类型起一个别名  ,然后把这个别名输出(别名中记录异常的错误信息)
open("prac_08异常的传递.py","w",encoding="utf-8")
try :
   # 函数形参不传调用了任意类型错误,列表索引错误也带哦用任意类型错误

    def num(ok):
        print("函数")
    num()
    list[1,2]
    print(list[3])
except( NameError,ZeroDivisionError  ) as oj : #一次捕获多个异常
    print("已经出现异常了",oj)
except Exception as hhh:
    print("捕捉到任意异常.对异常进行处理,这是属于异常",hhh)

