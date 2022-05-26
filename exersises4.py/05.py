#my_list=[1,2]
#for name in enumerate(my_list):
 #   idx,elem=name
  #  print(name)
#for idx,elem in enumerate(my_list):
#    print(elem,idx)
#for item in range(10):
    #print(item)
#n=int(input())
#my_name=[]
#fo   my_name.append(name)
#print(my_name)r _ in range(n):
 #   name = input()
 
#print(my_name.index(12))
#print(my_name[1])
#n=int(input())
#my_name=([])
#for _ in range(n):
 #   name=input()
  #  my_name.append(name.split())
#print(my_name)




n=int(input())
my_name=[]
for _ in range(n):
    name=input().split()
    my_name.append(name)
print(my_name)
a =my_name[0]
print(a)
#b = int(a[0])
#print(type(b))
my_list=a
for idx,item in enumerate(my_list):
    my_list[idx]=int(item)

for item in my_list:
    print(item,type(item))




