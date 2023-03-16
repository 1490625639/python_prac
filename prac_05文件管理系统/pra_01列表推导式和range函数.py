
# range(开始位置，结束位置，步长可正可负)
# 起始位置可以省略 结束位置不能省略
# for x in range  (0,12,1):
#     print(x)

# 轻量级循环创建列表     列表推导式
# 格式： [包含变量的表达式   for  变量 in  range（范围值） ]
a=[x for x in range(1,4)]
print(a)

num=[ b+100 for b in  range(10)]
print(num)
# b以此从range中取一个数 然后放到前边的表达式中 然后再 放进列表里
# e=[c*c for c in  range(3)]
# print(e)

#TODO 列表表达式中可以加条件判断
aa=[f for  f in  range(0,2) if f%2==0]
print(aa)