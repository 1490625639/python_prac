list = [11, 22, 33, 44]
# 列表的修改   直接修改指定位置  列表[索引]=修改后的数据
list[1]=34
print(list)

# 查找数据  一利用索引查找 列表名[索引]
print(list[0])
# 查找索引 利用数据查找 列表名.index(数据)
print(list.index(11))