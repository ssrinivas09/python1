print('welcome to calculator !')
cnd = input('please press enter if you want to use this tool')
cnd = input('please enter your command (+,-,/,*,%) : ')
print('you have selected : ', cnd)
num1 = int(input('please enter your first number :'))
num2 = int(input('please enter your second number'))
if cnd == '+' :
	print('your answer is : ', num1+num2)
elif cnd == '-':
	print('your answer is : ', num1-num2)
elif cnd == '*':
	print('your answer is : ', num1*num2)
elif cnd == '/':
	print('your answer is : ', num1/num2)
else:
	print('something is wrong')


'''Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators
if cnd == '%' :
	print('your answer is : ', num1%num2)
print('Welcome to Arthematic operaions')
print('you have selected :', cnd)'''

'''print('Welcome to *121*2#')
cnd = input('please select your options')
num1 = 'Arthematic operaions'
print('you have selected :', cnd)
if cnd == '1':
	print('Arthematic operaions')
else:
	print('something went wrong')'''
