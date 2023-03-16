list=[11,22,33,44,55,66]
# 使用del删除列表数据     del 列表名[索引]
del list[0]
# 使用remove删除指定的数据 列表.remove(数据)
list.remove(66)
# 列表.pop  弹出末尾数据
# 列表.pop(索引)弹出指定索引的数据
list.pop(0)
# 清空整个列表数据  列表.clear()
list.clear()
print(list)