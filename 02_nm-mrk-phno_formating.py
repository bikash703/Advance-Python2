# def student():
#     return 'The name of the student is {}, His mark {}, and his phone Number is {}'.format('Bikash',420,7978677146)

# s=student()
# print(s)


name=input('Enter Your Name: ')
mark=input('Enter Your Marks: ')
phone=input('Enter Your Phone Number: ')

template = 'The name of the student is {}, His mark {}, and his phone Number is {}'
output=template.format(name,mark,phone)
print(output)