my_list=list(map(int,input().split()))
while True:
    i=input()
    a=int(input())
    if i=="append":
        my_list.append(a)
        print(my_list)
    elif i=="reverse":
        my_list.reverse() #a==0
        print(my_list)
    elif i=="remove":
        my_list.remove(a)
        print(my_list)
    elif i=="sort":
        my_list.sort() #a==0
        print(my_list)
    elif i=="pop":
        while True:
            idx=int(input())
            my_list.pop(idx) #a=0
            print(my_list)
            break
    elif i=="insert":
        while True:
            idx=int(input())
            my_list.insert(idx,a)
            print(my_list)
            break
    elif i=="extend":
        my_list_extend=list(map(int,input().split()))
        for items in my_list_extend:
            my_list.append(items) #a=0
        print(my_list)
        break 
    elif i=="clear":
        my_list.clear() #a=0
        print(my_list)
    elif i=="len":
        len(my_list) #a=0
        print(len(my_list))
    elif i=="count":
        while True:
            sub=int(input())
            my_list.count(sub) #a=0
            print(my_list.count(sub))
    elif i=="index":
        while True:
            value=int(input()) #a=0
            start=int(input())
            stop=int(input())
            my_list.index(value,start,stop)
            print(my_list.index(value,start,stop))
            break
    elif i=="range":
        while True:
            start=int(input()) #a=0
            stop=int(input())
            step=int(input())
            print(my_list[start:stop:step])
            break
    elif i=="exit":
        break  #a=0
            

"""
n=input()
my_list=[]
for character in n:
    for item in my_list:
        if item[0]==character:
            item[1]+=1
            break
        else:
            my_list.append([character,1])

print(my_list)

#for char,value in my_list:
#    print(f"{char}:{value}")
"""
"""
n=int(input())
revers_n=0
while True:
    reminder=n % 10
    revers_n=revers_n*10+reminder
    n=n//10
    print(n)
    if n==0:
        print(revers_n)
        break
"""
"""
n=input()
curent_pos=0
jump_count=0
while True:
    next_cloud_pos_candidate=curent_pos+2
    if next_cloud_pos_candidate<len(n) and n[next_cloud_pos_candidate]=="1":
        curent_pos+=2
        jump_count+=1
    else:
        curent_pos+=1
        jump_count+=1
    if curent_pos==len(n)-1:
        print(jump_count)
        break
"""
"""
my_list=[1,2,3,4]
def func(item):
    return item*2

print(list(map(func,my_list)))
"""
"""
my_list=["1","2","3","4"]
print(list(map(int,my_list)))
"""
"""
my_list=[1,2,3,4,5]
print(list(map(lambda a:a*2,my_list)))
func=lambda x**2
print(func(2,6))
"""
"""
def is_even(item):
    if item%2==0:
       return True
    else:
        return False

my_list=[1,2,3,4]
print(list(filter(is_even,map(int,my_list))))
"""
"""
num=int(input())
print("asghar" if num<10 else None)
"""
"""
print(list(filter(lambda x:x%2==0,map(int,input().split()))))
print(list(filter(lambda x: not x%2==0,map(int,input().split()))))
"""








































