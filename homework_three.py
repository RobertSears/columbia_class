def question_1(name: str) -> str:
	"""
	Parameters
	----------
	tring: name

	Returns
	----------
	"hellow my name is" + name
	"""
	return f"hello my name is {name}"

def question_2(name: str) -> str:
	"""
	Parameters
	----------
	string: name

	Returns
	----------
	"hellow my name is" + upper case (name)
	"""
	name = name.upper()
	return f"hello my name is {name}"
def question_3(name: str) -> str:
	"""
	Parameters
	----------
	string: name

	Returns
	----------
	"my first name is" + name
	"""
	return f"my first name is {name}"

def question_4(name: str) -> str:
	"""
	Parameters
	----------
	string: name

	Returns
	----------
	"my first name is" + upper case (name)
	"""
	name = name.upper()
	return f"my first name is {name}"

def question_5(first_name: str, last_name: str) -> str:
	"""
	Parameters
	----------
	string: first_name
	string: last_name

	Returns
	----------
	"my full name is" fist_name + last_name
	"""
	return f"my full name is {first_name} {last_name} "

def question_6(first_name: str, last_name: str) -> str:
	"""
	Parameters
	----------
	string: first_name
	string: last_name

	Returns
	----------
	"my full name is" uppercase(fist_name + last_name)
	"""
	first_name = first_name.upper()
	last_name = last_name.upper()
	return f"my full name is {first_name} {last_name}"

def question_7(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The number indices of all lowercase characters
	"""
	list =[]
	counter = 0
	for char in name:
		if char.islower() == True:
			list.append(counter)
		counter += 1
	return list
def question_8(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The number indices of all uppercase characters
	"""
	list =[]
	counter = 0
	for char in name:
		if char.isupper() == True:
			list.append(counter)
		counter += 1
	return list
def question_9(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The number indices of all whitespaces
	"""
	list =[]
	counter = 0
	for char in name:
		if char.isspace() == True:
			list.append(counter)
		counter += 1
	return list
def question_10(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The number individual words in a string
	"""
	x = len(name.split())
	return x
def question_11(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The quantity of numbers in the string
	"""
	list =[]
	counter = 0
	for char in name:
		if char.isdigit() == True:
			counter += 1
	return counter
def question_12(string_one: str, string_two: str) -> str:
	"""
	Parameters
	----------
	string: string_one
	string: string_two

	Returns
	----------
	string_one + string_two
	"""
	return string_one + string_two
def question_13(string_one: str, string_two: str) -> str:
	"""
	Parameters
	----------
	string: string_one
	string: string_two

	Returns
	----------
	upper case(string_one + string_two)
	"""
	string_one = string_one.upper()
	string_two = string_two.upper()
	return string_one + string_two

def question_14(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The same string with "_" instead of " "
	"""
	name = name.split()
	name = '_'.join(name)
	return name
def question_15(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The longest word in the string
	"""
	name = name.split()
	x = max(name, key = len)
	return x
def question_16(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The shortest word in the string
	"""
	name = name.split()
	x = min(name, key = len)
	return x

def question_17(name: str) -> float:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The average length of a word in the string
	"""
	name = name.split()
	x = 0 
	for i in name:
		x = x + len(i)
	y = len(name)
	return x/y

def question_18(name: str) -> int:
	"""
	Parameter
	----------
	string: name
	
	Returns
	----------
	The median word in the string based on length
	""" 
	name = name.split()
	list = [] 
	for i in name:
		list.append(len(i))
	list.sort()
	if len(list)%2 == 0:
		x = (list[int((len(list)-1)/2)]+list[(int((len(list)-1)/2))+1])/2
	else:
		x = list[int((len(list)-1)/2)]
	return x, list
def question_19(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	A list of the even numbers
	"""
	numbers = numbers.split()
	even = []
	for i in numbers:
		if int(i)%2==0:
			even.append(i)
	return even

def question_20(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	A list of the odd numbers
	"""
	numbers = numbers.split()
	odd = numbers
	for i in numbers:
		if int(i)%2==0:
			odd.remove(i)
	return odd

def question_21(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	A list of the three largest numbers
	"""
	numbers = numbers.split()
	numbers.sort(reverse=True)
	return numbers[:3]

def question_22(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	A list of the three smallest numbers
	"""
	numbers = numbers.split()
	numbers.sort()
	return numbers[:3]

def question_23(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	The mean of the list
	"""
	numbers = numbers.split()
	for i in range(0, len(numbers)):
		numbers[i] = int(numbers[i])
	
	return sum(numbers)/len(numbers)

def question_24(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	The mode of the list
	"""
	from statistics import mode
	numbers = numbers.split()
	for i in range(0, len(numbers)):
		numbers[i] = int(numbers[i])
	if len(numbers) == len(set(numbers)):
		numbers = "No Mode"
	else:
		numbers = mode(numbers)	
	return numbers

def question_25(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	The reverse of that list of numbers
	"""
	numbers = numbers.split()
	numbers.reverse()
	return numbers

def question_26(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	The cumulative sum of that list of numbers
	"""
	numbers = numbers.split()
	csum = []
	clist = []
	for i in range(len(numbers)-1):
		csum = int(numbers[i]) + int(numbers[i+1])
		clist.append(csum)
	return sum(clist)

def question_27(numbers: str) -> int:
	"""
	Parameter
	----------
	str: numbers (list of numbers as string)
	
	Returns
	----------
	The cumulative sum of that list of numbers
	"""
	numbers = numbers.split()
	csum = []
	clist = []
	for i in range(len(numbers)-1):
		csum = int(numbers[i]) - int(numbers[i+1])
		clist.append(csum)
	return clist

def question_28(x: int) -> int:
	"""
	Parameter
	----------
	int: interger to start function

	Returns
	----------
	Result of recursive function
	"""
	if x == 0:
		return 0
	if x == 1:
		return 1
	if x == 2:
		return 2
	else:
		return question_28(x-1) + question_28(x-3)

def question_28(x: int) -> int:
	"""
	Parameter
	----------
	int: interger to start function

	Returns
	----------
	Result of recursive function
	"""
	if x == 0:
		return 0
	if x == 1:
		return 1
	if x == 2:
		return 2
	else:
		return question_28(x-1) + question_28(x-3)

def question_29(x: int) -> int:
	"""
	Parameter
	----------
	int: interger to start function
	
	Returns
	----------
	Result of recursive function
	"""
	if x == 0:
		return 1
	else:
		return question_29(x-1) * 1
def question_30(x: int, y: int) -> int:
	if y == 1:
		return 1
	else:
		return x 


