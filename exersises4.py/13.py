""""
n=int(input())
my_list=[]
for _ in range(n):
    name=input()
    my_list.append(name)
    if my_list[0].isnumeric():
        print("i found anumber")
    else:
        print("nothing")
        
    if my_list[0][0].isupper():
        print("i found upercase string")
    elif my_list[0].islower():
        print("i found lowercase strig")
    else:
        print("nothing")
        
        
    if my_list[0].isalnum():
        print("alphanumeric")
    else:
        print("nothing")
        
    print(my_list[0].count("o"))

    if my_list[0][0].startswith("h"):
       if my_list[0][0].endswith("o"): 
        print("i found hello")
    else:
        print("nothing")
"""
"""""
my_list=["ali","mobin","asghar"]
flag = False
for name in my_list:
    if name == "ali":
        print("i found ali")
        flag=True
        break
if not flag:
    print("didnt find ali")

"""
""""
my_list=["ali","mobin","asghar"]
for name in my_list:
    if name == "ali":
        print("i found ali")
else:
    print("didnt find ali")
"""
"""""
char_count=[0]*26
for character in input():
    idx=ord(character)-ord("a")
    char_count[idx]+=1
for idx,value in enumerate(char_count):
    character=chr(idx+ord("a"))
    if value:
        print(f"{character}: {value}")
"""
""""
my_list=[1,2,3,4,5]
n=int(input())
for _ in range(n):
    item=my_list.pop()
    my_list.insert(0,item)
print(my_list)
"""
""""
my_list=[1,2,3,4,5]
n=int(input())
for _ in range(n):
    item=my_list.pop()
    my_list.append(item)
print(my_list)
"""
""""
my_list=[1,2,3,4,5]
n=int(input())
print(my_list[:n]+my_list[n:])
"""















    