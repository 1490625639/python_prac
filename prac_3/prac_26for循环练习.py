list=[{'name':'张三','sex':'男','age':'22'},
{'name':'李四','sex':'男','age':'22'},
{'name':'赵一','sex':'男','age':'22'},
{'name':'王五','sex':'男','age':'22'},
      ]
find='赵一'
for temp in list:
    # 获取字典的value信息 用字典名。get方法
    if temp.get('name')==find:
        print('恭喜你 找到了')
        print(temp.get('name',temp.get('sex')))
        break
else:
    print("不好意思没有这个人")