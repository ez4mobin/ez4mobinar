n=int(input())
uri=[]
for _ in range(n):
    ur=input().split(" ")
    uri.append(ur)

print(uri)
print('|'.join(uri[0]))

