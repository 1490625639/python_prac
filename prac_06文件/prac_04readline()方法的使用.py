# file=open("new.txt","r",encoding="utf-8")
# line_text=file.readline()
# print('----%s--------------'%line_text)
# file.close()
# 打开文件
file=open('new.txt','r',encoding='utf-8')
# 读取文件
textline=file.readline()
print(textline)
"""一、read方法

　　特点是：读取整个文件，将文件内容放到一个字符串变量中。

　　劣势是：如果文件非常大，尤其是大于内存时，无法使用read()方法。

    二、readline方法

　　特点：readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存

　　缺点：比readlines慢得多

    三、readlines方法

　　特点：一次性读取整个文件；自动将文件内容分析成一个行的列表。    
"""



#
# textline=file.readlines()
# print(textline)
# 关闭文件
file.close()