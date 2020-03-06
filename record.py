def record(streng, id):
	print(streng)
	file = open(F"{id}.txt")
	backup = []
	for strong in file.readlines():
		backup.append(strong)

	backup.append(streng)

	file.close()
	file = open(F"{id}.txt", 'w')
	file.truncate()

	for data in backup:
		file.write(data)
		if data == "\n":
			continue
		else:
			file.write("\n")

