"""     open('')
        .read()只能一次性读取文件内容,再去读取时读不到任何内容
            原因是有一个文件指针,打开文件时 ,指针位于文件的开头,使用read方法后,文件指针到了末尾,
            所以再次使用read方法时没有内容
        write()
        .close()"""
ok = open('test', encoding='utf-8')
print(ok)
print(ok.read())
ok.close()
print(type(ok))
