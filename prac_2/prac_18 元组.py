# 元组：修改受到限制，可以存储多个数据
# 定义    元组名=（） 元组里只有一个数据的时候，在最后加上一个，不加，本质上是数据类型转换
tuple = (1, 2, 'zhang', 4, 5)
print(tuple)

print(type(tuple))
# 通过数据查询元组的索引下标 元组，index(数据)
print(tuple.index(5))
# 通过索引下标查询数据  元组名【索引】
print(tuple[2], tuple[3], tuple[4])
'''
元组的增删查改
tuple[1]='彤'
print(tuple[1])  # 会报错item assignment 因为元组的数据不支持修改
元组里面如果有列表 或者 字典 则可以通过修改列表或者字典中的数据来达到修改元组的目的

arr=(13,[1,2])
arr[1][1]=100
print(arr)

元组的常见操作
通过索引查找数据  通过数据查找索引下标    统计某个数据的出现次数    统计元组长度
元组名【下标】     元组名.index（数据）   元组名。count(数据名)      元组名。len/len.元组名
'''
print(tuple[0], tuple.index('zhang'), tuple.count(2), len(tuple))
