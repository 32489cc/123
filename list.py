mylist=[[1,2],[3,4]]
# print(mylist.index([1,2]))
# mylist[0]=[3,4,5,6,7]
# print(mylist)
list2=['extend',[123,456],222]
mylist.extend(list2)
print(mylist)
newlist=mylist.pop(0)
print(newlist)





re_list=[1,1,1,1,2,3,4]

# print(re_list.count(1))
# re_list.clear()
# print(re_list)
for i in re_list:
    if i!=1:
        print(i)