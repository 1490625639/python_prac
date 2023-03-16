file_read = open("new.txt", "r", encoding="utf-8")
file_write = open("filesmall", "w", encoding="utf-8")

text = file_read.read()
file_write.write(text)
#
# file_read.read()
# file_write.write()
print(text)
file_read.close()
file_write.close()
