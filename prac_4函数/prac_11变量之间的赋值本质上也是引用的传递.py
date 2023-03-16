# 变量之间的引用本质上也是引用的传递
num=122

num2=num
print(id(122))
print(num,id(num))
print(num2,id(num2))
# 结论：变量之间的赋值，本质上是引用的传递
