""" 可变数据类型   修改数据不用修改数据空间   比如：列表 字典 [] {}

    不可变数据类型 修改数据必须修改数据空间    分类：int float bool str tuple """
#
list=[12,34]
print(list,id(list))
list +=[78]
# 对列表使用+=语句 等价于列表。extend（）
print(list,id(list))
list.append(77,)
print(list,id(list))

dic={'neme':'张三','age':22}
print(dic,id(dic))
dic.update({'sex':'男'})
print(dic,id(dic))

# 通过以上对列表和字典的研究分析发现，    地址不变内容可变  没有开辟新的内存空间
# 即便是对他们的数据进行了修改后，他们的内存空间还是老样子没有改变