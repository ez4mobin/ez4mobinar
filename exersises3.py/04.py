name=str(input())
print("----------------------")
math=int(input())
if math<12:
    print("failed")
elif math>=12:
    print("passed") 
print("----------------------")
science=int(input())
if science<12:
    print("failed")
elif science>=12:
    print("passed")
print("----------------------")
art=int(input())
if art<12:
    print("failed")
elif art>=12:
    print("passed")
print("----------------------")
PE=int(input())
if PE<12:
    print("failed")
elif PE>=12:
    print("passed")
print("----------------------")
literature=int(input())
if literature<12:
    print("failed")
elif literature>=12:
    print("passed")
print("----------------------")
print(f"scores[{math},{science},{art},{PE},{literature}]")