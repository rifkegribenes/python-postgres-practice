import random

def menu():
    # ask player for numbers
    player_numbers = get_player_numbers()
    # calculate lottery numbers
    lottery_numbers = create_lottery_numbers()
    # print out winnings
    matches = lottery_numbers.intersection(player_numbers)
    print("You matched {}. You won ${}!".format(matches, 100 ** len(matches)))


def get_player_numbers():
    numbers_csv = input("Choose six lottery numbers separated by commas: ")
    user_input_split = numbers_csv.split(',')
    return {int(number) for number in user_input_split}


def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1,20))
    return values


menu()