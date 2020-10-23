#!usr/bin/env python3

"""calcutation of temperatur in either celcius or fahenriet"""

def temperature(*, f_temp=None, c_temp=None):
	if c_temp is None:
		return {'f_temp': f_temp, 'c_temp': 5*(f_temp - 32)/9}
	elif f_temp is None:
		return {'f_temp': 32+9*c_temp/5, 'c_temp': c_temp}
	else:
		raise TypeError('One of f_temp or c_temp must be provided')
print(temperature(f_temp=20))
