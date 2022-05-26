n=int(input())
max_width=2*n-1
for idx in range(n):
    print(("*"*(2*idx+1)).center(max_width))

for idx in range(n):
    print(("*"*(-2*idx+(2*n-3))).center(max_width))