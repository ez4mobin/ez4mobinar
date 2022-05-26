a=int(input()) 
my_number=[]

for _ in range(a):
    number=input().split()
    my_number.append(number)
print(my_number)
a=my_number[0]
print(a)
for idx,item in enumerate(a):
    a[idx]=int(item)
print(a)
print(sum(a))




