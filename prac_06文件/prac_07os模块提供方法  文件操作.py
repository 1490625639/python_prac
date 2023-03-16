# os.rename（原来的,现在的）
# os.remove(文件名)   删除指定文件。
import os
os.rename("info.txt","innn.txt")
os.remove("info.txt")
# remove也可填写路径 但是为了防止路径/被转义，需要两个//