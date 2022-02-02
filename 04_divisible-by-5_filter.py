# def divisible(num):
#     if num%5==0:
#         return True
#     else:
#         return False

l1=[7,4,5,20,10,60]
# print(list(filter(divisible,l1)))

#shortcut formula of lambda function
# print(list(filter(lambda a: a%5==0 ,l1)))

a=filter(lambda a: a%5==0 ,l1)#another type
print(list(a))
