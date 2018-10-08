import random

magic_numbers = [random.randint(0, 9) for x in range(2)]

user_attempts = int(input("How many chances do you want? "))

def ask_user_and_check_number():
    user_number = input("Enter a number between 0 and 9: ")
    if int(user_number) in magic_numbers:
            return 'You got it right!'

    if int(user_number) not in magic_numbers:
            return 'You got it wrong!'

def run_program_x_times(chances):
    for attempt in range(chances):
        print("This is attempt {}".format(attempt + 1))
        print(ask_user_and_check_number())

run_program_x_times(user_attempts)
    
