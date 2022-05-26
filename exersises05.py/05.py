
n=int(input())
for _ in range(n):
    items=input().split()
    name=items.pop(0)
    a=int(items.pop(0))
    b=int(items.pop(0)) 
    c=int(items.pop(0)) 
    name=[a,b,c]
    #print(sum(name)//len(name))

m=str(input())

if m==name:
    print(sum(m)//len(m))