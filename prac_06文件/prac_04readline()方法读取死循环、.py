"""readline()函数一次只能读取一行的内容，即便是再次运行也是一行的内容、
想要显示多行 多个print或者用循环"""
file=open('new.txt','r',encoding='utf-8')
# 读取文件
while True:

    textline=file.readline()
    print(textline,end="")
    """end= end：可以设置print打印结束时最后跟的字符形式。
    sep：可以设置print中分隔不同值的形式"""
    if len(textline)==0:
        break
# 关闭文件
file.close()