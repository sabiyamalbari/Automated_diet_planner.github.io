weight = float(input('Your weight in kilos: ')) # <=== 79
height = float(input('Your height in cm: ')) # <=== 1.75
gender = input('your gender:')
age = int(input('your age:'))
man = ((11 * weight) + (6.25 * height) - (5 * age)+ 5)
women = ((11 * weight) + (6.25 * height) - (5 * age) - 161)
cal_man = man * 1.5
cal_women = women * 1.55
if (gender=='male'):
	 answer =  ',cal_man'
	 print('calories',cal_man)
elif (gender=='female'):
	answer = ',cal_women'
	print('calories',cal_women)
else:
	 answer = 'enter a valid gender'	
	

#calories = 66.4730 + (13.7516 * weight) + (5.0033 * height) - (6.7550 * age)



#man 

#women 

