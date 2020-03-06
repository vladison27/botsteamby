def check(id):
	import os
	a = 0
	respond = False

	subs =  os.listdir()
	file = F"{id}.txt"

	for sub in subs:

		if file == sub:
			a += 1
		else:
			continue

	if a == 0:
		respond = False

	else:
		respond = True

	return respond