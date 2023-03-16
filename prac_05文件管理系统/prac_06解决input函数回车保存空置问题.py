# 让input函数在不经过修改时 直接保存的是原来的默认值
def input_info(me):
    ok=input('请输入信息')
    if len(ok)>0:

        print('有信息--------%s-------'%ok)
        return  ok
    else:
        print('没信息-----%s____'%ok)
        # 返回原来的默认值
        return '原来的默认值'
ret=input_info('shuru1')
print(ret)