"""try:感觉要出问题的代码
except (多个异常类型1,多个异常类型用2,隔开4):
                      作用:  适用于对异常类型1,异常类型2,异常类型3有相同的处理结果

     对异常的处理结果"""





try :
    # int1
    str=we
    a=1/0
except( NameError,ZeroDivisionError) : #一次捕获多个异常
    print("已经出现异常了")
except SyntaxError:
    print("出现了SyntaxError异常")


    """
    Tips:
    要选择多个文本片段，请按住Shift + Alt并在文本上拖动鼠标
    如果修改了活动模板，它将被标记为蓝色。
    要将模板还原为其原始状态，请右键单击该模板，然后从关联菜单中选择“还原默认值”"""
