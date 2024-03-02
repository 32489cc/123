num=input('enter a number:')

def main(*args):

    try:
        if len(args)==2:
            result=fun(*args)
        return result
    except ZeroDivisionError as e:
        print('分母为0')
        return None
def fun(a,b):
     result= a/b
     return result


result=main(100,int(num))
print(result)