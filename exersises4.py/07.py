
n=int(input())
my_name=[]
for _ in range(n):
    name=input()
    my_name.append(name)
print(my_name)
print("#".join(my_name))