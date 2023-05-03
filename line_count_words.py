#更精簡改寫對話檔案，唯一限制是對話人名要是Allen, Tom
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def write_file(flines):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen said', allen_word_count, 'words, sent', allen_sticker_count, 'stickers and sent', allen_image_count, 'images.')
	print('Viki said', viki_word_count, 'words, sent', viki_sticker_count, 'stickers and sent', viki_image_count, 'images.')


lines = read_file('LINE-Viki.txt')
write_file(lines)
print('Conversion is complete, please check your file.')