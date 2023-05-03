#更精簡改寫對話檔案，唯一限制是對話人名要是Allen, Tom
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def write_file(lines):
	person = None
	with open('output2.txt', 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			if line == 'Allen':
				person = 'Allen'
				continue
			elif line == 'Tom':
				person = 'Tom'
			if person:
				f.write(person + ': ' + line + '\n')


filename = input('選擇你要改編的對話檔: ')
lines = read_file(filename)
print('test: ', lines)
write_file(lines)
print('Conversion is complete, please check your file.')