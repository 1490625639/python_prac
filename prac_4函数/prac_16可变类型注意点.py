# 不可变类型 整型浮点 字符串 元组
# 可变 列表 字典
num=12
print(num,id(num))
num=122
print(num,id(num))

# 思考一下，num为整型，为不可变类型（数据空间不可变，只能开辟新空间）
list=[12,23]
print(list,id(list))
list=[23,22]
print(list,id(list))
# 思考一下，列表不是可变类型么（地址空间不用开辟空间就能改变数据）为什么这里两个的地址空间发生了改变呢
# 因为这个是赋值

# 无论是可变还是不可变数据类型 通过赋值语句 都会修改变量的引用地址
"""查看一个变量是否是可变数据类型，通过方法的方式修改，而不是    赋值语句    
"""
zifu='hello'
print(zifu,id(zifu))
newzifu=zifu.upper()
print(newzifu,id(newzifu))

# 可以看到，字符串不可变数据类型，数据改变后开辟了新的内存空间
# 可变类型列表 字典  内存不变的情况下数据可改变
lis=[23,233,5]
print(lis,id(lis))
lis.remove(5)
print(lis,id(lis))
# 可以看到 内存空间固定的情况下通过方法可以做到数据改变

# 字典的键只能使用不可变数据类型 整型浮点元组字符串