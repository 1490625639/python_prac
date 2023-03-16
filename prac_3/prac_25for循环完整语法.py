# # for else语句
# 格式：for 临时变量 in 容器：
#     对临时变量的处理
#     满足条件时 对临时变量进行处理
#     else ：
#         在for循环中没有执行BREAK语句 for循环遍历完后 一定执行else语句
list=[10,23,49,22]
find=23
for i in list:
    if i==find:
        print('找到了你要的数据%d'%find)
        break
else:
    print('yijing已经执行完了 没有找到啊')