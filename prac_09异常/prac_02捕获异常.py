import os
if os.path.exists("prac_02异常.py"):
    os.rename("prac_02异常.py","prac_02捕获异常.py")


"""异常与捕获异常      

出现异常需要捕获异常么? 
    程序开发人员无法消灭异常,(为网络不稳定)只能靠捕捉异常,并对捕捉到的异常进行处理,(图片加载失败,弹出相对应的提示)
 
注意:只要捕获了异常,无论try部分有没有异常,程序都可以运行起来
                try部分又多个异常,只会捕获第一个异常
格式 try:
        可能会出现异常的代码
   except:
       如果try部分出现异常,执行except部分
       这里可以写异常提示,也可以写对出现异常的处理

"""
try:
    int ("oih")
except:
    print("捕获到了异常")
print("hhhhh")