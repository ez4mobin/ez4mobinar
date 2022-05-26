my_list=[49,0,1,-1,-49,-1]
index=0
for item in my_list:
    
    a=abs(item-50)
    item=a
    my_list[index]=item
    index+=1
print(my_list)
print(sorted(my_list))
