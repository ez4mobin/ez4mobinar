fruits=['orange','banana','apricot','cucumber','watermelon','orange']
print(fruits.count("orange"))
#['orange','apricot',watermelon']
print(fruits[0::2])
#['banana',cucumber',orange]
print(fruits[1::2])
fruits.insert(2,"peach")
print(fruits)
fruits.remove("watermelon")
print(fruits)
fruits.append("cherry")
print(fruits)
fruits.remove("cucumber")
fruits.insert(4,"pineapple")
print(fruits)
fruits.remove("banana")
print(fruits)

