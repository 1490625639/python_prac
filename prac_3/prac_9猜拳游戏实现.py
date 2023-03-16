import random

computer = random.randint(1, 3)
print("电脑选择为",computer)
player = int(input("请输入你的选择 1  石头 2 剪刀 3 布\n"))
# 因为获取的输入类型是字符串类型 所以二者相等的情况存在问题 需要转成数字
print("你的选择为\n" , player)
# 这里又犯了错误 一开始还是使用了+来连接 实际上应当选择逗号，
if computer == player:
    print('游戏的结果是平局')
elif (computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
    print('你输了')
else:
    print('游戏的结果为你赢了')

# 使用+连接时，只能将字符串与字符串连接，不能和int型连接。
# 需要将x强制转换成str型。    一般使用，进行连接