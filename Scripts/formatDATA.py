from collections import OrderedDict
import operator



f = open("test.txt", "r")

file1 = open("Output.txt", "w") 


list_of_lists = []

for line in f:
	stripped_line = line.strip()

	if stripped_line:
		stripped_line = stripped_line + '0'
		list_of_lists.append(stripped_line)

list_of_lists = list(filter(None, list_of_lists))


for one_line in list_of_lists:

	print(one_line)

	list_of_names =[]
	list_of_nums = []

	cur_num = ''

	prev = one_line[0]

	for i in range(1, len(one_line)):

		item = one_line[i]
		if item.isdigit():

			list_of_names.append(prev)

			prev = ''

			cur_num = prev_num + item
			prev_num = cur_num


		else:
			cur = prev + item
			prev = cur
			prev_num = ''

			list_of_nums.append(cur_num)


	list_of_names = list(filter(None, list_of_names))
	list_of_nums = list(filter(None, list_of_nums))

	list_of_nums = list(OrderedDict.fromkeys(list_of_nums))

	District = list_of_names[0]

	del list_of_names[0]

	print(list_of_names)
	print(list_of_nums)

	print(len(list_of_names))
	print(len(list_of_nums))

	list_of_nums = list(map(int, list_of_nums)) 

	new_dict = dict(zip(list_of_nums, list_of_names)) 

	{k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1])}

	for key, value in new_dict.items():

		line = District + '\t' + str(key) + '\t' + value + '\n'
		# print(line)

		file1.write(line)