import os 

# read file
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			word = line.strip()
			chat.append(word)
	return chat


# adding name for each sentence
def add(chat):
	person = None
	new_sentence = []
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for i in chat:
		s = i.split(' ')
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
	print('allen said', allen_word_count,'words')
	print('allen sent',allen_sticker_count, 'stickers')
	print('allen sent',allen_image_count, 'pics')
	print('viki said', viki_word_count,'words')
	print('viki sent',viki_sticker_count, 'stickers')
	print('viki sent',viki_image_count, 'pics')

	return new_sentence


#write in file
def write_file(filename2, new):
	with open(filename2, 'w', encoding = 'utf-8-sig') as f:
		for line in new:
			f.write(line + "\n")


def main():
	filename = 'LINE-Viki.txt'
	filename2 = 'output.txt'
	chat = read_file(filename)
	new = add(chat)
	#write_file(filename2, new)
	

main()


