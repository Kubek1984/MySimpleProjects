import random
from time import sleep

def pick_the_number(numbers_list):
    index = random.randint(0, len(numbers_list) - 1)
    return numbers_list[index]

def pick_six():
    # ----------------Generate List Numbers ------------------------
    list_numbers = []
    for i in range(1, 50):
        list_numbers.append(i)
    # ---------------- Pick six numbers --------------------------
    numbers = []
    for i in range(6):
        num = pick_the_number(list_numbers)
        numbers.append(num)
        list_numbers.remove(num)

    return numbers

def checker(lucky_numbers, my_numbers):
    pass
    list_of_same_num = []
    for number in lucky_numbers:
        for nr in my_numbers:
            if number == nr:
                list_of_same_num.append(nr)
    return list_of_same_num


def player_numbers():
    # player_six = []
    # loop_nr = 1
    # while len(player_six) < 6:
    #     pass
    #     nr = input(f'{loop_nr} number : ')
    #     if nr.strip().isdigit() and 0 < int(nr.strip()) < 50:
    #         player_six.append(int(nr))
    #         loop_nr += 1
    #     else:
    #         print('Must be nr between 1 and 49')
    # return player_six
    return [16, 3, 4, 7, 23, 49]
# pick_six()
# player_numbers()
def main():
    six_dictionary = {
        'one': 0,
        'two': 0,
        'three': 0,
        'four': 0,
        'five': 0,
        'six': 0
    }
    games = 0
    while True:
        lucky_six = pick_six()
        player = player_numbers()
        result = checker(lucky_six, player)
        if result == 1 :
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            six_dictionary['one'] += 1
            games += 1
        elif result == 2:
            six_dictionary['two'] += 1
            games += 1
            print(f'Congrats !! You have TWO !!\nGames : {games}')
            # sleep(5)
        elif result == 3:
            six_dictionary['three'] += 1
            games += 1
            # print(f'Congrats !! You have THREE !!\nGames : {games}')
            # sleep(5)
        elif result == 4:
            six_dictionary['four'] += 1
            games += 1
            # print(f'Congrats !! You have FOUR !!\nGames : {games}')
            # sleep(5)
        elif result == 5:
            six_dictionary['five'] += 1
            games += 1
            # print(f'Congrats !! You have FIVE !!\nGames : {games}')
            # sleep(5)
        elif result == 6:
            six_dictionary['six'] += 1
            games += 1
            break
    for key, value in six_dictionary.items():
        print(key, ': ', value)

main()