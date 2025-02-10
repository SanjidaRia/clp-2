list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70, 80]
CommonElements = sorted(list(set(list1) & set(list2)))  
print(CommonElements)

