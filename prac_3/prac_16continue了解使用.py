# 五个苹果 吃到第三个苹果时吃到大虫子 不吃了 吃后面的
# 1 continue 到这个地方跳出这一次循环接着执行接下来的循环
# 总结:修改循环变量放在continue前边 3continue只能作用于当前一层while循环
apple=0
while apple<5 :
    apple+=1
    """修改循环变量这一步建议放到continue前面
    否则容易死循环
    比如0 到1到2到3 然后一直打印3 
    因为没有修改循环变量进行控制"""
    if apple==3:
        print('我吃出来一个大虫子，不想吃了，这是第%d个苹果'%apple)
        continue
    print('现在吃的是第%d个苹果' % apple)
print('循环结束')