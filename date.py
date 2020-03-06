def check_date(streng, idd):
	import datetime
	import record as rec

	file = open(F"{idd}.txt")
	file_mass = []

	for string in file.readlines():
		file_mass.append(string)

	date = file_mass[0]
	del(file_mass)

	date = date.split("-")
	date_m = []
	for i in date:
		i = int(i)
		date_m.append(i)

	date = date_m
	del(date[0])

	date_sum = (date[0] * 30) + date[1]		# дата из файла.

	date_today = str(datetime.date.today())
	date_today = date_today.split("-")
	date_today_m = []

	for i in date_today:
		i = int(i)
		date_today_m.append(i)

	date_today = date_today_m
	del(date_today_m)

	del(date_today[0])

	date_today_sum = (date_today[0]*30) + date_today[1]

	diff = date_today_sum - date_sum
	
	file.close()

	if diff >= 30:
		file = open(F"{idd}.txt", "w")
		file.truncate()
		file = open(F"{idd}.txt", "w")
		date = str(datetime.date.today())
		file.write(date)
		rec.record(streng, idd)
		return "Запись за прошлые 30 дней очищена!"
	else:
		rec.record(streng, idd)
		return "Запись произведена успешно!"