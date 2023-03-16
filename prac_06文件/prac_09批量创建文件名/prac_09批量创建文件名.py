import os
import shutil
# 先创建
def creat_files():
    if os.path.exists('./files'):
        shutil.rmtree('./files')
    # 再修改目录
    os.mkdir("./files")
    os.chdir("./files")
    # 然后创建文件
    for i in range(1,21):
        file=open("new%d.txt"% i,"w",encoding="utf-8")
        # file = os.open("new"+str(i)+".txt" , "w", encoding="utf-8")
        file.write("wefwefwfw")
        print("%d"%i)
        file.close()
def change_files_name():
    print("查看当前文件目录",os.getcwd())
    path= "D:\\python_prac\\prac_06文件\\prac_09批量创建文件名\\files"

    if os.getcwd()!=path:
        os.chdir(path)
    print("当前的目录修改后",os.getcwd())
    files_name=os.listdir()
    # print(files_name)
    for name in files_name:
        os.rename(name,"rename"+name)




creat_files()

change_files_name()