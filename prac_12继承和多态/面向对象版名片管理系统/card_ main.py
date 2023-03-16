import card_tools
print('\n\n')
class Card_main:
    def __init__(self):
        # 把card_tool模块中的 名片功能类 创建的对象作为当前的属性
        self.ct=card_tools.Cardstool()
        # 先导入包 使用包的函数时候用包名。函数
        self.ct.read_data_from_file()
        # 程序刚启动，就把文件信息加载到程序中去
    def run(self):
        while True:
            self.ct.menu()
            op = input('请输入您的选择：\n')
            if op in ['1', '2', '3']:

                if op == '1':
                    self.ct.new_card()
                elif op == '2':
                    self.ct.show_all_card()
                else:
                    self.ct.search_card()
            elif op == '0':
                # self.ct.quit_s()
                self.ct.save_data_to_file()
                break

            else:
                print('您输入的类型错误，请核对后重新输入')
            print('欢迎下次使用')
            # pycharm并行运行已经打开

if __name__=="__main__":
    # 使用类模板创建对象
    file=Card_main()
    # 程序启动
    file.run()