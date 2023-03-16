"""# if  elif else 相当与if else if
格式为： if 条件：
    elif 条件二：
    elif 条件三：
    else """
score=int(input('请输入成绩'))
if score<30:
    print('成绩为差劲')
elif score>30and score<60:
    print('成绩不及格')
elif score>60and score<80:
    print('成绩及格了')
else :
    print('成绩优秀')