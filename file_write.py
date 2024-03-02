with open('/Users/toki32489/Documents/price.html','w',encoding="utf-8") as f:
    f.write('<htmk>head</html>')
    #write是把内容写到内存中 flush是把内存的内容写到文件中
    #close函数会自动执行flush
    #w模式如果不存在文件会新建文件 如果存在文件则会清空原有的文件内容重新写入
    #f.flush()
    f.close()