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
	for i in chat:
		if i == 'Allen' or i == 'Tom':
			person = i
			continue
		if person:
			new_sentence.append(person + ': ' + i)
	return new_sentence


#write in file
def write_file(filename2, new):
	with open(filename2, 'w', encoding = 'utf-8-sig') as f:
		for line in new:
			f.write(line + "\n")


def main():
	filename = 'input.txt'
	filename2 = 'output.txt'
	chat = read_file(filename)
	new = add(chat)
	write_file(filename2, new)
	

main()


