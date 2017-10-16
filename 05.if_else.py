age = 20
if age >= 18:
	print('adult')
elif age >=6:
	print('teenager')
else:
	print('kid')

birth = input('enter your birth:')
if int(birth) < 2000:
	print('00前')
else:
	print('00后')