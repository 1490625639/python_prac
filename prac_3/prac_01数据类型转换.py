# 数据类型转换  数据类型（数据）
# 总结：int(x)   将x转为int整型
#     floa(x)     将x转为float型
#     str(x)      将x转为字符串类型
#     list(x)     将x转为列表类型
#     tuple(x)    将x转为元组
print(int(22.2))
print(float(23))
nihao={'字典':1,'zifu':2}
x=(23,2)
print(str(nihao))
print(str(x))
n=23.3
print(str(n))
# pycharm自带交互式运行方式python console
# 字符串转成列表
str='hellp'
print(list(str))
print(type(list(str)))
# 列表转成字符串、不能用str进行转，因为有括号 用”“。join
print(''.join(list(str)))
# 字典转成列表        只能把键值对转成列表
dic={'name':'张彤','gender':'男','age':21}
print(list(dic))
print(type(list(dic)))
# tuple(x)    把序列数x转成元组
x='2323'
print(tuple(x))
# 列表转成元组
m=[12,23]
print(tuple(m))