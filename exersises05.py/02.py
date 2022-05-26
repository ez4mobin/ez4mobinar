n=int(input())
my_list=[]
for _ in range(n):
    name=input().split(" ")
    my_list.extend(name)
    if name=="asghar":
        print("i found asghar")
    else:
        print("where is asghar")
    print(my_list)