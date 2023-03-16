# if self.gun == None:
# 身份运算符
class Cat:
    def __init__(self):
        if self.name is None:
            print("输入的为空")

# # 用来比较两个对象的内存地址是否一致  ---  是否是对同一个对象的引用用 is 或者 is not
# python中针对None比较时，建议使用is比较
# cat=Cat()
# 身份运算符，is 用来判断两个数据的引用地址是否相等，相等返回true
#         ==  用来判断两个数据的值是否相等，相等返回true 否则返回false

a=[12]
b=[111]
print(a is b)