file_read = open("new.txt", "r", encoding="utf-8")
file_write = open("filebig", "w", encoding="utf-8")
# 打开文件
while True:

    text_line = file_read.readline()
    file_write.write(text_line)
    if len(text_line)==0:
        break

# 操作文件
file_read.close()
file_write.close()


# 关闭文件