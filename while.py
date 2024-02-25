# i=1
# result=0
# while i<=100:
#
#     result += i
#     i += 1
# print(result)

# i=0
# while i<100:
#     print('今天是第%d天，准备跟小美表白' % i)
#     j=1
#     while j<=10:
#         print('送给小妹第%d只玫瑰花' % j)
#         j+=1
#     print('小妹我喜欢ni')
#     i+=1
# print('坚持到第%d天表白成功'% i)


i=1
while i<=9:
    j=1
    while j<=i:
        print(f'{j}*{i}={j*i} ',end='')
        j+=1
    i+=1
    print('')