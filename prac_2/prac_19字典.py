# 存储数据 无序 存储人或事物的详细信息 不能通过索引查询 以键值对方式存储
# 格式：字典名={key1:valuee1,key2:value2,key3:value3}
dict = {'name': '张三', 'sex': '男', 'thing': '吃饭','w':{1,2,}}
print(dict)
# 字典的访问 字典不能通过索引访问 因为无序的
'''print(dict.index[1])'''
# 通过键值进行访问
print(dict['name'], dict['sex'])
# 字典的类型可以是除了列表都可以   []列表 （）元组 {}字典，
dit = {'name': '张三', 18: 'age', True: '真', (1, 2): '元组'}
# # 字典的修改     通过字典名【要修改的键值对】=数值
# newname=input('输入你的名字')
# dict['name']=newname
# print(dict['name'])
# # 字典的增加     类似赋值 字典名【键值对】=数据 注意字典的访问某一数据要加引号
# dict['id']=20181221120
# print(dict['id'])
# # 字典的删除操作       del 字典名【键值对或】   字典名。clear（）函数
# # del dict['id']
# dict.clear()
# print(dict)
# 字典是无序的      例如
dict = {'name': '张三', 'sex': '男', 'thing': '吃饭', 'w': {1, 2, }}
dict1 = {'thing': '吃饭', 'w': {1, 2, }, 'name': '张三', 'sex': '男', }
print(dict == dict1)
# 可以看到输出结果为true
