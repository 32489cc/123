f=open('/Users/toki32489/Documents/price.txt','w',encoding="UTF-8")
f.write('测试文本')
f.close()

f=open('/Users/toki32489/Documents/price.txt','a',encoding="UTF-8")
f.write('\n')
f.write('\n\r追加文本')
f.close()