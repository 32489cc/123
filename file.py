#打开文件 open（）
f=open('/Users/toki32489/Documents/index_副本.html','r',encoding="utf-8")
#read（）读取函数
print(f.read())
f.close()
with open('/Users/toki32489/Documents/index_副本.html','r',encoding="utf-8") as f:
    content=f.read()
    count=content.count('<div')
    print(count)