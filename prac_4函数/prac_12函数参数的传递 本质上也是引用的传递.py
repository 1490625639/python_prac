# 定义函数
# 调用函数
def onn(one, two):
    ret = one + two
    print(id(one))
    # 函数引用后的地址
    return ret


print(onn(12, 3))
# 本质上一直所使用的还是地址 使用的是12 跟3的地址
print(id(12), end='分割')
print('------------')

q = input("liagngeshu")
w = input()
print(q, w)
