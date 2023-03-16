"""1 'r'只读      文件不存在会报错    文件存在,从开头读取
    2 'w'只写     文件不存在新建      文件存在,覆盖
    3 'a'追加     文件不存在新建      文件存在,追加补充"""
# 频繁的移动文件指针会降低文件的读写效率  所以一般使用只读只写
# 打开文件
file=open('new.txt','r',encoding='utf-8')
# 读取文件
text=file.read()
print(text)
# 关闭文件
file.close()
"""# 打开文件只写方式     文件不存在新建      文件存在,覆盖
file = open('info.txt', 'w', encoding='utf-8')
# 读取文件
text = file.write('存在测试 结果覆盖')
print(text)

# 关闭文件
file.close()
"""



"""# 打开文件只写方式     文件不存在新建      文件存在,覆盖
file = open('info.txt', 'w', encoding='utf-8')
# 读取文件
text = file.write('存在测试 结果覆盖')
print(text)

# 关闭文件
file.close()
"""




"""# 打开文件只写方式     文件不存在新建      文件存在,追加补充
file = open('info.txt', 'a', encoding='utf-8')
# 读取文件
text = file.write('追加测试')
print(text)

# 关闭文件
file.close()

"""


# # 打开文件只写方式
# file = open('info.txt', 'a', encoding='utf-8')
# # 读取文件
# list=[12,23,11]
# # TODO write只能写入字符串,不能写入列表
# #       write() argument must be str, not list
# #       write() 方法有返回值,返回值是写入字符串的长度
# text = file.write(list)
# print(text)
#
# # 关闭文件
# file.close()
