a=int(input('enter sides='))
b=int(input('enter sides='))
c=int(input('enter sides='))
if((a**2)+(b**2)==(c**2) or(b**2)+(c**2)==(a**2) or(c**2)+(a**2)==(b**2)):
	print('triangle is right angled')
else:
	print('triangle but not right angled')
