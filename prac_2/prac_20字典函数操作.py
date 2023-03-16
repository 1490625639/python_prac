dict = {'删除': 1, '增加': 2, '修改': 6, }
# 查询字典长度 len.字典名
print(len(dict))

# 获取字典的键视图 字典名。key()
print(dict.keys())
# 获取字典的值视图  zz字典名。values()
print(dict.values())
# 获取字典的元素视图 字典名。items()    item y元素
print(dict.items())
# 字典的遍历     for循环使用     key：键   values:值    items:元素
for key in dict.keys():
    print(key)
for va in dict.values():
    print(va)
for yuansu in dict.items():
    print(yuansu)
# for jianzhidui in dict.items():
#     print(key.values)
