# os.rename（原来的,现在的）
# os.remove(文件名)
import os
import shutil
# os.listdir(目录名)目录列表   查看文件名和目录名，以列表的形式展开，默认为当前目录
# print(os.listdir("."))
#os.mkdir("目录名或者绝对路径目录名"))  创建一个目录
# print(os.mkdir("hello"))
# 删除文件夹目录   rmdir(名称/路径)只能删除空目录
# os.remove("hello")
# 使用shutil.rmtree可以删除非空目录
# shutil.rmtree('hello')

# os.mkdir("python")
# 获取当前目录getdir()
print(os.getcwd())
# # chdir(目标目录)   修改工作目录
# print(os.chdir("python"))
# print(os.getcwd())

# path.isdir(文件夹路径) 判断是不是一个文件夹 结果以布尔类型返回
print(os.path.isdir("python"))
# path.isfile("文件名或者目录名")判断是否是文件布尔返回
print(os.path.isfile("test"))
# path.exists("文件名或目录名")判断文件是否存在
print(os.path.exists("test"))





# alt+space  出小窗 CTRL+字母 进行操作