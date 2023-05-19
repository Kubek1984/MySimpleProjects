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
#     player_six = []
#     loop_nr = 1
#     while len(player_six) < 6:
#         pass
#         nr = input(f'{loop_nr} number : ')
#         if nr.strip().isdigit() and 0 < int(nr.strip()) < 50:
#             player_six.append(int(nr))
#             loop_nr += 1
#         else:
#             print('Must be nr between 1 and 49')
#     return player_six
    return [16, 3, 4, 7, 23, 49, 12, 14, 33, 39, 44, 1]
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
    six_dictionary_1 = {
        'one': 0,
        'two': 0,
        'three': 0,
        'four': 0,
        'five': 0,
        'six': 0
    }
    six_dictionary_2 = {
        'one': 0,
        'two': 0,
        'three': 0,
        'four': 0,
        'five': 0,
        'six': 0
    }
    six_dictionary_3 = {
        'one': 0,
        'two': 0,
        'three': 0,
        'four': 0,
        'five': 0,
        'six': 0
    }
    six_dictionary_4 = {
        'one': 0,
        'two': 0,
        'three': 0,
        'four': 0,
        'five': 0,
        'six': 0
    }
    six_dictionary_5 = {
        'one': 0,
        'two': 0,
        'three': 0,
        'four': 0,
        'five': 0,
        'six': 0
    }
    six_dictionary_6 = {
        'one': 0,
        'two': 0,
        'three': 0,
        'four': 0,
        'five': 0,
        'six': 0
    }
    games = 0
    player = pick_six()
    player_1 = pick_six()
    player_2 = pick_six()
    player_3 = pick_six()
    player_4 = pick_six()
    player_5 = pick_six()
    player_6 = pick_six()
    while True:

        lucky_six = pick_six()
        result = checker(lucky_six, player)
        result_1 = checker(lucky_six, player_1)
        result_2 = checker(lucky_six, player_2)
        result_3 = checker(lucky_six, player_3)
        result_4 = checker(lucky_six, player_4)
        result_5 = checker(lucky_six, player_5)
        result_6 = checker(lucky_six, player_6)
        if len(result) == 1 :
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            six_dictionary['one'] += 1
            games += 1
        elif len(result) == 2:
            six_dictionary['two'] += 1
            games += 1
            print(f'Congrats !! You have TWO !!\nGames : {games}')
            # sleep(5)
        elif len(result) == 3:
            six_dictionary['three'] += 1
            games += 1
            # print(f'Congrats !! You have THREE !!\nGames : {games}')
            # sleep(5)
        elif len(result) == 4:
            six_dictionary['four'] += 1
            games += 1
            # print(f'Congrats !! You have FOUR !!\nGames : {games}')
            # sleep(5)
        elif len(result) == 5:
            six_dictionary['five'] += 1
            games += 1
            # print(f'Congrats !! You have FIVE !!\nGames : {games}')
            # sleep(5)
        elif len(result) == 6:
            six_dictionary['six'] += 1
            games += 1
            break
        else:
            print('Zero matches')
            games += 1

        if len(result_1) == 1 :
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            six_dictionary_1['one'] += 1
        elif len(result_1) == 2:
            six_dictionary_1['two'] += 1
            print(f'Congrats !! You have TWO !!\nGames : {games}')
            # sleep(5)
        elif len(result_1) == 3:
            six_dictionary_1['three'] += 1
            # print(f'Congrats !! You have THREE !!\nGames : {games}')
            # sleep(5)
        elif len(result_1) == 4:
            six_dictionary_1['four'] += 1
            # print(f'Congrats !! You have FOUR !!\nGames : {games}')
            # sleep(5)
        elif len(result_1) == 5:
            six_dictionary_1['five'] += 1
            # print(f'Congrats !! You have FIVE !!\nGames : {games}')
            # sleep(5)
        elif len(result_1) == 6:
            six_dictionary_1['six'] += 1
            break
        if len(result_2) == 1 :
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            six_dictionary_2['one'] += 1
        elif len(result_2) == 2:
            six_dictionary_2['two'] += 1
            print(f'Congrats !! You have TWO !!\nGames : {games}')
            # sleep(5)
        elif len(result_2) == 3:
            six_dictionary_2['three'] += 1
            # print(f'Congrats !! You have THREE !!\nGames : {games}')
            # sleep(5)
        elif len(result_2) == 4:
            six_dictionary_2['four'] += 1
            # print(f'Congrats !! You have FOUR !!\nGames : {games}')
            # sleep(5)
        elif len(result_2) == 5:
            six_dictionary_2['five'] += 1
            # print(f'Congrats !! You have FIVE !!\nGames : {games}')
            # sleep(5)
        elif len(result_2) == 6:
            six_dictionary_2['six'] += 1
            break
        if len(result_3) == 1 :
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            six_dictionary_3['one'] += 1
            games += 1
        elif len(result_3) == 2:
            six_dictionary_3['two'] += 1
            games += 1
            print(f'Congrats !! You have TWO !!\nGames : {games}')
            # sleep(5)
        elif len(result_3) == 3:
            six_dictionary_3['three'] += 1
            games += 1
            # print(f'Congrats !! You have THREE !!\nGames : {games}')
            # sleep(5)
        elif len(result_3) == 4:
            six_dictionary_3['four'] += 1
            games += 1
            # print(f'Congrats !! You have FOUR !!\nGames : {games}')
            # sleep(5)
        elif len(result_3) == 5:
            six_dictionary_3['five'] += 1
            games += 1
            # print(f'Congrats !! You have FIVE !!\nGames : {games}')
            # sleep(5)
        elif len(result_3) == 6:
            six_dictionary_3['six'] += 1
            games += 1
            break
        else:
            print('Zero matches')

        if len(result_4) == 1 :
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            six_dictionary_4['one'] += 1
        elif len(result_4) == 2:
            six_dictionary_1['two'] += 1
            print(f'Congrats !! You have TWO !!\nGames : {games}')
            # sleep(5)
        elif len(result_4) == 3:
            six_dictionary_4['three'] += 1
            # print(f'Congrats !! You have THREE !!\nGames : {games}')
            # sleep(5)
        elif len(result_4) == 4:
            six_dictionary_4['four'] += 1
            # print(f'Congrats !! You have FOUR !!\nGames : {games}')
            # sleep(5)
        elif len(result_4) == 5:
            six_dictionary_4['five'] += 1
            # print(f'Congrats !! You have FIVE !!\nGames : {games}')
            # sleep(5)
        elif len(result_4) == 6:
            six_dictionary_4['six'] += 1
            break
        if len(result_5) == 1 :
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            six_dictionary_5['one'] += 1
        elif len(result_5) == 2:
            six_dictionary_5['two'] += 1
            print(f'Congrats !! You have TWO !!\nGames : {games}')
            # sleep(5)
        elif len(result_5) == 3:
            six_dictionary_5['three'] += 1
            # print(f'Congrats !! You have THREE !!\nGames : {games}')
            # sleep(5)
        elif len(result_5) == 4:
            six_dictionary_5['four'] += 1
            # print(f'Congrats !! You have FOUR !!\nGames : {games}')
            # sleep(5)
        elif len(result_5) == 5:
            six_dictionary_5['five'] += 1
            # print(f'Congrats !! You have FIVE !!\nGames : {games}')
            # sleep(5)
        elif len(result_5) == 6:
            six_dictionary_5['six'] += 1
            break
        if len(result_6) == 1 :
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            six_dictionary_6['one'] += 1
        elif len(result_6) == 2:
            six_dictionary_6['two'] += 1
            print(f'Congrats !! You have TWO !!\nGames : {games}')
            # sleep(5)
        elif len(result_6) == 3:
            six_dictionary_6['three'] += 1
            # print(f'Congrats !! You have THREE !!\nGames : {games}')
            # sleep(5)
        elif len(result_6) == 4:
            six_dictionary_6['four'] += 1
            # print(f'Congrats !! You have FOUR !!\nGames : {games}')
            # sleep(5)
        elif len(result_6) == 5:
            six_dictionary_6['five'] += 1
            # print(f'Congrats !! You have FIVE !!\nGames : {games}')
            # sleep(5)
        elif len(result_6) == 6:
            six_dictionary_6['six'] += 1
            break

    for key, value in six_dictionary.items():
        print(f' {key} : {value}', end='')
    print()
    for key, value in six_dictionary_1.items():
        print(f' {key} : {value}', end='')
    print()
    for key, value in six_dictionary_2.items():
        print(f' {key} : {value}', end='')
    print()
    for key, value in six_dictionary_3.items():
        print(f' {key} : {value}', end='')
    print()
    for key, value in six_dictionary_4.items():
        print(f' {key} : {value}', end='')
    print()
    for key, value in six_dictionary_5.items():
        print(f' {key} : {value}', end='')
    print()
    for key, value in six_dictionary_6.items():
        print(f' {key} : {value}', end='')

main()