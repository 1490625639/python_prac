# 打印三角形 只需要找到行跟列的关系就行 每一行都是跟列相同的     联动关系
# 1
# 11
# 111
# 1111
lie=1
while lie<=5:
    row=1
    while row<=lie :
        print('*',end='')
        row+=1
    print()
    # 换行语句
    lie+=1
print('程序结束')