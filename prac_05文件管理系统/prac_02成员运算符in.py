# # in用来判断一个数据是否为数据容器的成员
# 格式为 数据 in 容器
# 常和if语句使用
list=[12, 23, 5, 56,]
print(12 in list)
str='iwenfh'
print('i' in str)
# 有in 就有not in
# 用in成员运算符时候 可以判断字典，但是只能判断字典的key
dic={'明星':'里hi和','性别':'男'}
print('性别'in dic)
print('hi'in dic)
print('明星'in dic)