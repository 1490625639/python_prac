import os

class Cardstool:
    """名片功能类 """
    def __init__(self):
        """初始化i方法"""
        self.card_list=[]


    @staticmethod
    def menu():
        """
        菜单的界面
        :return:
        """
        print('*' * 30)
        print(' 欢迎使用\n&名片管理系统& ')
        print()
        print(' 1. 新建名片')
        print(' 2. 显示全部')
        print(' 3. 查询名片')
        print()
        print(' 0.退出系统')
        print('*' * 30)



        # 实例方法
    def new_card(self):
        """
        1 确定好数据结构 这里用 列表套字典来存储多个信息
        2 定义全局变量名片列表

          一 获取用户输入
          二 将获取的输入保存到字典中去
          三 将字典添加到列表
          四 打印提示新建名片成功

        当前函数执行新建名片操作
        :return:
        """
        print('执行新建名片的操作')

        card_name = input('请输入你的名字')
        card_age = input('请输入你的年龄')
        card_phone = input('请输入你的手机号')

        card_dic = {
            'name': card_name,
            'age': card_age,
            'phone': card_phone
        }
        self.card_list.append(card_dic)
        print('%s名片信息保存成功' % card_name)
        print('当前名片信息为%s' % self.card_list)
        pass


    # pass是占位符 起到完善语法结构的作用，不输出任何内容
    # 写成实例方法
    def show_all_card(self):
        """
        当前函数执行显示名片操作
        :return:
        """

        if len(self.card_list) == 0:
            print('当前名片中没有数据')
            return
        print('-' * 20)
        print('姓名'.ljust(13), '年龄'.ljust(13), '电话'.ljust(13), sep='\t\t')
        print('-' * 20)
        for temp in self.card_list:
            print(temp.get('name').ljust(13),
                  temp.get('age').ljust(13),
                  temp.get('电话'), sep='\t\t\t')

            # TODO 这是显示名片位置

    # 实例方法
    def search_card(self):
        """
        当前函数执行查询名片的操作
        :return:
        """
        print('执行查询名片的操作')
        find_name = input('请输入你想查找的名字')
        for item in self.card_list:
            if item.get('name') == find_name:
                print('找到了%s的信息了' % find_name)
                print('-' * 20)
                print('姓名'.ljust(13), '年龄'.ljust(13), '电话'.ljust(13), sep='\t\t')
                print('-' * 20)
                print(item.get('name').ljust(12),
                      item.get('age').ljust(12),
                      item.get('phone').ljust(12), sep='\t\t')
                self.deal_card(item)
                break
                # 已经找到人物信息，退出循环
        else:
            print('没有找到你要寻找的信息')


    #     TODO 这是查询名片位置
    def deal_card(self,find_dict):
        while True:
            info_deal_card = input('请输入你想进行的操作1 修改    2   删除 0    返回上一级\n')
            if info_deal_card in ['1', '2', '0']:

                if info_deal_card == '1':
                    print('修改名片')
        # 按住alt键可以多个选择地方插入
                    find_dict['name'] = self.input_info(find_dict.get('name'), '请输入修改后的姓名【不修改直接回车】')
                    find_dict['age'] = self.input_info(find_dict.get('age'), '请输入修改后的年龄【不修改直接回车】')
                    find_dict['phone'] = self.input_info(find_dict.get('phone'), '请输入修改后的电话号【不修改直接回车】')
                    print('-' * 20)
                    print('姓名'.ljust(13), '年龄'.ljust(13), '电话'.ljust(13), sep='\t\t')
                    print('-' * 20)
                    print(find_dict.get('name').ljust(12),
                          find_dict.get('age').ljust(12),
                          find_dict.get('phone').ljust(12),
                          sep='\t\t'
                          )

                elif info_deal_card == '2':
                    print("del_card()")
                    self.card_list.remove(find_dict)
                    print('删除成功')
                else:
                    print("goback()")
                    # 返回上一级直接return     想考究的就向上寻找看在哪个循环里结束，在哪个函数中被调用就知道
                    # TODO 与此同时 快捷键CTRL+SHIFT+ALT+J pycharm 一键选择、修改多个相同变量、符号、值
                    #                  按住ALT+J 可以选中一个变量 再按上下查找下一个
                    # CTRL+/是注释 老是按shift
                    return

                break
            else:
                print('您输入的类型错误，请核对后重新输入')


    def quit_s(self):
        """
        当前函数执行退出系统的操作
        :return:
        """
        print('退出系统')

        pass

    def input_info(self,dict_value, me):
        ok = input(me)
        if len(ok) > 0:

            print('有信息--------%s-------' % ok)
            return ok
        else:
            print('没信息-----%s____' % ok)
            # 返回原来的默认值
            return dict_value
        ret = input_info('shuru1')
        print('%s' % ret)
    def save_data_to_file(self):
        # 利用文件的方式存储名片信息
        data_file=open("card_data.txt","w",encoding="utf-8")
        # 写入文件
        data_file.write(str(self.card_list))
        data_file.close()
    def read_data_from_file(self):
        if os.path.exists("card_data.txt"):
            print("文件存在")
            data_file=open("card_data.txt","r",encoding="utf-8")
            text=data_file.read()
            print(text)
            print("文件写入完毕")
            if len(text)==0:
                print("当前文件内容为空，不能执行eval函数，eval函数无法对空进行操作")
                data_file.close()
                return
            # global card_list
            self.card_list= eval(text)
            data_file.close()