with open('./cpp.c', 'r') as f:
	file = f.readlines()

with open('./indent.c', 'w') as f:
	indent = 0
	for line in file:
		if line[:5] == '#if S':
			f.write('\n')

		f.write('\t' * (indent - (line[:5] == '#else' or line[:6] == '#endif')) + line)
		
		if line[:3] == '#if':
			indent += 1
		elif line[:6] == '#endif':
			indent -= 1
