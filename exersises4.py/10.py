n=int(input())
my_fruit=[]
for _ in range(n):
    name=input().split(" ")
    my_fruit.extend(name)
print(my_fruit)