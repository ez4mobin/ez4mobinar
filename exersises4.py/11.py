#n=int(input())
#my_list=[]
#for _ in range(n):
  #  name=input()
 #   my_list.append(name)
#print(my_list)
#if my_list
"""
n=int(input())
student_score=[]
for _ in range(n):
    score=int(input())
    if score >20 or score<0:
        print("wrong_inpur")
    student_score.append(score)

student_sum=0
for score in student_score:
    student_sum+=score

print(student_sum/n)
"""
"""
n=int(input())
student_score=[]
for _ in range(n):
    score=int(input())
    
    student_score.append(score)
print(student_score)
print(max(student_score))
"""
"""
n=int(input())
student_score=[]
for _ in range(n):
    score=int(input())
    
    student_score.append(score)

student_score_new=[]
for score in student_score:
    if 17<= score <= 20:
        print("a")
    elif 14 <= score < 17:
        print("b")
    elif 11<= score <14:
        print("c")
    elif 8<= score <11:
        print("d")
    else:
        print("i will call ur daddy")
    student_score_new.append(score)
print(student_score_new)
"""
"""
n=int(input())
student_score=[]
for _ in range(n):
    score=int(input())
    student_score.append(score)

max_score,befor_max_score=0,0
for score in student_score:
    if score > max_score:
        befor_max_score=max_score
        max_score=score

print(befor_max_score)
"""
""""
n=int(input())
student_score=[]
for _ in range(n):
    score=int(input())
    student_score.append(score)
    if score<10:
        student_score.remove(score)

print(student_score)
"""
n=int(input())
student_score=[]
for _ in range(n):
    score=int(input())
    student_score.append(score)

student_score.sort()
a=len(student_score)
print(student_score[a-2])


