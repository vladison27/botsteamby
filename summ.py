def summ(idd):

	file = open(F"{idd}.txt")
	file_mass = []

	for i in file.readlines():
		file_mass.append(i)

	del(file_mass[0])

	file = file_mass
	waste = []

	for info in file:
		info = info.split(" ")
		waste.append(int(info[1]))

	sum = 0

	for i in waste:
		sum += i

	return sum
