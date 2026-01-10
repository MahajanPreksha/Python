li1 = [1, 5, 5, 10]
li2 = [3, 4, 5, 5, 10]
li3 = [5, 5, 10, 20]

#Typecasting the lists to sets
set1 = set(li1)
set2 = set(li2)
set3 = set(li3)

#Finding common elements using intersection
s1s2 = set1.intersection(set2)
final_set = s1s2.intersection(set3)

#Typecasting the final set back to list
final_list = list(final_set)
print(final_list)

#Output: [10, 5]