"""不可变数据类型
解释：原内存空间的数据不允许修改
    如果想要修改数据，只能开辟新的内存空间，让变量重新引用新内存空间的地址
分类：int float bool str tuple

            可变与不可变的最主要的区分就是看在内存空间不变的情况下数据可不可变
"""
num=12
print("这个数的值为%s,%s"%(num,id(num)))
num+=1
print("第二个数的值为%s,%s"%(num,id(num)))
# 由此可见 两个同样都是num但是他们的地址是不一样的，说明数据在改变后，地址空间改变，只能新开辟内存空间

# 字符串类型
str='hello'
print(str,id(str))
str+='nohello'
print("字符串改变后的数据和空间为\n%s,%s"%(str,id(str)))

"""
从这里可以看出 字符串改变后 内存地址空间也不一样 说明无法做到改变数据的同时 数据空间也不变
此为不可变类型
"""
# 元组可以拼接
tuple=(12,32)
print(id(tuple))
tuple+=(22,)
print(id(tuple))