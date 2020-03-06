def reg(id):
	import datetime

	date = str(datetime.date.today())
	file = open(F"{id}.txt", 'w')
	file.write(date)
	file.close()