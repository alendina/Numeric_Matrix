def startswith_capital_counter(names):
	count = 0
	# names = names.split()
	for name in names:
		count += 1 if name[0] == name[0].upper() else 0

	return count
