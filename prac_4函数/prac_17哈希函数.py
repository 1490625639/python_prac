# 哈希查找 楚留余数法  直接定制法
print(hash(12))
print(hash(True))
print(hash((23,4,)))
print(hash(23.3))
print(hash('we'))
# 下边的是列表 报错  File "D:/python_prac/prac_4函数/prac_17哈希函数.py", line 8, in <module>
#     print(hash([1, 2, ]))
# TypeError: unhashable type: 'list'


# 因为hash这能接收不可变数据类型
# 而列表是可变数据类型  字典中因为value(任意类型)可以有列表，且也是可变类型，所以hash对列表字典不能用
# 字典的键是通过哈希函数运算得到的，所以字典的键只能是不可变类型 整浮字元不二
print(hash([1, 2, ]))