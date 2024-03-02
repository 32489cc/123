try:
    num=input('enter a number')


    result=20 / int(num)
except ZeroDivisionError as e:
    print('分母为0')
