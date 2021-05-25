import string

def get_num(text):
	"""This function parses phone numbers from text"""
	table = str.maketrans("", "", string.punctuation)
	final_output = []
	for line in text.splitlines():
		normal_num = []
		item_list = line.split()
		# iterating through each words
		for idx, a in enumerate(item_list):
			if "+" in a:

				# join numbers if it has spaces
				if "+91" in a and len(a.translate(table)) == 7:
					a = a + item_list[idx+1]
				# the number will either be written as 2+5+5
				# or it'll be written as 5+5 so we are using different
				# conditions to merge such cases

				# get the pos of plus symbol
				plus_pos = [pos for pos, char in enumerate(a) if char == "+"]
				output = []

				# adding 1 here and subtracting i*2 because everytime
				# the loop runs one item will get lesser, the 1 is added because
				# we need to remove the 91 not +

				# remove the 91 and add extract numbers
				num_list = list(a)
				i = 0
				while i != len(plus_pos):
					del num_list[plus_pos[i] +1 - i*2]
					del num_list[plus_pos[i] +1 - i*2]
					i = i+1
				output.append("".join(num_list).translate(table))

				# we are taking each number from the list and if the number
				# has more than 10 digits then we are slicing the number and adding
				# for example 0-10 is one number then 10-20 then 20-30 and so on
				# the while loop will run as many phone numbers are there,
				# we can get the count by dividing by 10
				for item in output:
					j = 0
					while j < len(item)/10:
						counter = 10*j
						final_output.append(item[counter:counter+10])
						j = j+1

			# for numbers that don't start with +91
			# we are taking all numbers except the ones that have a number
			# previously with a +91 in it, for example we won't take this number
			# +919051 818687 as this was taken and added in the if part.
			else:
				a = a.translate(table)
				if len(a) > 4 and a.isdigit():
					if len(item_list[idx-1]) == 8 and "+91" in item_list[idx-1]:
						pass
					else:
						normal_num.append(a)
		# taking all the normal numbers from each line and joining them without
		# space so that we don't face any issue with spaces.
		# then doing the same while loop as before.
		if len(normal_num) > 0:
			temp_str = "".join(normal_num)
			if len(temp_str) > 5:
				j = 0
				while j < len(temp_str)/10:
					counter = 10*j
					final_output.append(temp_str[counter:counter+10])
					j = j+1

	return final_output
