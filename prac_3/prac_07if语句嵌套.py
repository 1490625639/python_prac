# if语句嵌套上火车
hasticket=True
knifelen=int (input('输入你的刀的长度'))
if hasticket:
    # 布尔类型可以为空 为空时判断是否为真
    print('有车票')
    if knifelen<=20:
        print('可以上车')
    else:
        print('刀的长度超出规定，你不能上车')
else:
    print('没有车票了 你走吧')