# 字符串的切片操作
# 字符串【开始的索引：截止的索引：步长切片长度】   切的地方为开头结尾时可省略
name="wangzherngyao"
print(name[name.index('w')::2])
# slice indices must be integers or None or have an __index__ method

# 倒序切片
# 字符串[尾部某索引位置:头部某索引位置:负数步长]
print(name[10:0:-2])

# 字符串的逆序输出
str="nixushuchu"

# print(str.index('w'))
""""str[]为切片方法,其中不知道字符串最后位置,用len()函数获取,"""
print(str[len(str)+1::-1])
print(str[:-13:-1])
print(str[ : : -1])
