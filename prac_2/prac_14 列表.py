# 跟数组一样,换了个名字而已 存放多个数据的高级容器
list = ['张彤', 22, 201812211120, "软件工程1841"]
print(list[1])
print(list.index('张彤'))
print(len(list))

# print(list.count(22))
"""列表的增删改查"""
# 列表的快速格式化 CTRL+alt+l   对有曲线的都可以进行
lis = [1, 2, 3, 4, 5, 9]
lio = [22, 33]
# 列表的增删查改
# 增加 insert(索引,数据)    append(数据)直接插入表尾   extend合并两个表
lis.insert(6, 16)
lis.append(66)
"""在列表中插入一个小列表"""
# appead:附加的
lis.append(lio)
print(lis)
# 把lit列表的数据追加到lin列表中去
lin = [88, 99,]
lit=[11]
print(lin.extend([11]))
