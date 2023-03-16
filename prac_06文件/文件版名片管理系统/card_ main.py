import card_tools


print('\n\n')

# 先导入包 使用包的函数时候用包名。函数
card_tools.read_data_from_file()
# 程序刚启动，就把文件信息加载到程序中去
def main():
    while True:
        card_tools.menu()
        op = input('请输入您的选择：\n')
        if op in ['1', '2', '3']:

            if op == '1':
                card_tools.new_card()
            elif op == '2':
                card_tools.show_all_card()
            else:
                card_tools.search_card()
        elif op == '0':
            # card_tools.quit_s()
            card_tools.save_data_to_file()
            break

        else:
            print('您输入的类型错误，请核对后重新输入')
        print('欢迎下次使用')
        # pycharm并行运行已经打开
main()