def is_akic_2(string):
	p = string[0]
	for c in string:
		if p > c:
			return False
		else:
			p = c
	return True
	
f = open("name.txt")

for line in f:
	name = line.strip()
	if is_akic_2(name):
		print name

f.close()