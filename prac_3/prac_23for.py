"""
利用for循环来进行四大容器的遍历 字符串列表【】元（）组字典{}
格式： for 临时变量 in 容器：
     对临时变量的处理
特点：临时变量从容器中一个个取到
    """
list = [12, 3, 4, 32, 'hello', True]
for temp in list:
    # 使用for遍历列表
    print(temp)
tuple = (23, 21, 'hhh')
# 使用for循环遍历元组     输出英文时 按住shiFT可以打大写 同时可以打英文
for on in tuple:
    print(on)
str = 'zheshiyigezifuchuan'
for i in str:
    print(i)
    # 可以试试在i后加一个，end=“”试试看
# 使用for循环遍历字符串
# 使用for循环遍历字典
dic = {'name': 'zhh', 'age': 22}
for o in dic:
    print(o)
    # 只能获取键值对 不能获取values 可以通过访问键值对获取value  或者用字典名。get(k)
    print(o, dic[o])
    print(o, dic.get(o))
