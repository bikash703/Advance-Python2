def square(num):
    return num*num

l=[2,6,9,5]
# method1
l1=[]
for i in l:
    l1.append(square(i))
print(l1)
# method2

print(list(map(square,l)))