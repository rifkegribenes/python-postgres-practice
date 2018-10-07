numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
	print(number**2)

for number in numbers:
	print(number > 5)

for number in numbers:
	if number > 5:
		print(number)

magic_numbers = [3, 9]
user_number = 4

if user_number in magic_numbers:
	print('You got it right!')

if user_number not in magic_numbers:
	print('You got it wrong!')