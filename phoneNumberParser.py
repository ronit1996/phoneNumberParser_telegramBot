import string

def get_num(text):
	"""This function parses phone numbers from text"""
	table = str.maketrans("", "", string.punctuation)

	final_output = []
	# get the position of plus symbol
	for line in text.splitlines():
		for a in line.split():
			if "+" in a:
				plus_pos = [pos for pos, char in enumerate(a) if char == "+"]
				output = []
				# remove the 91 and add extract numbers
				num_list = list(a)
				i = 0
				while i != len(plus_pos):
					del num_list[plus_pos[i] +1 - i*2]
					del num_list[plus_pos[i] +1 - i*2]
					i = i+1
				output.append("".join(num_list).translate(table))
				for count, item in enumerate(output):
					j = 0
					while j < len(item)/10:
						counter = 10*j
						final_output.append(item[counter:counter+10])
						j = j+1
			elif a.isdigit():
				final_output.append(a)

	return final_output


# read the messages
with open("message.txt") as m:
	text = m.read()


print(get_num(text))