num=100
# tab 键可以和enter一样选中
# 熟练运用shift+enter快速换行ctrl+end快速回到末尾
print(num)
print(id(num))
print('-----------')
# 对变量重新赋值   结论：修改的是变量中引用的数据的内存地址
num=200
print(num)
print(id(num))
print('程序结束')
# 一开始把100的地址赋给了num 后来把200的地址赋给了num  100的地址不用了被回收
"""
打英文大写字母时，不用来回切换capsLOOK 按住SHIFT可以进行切换
大写状态下 按住shift输入的是小写英文 
小写状态下 按住SHIFT输入的是大写英文"""