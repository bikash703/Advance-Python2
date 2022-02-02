from functools import reduce
# def maximum(a,b):
#     return max(a,b)

l=[6,7,45,89,6,67,90,54,32,3,50]
# val=reduce(maximum,l)
# print(val)

#shortcut formula
val=reduce(lambda a,b: max(a,b) , l)
print(val)