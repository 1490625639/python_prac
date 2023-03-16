# 吃五个苹果 吃到第三个苹果就吃饱了
# break   循环到此 终止循环 退出程序
apple=1
while apple<=5:

    apple+=1
    if apple==3 :
        print('现在吃的是第%d个苹果'%apple)
        print("我已经吃饱了，我不想吃苹果了")
        break
print('循环结束')