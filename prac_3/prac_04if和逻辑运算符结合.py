# and or not 和if的结合使用
"""""
报错原因：字符串（str）未转化便和整数（int）进行比较
Python报错：TypeError: ‘<’ not supported between instances of ‘str’ and ‘int’
 
 if条件语句经常搭配逻辑运算符一起使用
 if 空列表【】空元组（）空字典{}空字符串 都是条件不成立的意思

"""""
age=23
if age>=120and age<=0 :
    print('不符合')
else :
    print('符合规定')
score=input('请输入你的成绩')
cscore=input('请输入第二门成绩')
score=int(score)
cscore=int(cscore)
if score > 60 or cscore > 60:
    print('成绩合格')
else :
    print('成绩不合格')