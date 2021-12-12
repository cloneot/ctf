import string

MOD = 1 << 8
MASK = (1 << 8) - 1

text = "3c3cf1df89fe832aefcc22fc82017cd57bef01df54235e21414122d78a9d88cfef3cf10c829ee32ae4ef01dfa1951cd51b7b22fc82433ef7ef418cdf8a9d802101ef64f9a495268fef18d52882324f217b1bd64b82017cd57bef01df255288f7593922712c958029e7efccdf081f8808a6efd5287595f821482822f6cb95f821cceff4695495268fefe72ad7821a67ae0060ad"
rm = ['', '', '', '', '\x0f', '\x05\x06\x05\x05\x06', '\x1d\x1d\x1d\x1d\x1d', '\x15\x15\x15\x16\x16', 'nmmnmn', 'ffff', '~}}~', 'uvvu', '\x00', 'FFFF', '^]]^', 'UVVU', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x0c\x0f\x0c\x0f\x0c\x0c', '\x04\x07\x04\x04\x07\x04', '\x1f\x1c\x1c\x1c\x1c', '\x14\x14\x14\x14\x17', 'ol', 'gg', '||\x7f|', 'twtt', 'OL', 'GG', '\\\\_\\', 'TWTT', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '\x00', '\x1c\x1c\x1f\x1f\x1f', '\x17\x17\x17\x14\x14\x14', 'olll', 'dggg', '|\x7f|', 'wwtt', 'OLLL', 'DGGG', '\\_\\', 'WWTT', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '\x05\x06\x05\x06\x05', '\x1d\x1d\x1d\x1e\x1e', '\x16\x15\x16\x15\x16\x15', 'nmnm', 'fef', '}}}', '\x00', 'NMNM', 'FEF', ']]]', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\n\n\n\n\n', '\x01\x01\x02\x02\x01\x01', '\x1a\x1a\x1a\x1a\x19', '\x00', 'ijj', 'babb', 'y', '\x00', 'IJJ', 'BABB', 'Y', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '\x00\x03\x03\x03\x03\x00', '\x1b\x1b\x1b\x1b\x1b', '\x10\x13\x13\x13\x10', 'k', '``', '{{x', '\x00', 'K', '@@', '[[X', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x08\x0b\x08\x08\x08', '\x00\x03\x00\x03\x00\x03', '\x1b\x18\x18\x18\x18', '\x00', 'hhkh', 'c`', 'xxx{', '\x00', 'HHKH', 'C@', 'XXX[', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\t\n\n\n\n\t', '\x02\x01\x01\x02\x01', '\x1a\x1a\x19\x19\x19', '\x11\x11\x12\x12\x11\x11', 'jji', 'bbb', 'yzz', 'qqrrqr', 'JJI', 'BBB', 'YZZ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
xm = 1056017893861212352
array = [xm & 255, xm >> 8 & 255, xm >> 16 & 255, xm >> 24 & 255, xm >> 32 & 255, xm >> 40 & 255, xm >> 48 & 255, xm >> 56 & 255]

# It's ror
def rol(v, cnt):
	cnt %= 8
	return ((v>>cnt) | (v<<(8-cnt))) & MASK

# It's rol
def ror(v, cnt):
	cnt %= 8
	return ((v<<cnt) | (v>>(8-cnt))) & MASK

def f0(c):
	if type(c) is str:
		c = ord(c)
	return rol(c, 3)

def f1(c):
	if type(c) is str:
		c = ord(c)
	return chr(ror(c, 5))

def f2(c, x):
	if type(c) is str:
		c = ord(c)	
	return ''.join([chr(ord(y) ^ c) for y in x])

def f3(c):
	if type(c) is str:
		c = ord(c)	
	return f2(c, ''.join(map(f1, rm[f0(c)])))

# text = text[::-1]
text2 = ''
for i in range(0, len(text), 2):
	text2 += chr(int(text[i:i+2], 16) ^ array[(i // 2) % len(array)])
text2 = text2.split('/')
print(text2)
# ['üüü', '$D$$', '\x0c', '\x0c', '»ÛÛ»', '\x0c', 'ù\x99ù', '\x81\x81', "'''", 'Á', 'üüü', '$D$$', '\x0c', '\x0c', '»ÛÛ»', '\x0c', 'ù\x99ù', '\x81\x81', "'''", 'Á', 'i\t\t', '\x81\x81', 'ØØØ', '\x88è', '»ÛÛ»', '»ÛÛ»', '\x0c', '\x88è', 'ù\x99ù', '\x81\x81', "'''", 'Á', '¥¥', '\x06f', 'ØØØ', '_', '\x88è', '\x06f', '_', '\x0c', 'ù\x99ù', '\x81\x81', "'''", '\xa0À\xa0À\xa0\xa0']

key = ''
for s in text2:
	cnt = 0
	for c in string.printable:
		if s == f3(c):
			key += c
			cnt += 1
	assert cnt == 1

print(key)
# Sleeperio Sleeperio Disappeario Instanterio!
