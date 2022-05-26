"""
n=int(input())
remider=n%9
if remider==0:
    print(9)
else:
    print(remider)
    # other way
"""
"""
n=input()
while True:
    s=0
    for char in n:
        s+=int(char)
    n=str(s)
    if s<10:
       print(s)
    break
#----------------------------------------------------------
"""""
""""
n=int(input())
string="absdefghijklmnopqrstuvwxyz"
max_width=4*n-3
for idx in range(n):
    char=string[n-(idx+1):n]
    right_side="-".join(char)
    left_side=right_side[-1:0:-1]
    a=right_side+left_side
    print(a.center(max_width))

for idx in range(n-2,-1,-1):
    char=string[n-(idx+1):n]
    right_side="-".join(char)
    left_side=right_side[-1:0:-1]
    a=right_side+left_side
    print(a.center(max_width))
    """
my_list=input().split()
flag=False
for name in my_list:
    if name =="asghar":
        print("error")
        flag=True
        break
    if not flag:
        print("hello name")
        

   


