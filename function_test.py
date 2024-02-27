def user_info(*args):
    return type(args)

print(user_info(1,2,'   333'))

def info(**kwargs):
    return type(kwargs),kwargs

print(info(list=[1,2,3],list1=1,list2='python'))