def add(*args):
	# sumofall = 0
	# for n in args:
	# 	sumofall += n
	# return sumofall
	
	return sum(list(args))


print(add(1, 2, 3, 4, 5, 6, 7))

some_dict = {'aaa':111,'bbb':222}
def calculate(**kwargs):
	for (key, value) in kwargs.items():
		print(key, value)


print(calculate(a=1, b=2))
print(calculate(a=1, b=2))
