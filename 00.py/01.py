"""
a = int(input("input:"))
b = int(input("input:"))
print("input type a:", type(a))
print("input type b:", type(b))
c = b * a
print("result:",c)
print("result type:",type(c))
"""
char_counts=[0]*26
for character in input():
    idx=ord(character)-ord("a")
    char_counts[idx]+=1

for idx,value in enumerate(char_counts):
    character=chr(idx+ord("a"))
    if value:
        print(f"{character}:,{value}")