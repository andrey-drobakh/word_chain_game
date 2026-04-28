




# payers_list = ['Bob', 'Tom', 'Rise', 'DAN', 'MAGIC']

# retired_players_list = []
#
# print(f'\n     {payers_list}     \n')
#
# payers_list.append(payers_list[0])
# payers_list.remove(payers_list[0])
# w_1 = input(f'       INPUT WORD {payers_list[-1]} : ').lower()
#
# winner = payers_list[-1]
# attempt_counter = 0


player_names = input('\n Введите имена игроков через пробел: ').split()

def create_players_list(users):
    if users and len(users) > 1:
        retired_players_list = []
        print(f'\n     {users}     \n')
        player_names.append(users[0])
        player_names.remove(users[0])
        w_1 = input(f'       INPUT WORD {users[-1]} : ').lower()
        winner = users[-1]
        attempt_counter = 0
        print(game(users, retired_players_list, w_1, winner, attempt_counter))
    elif users and len(users) == 1:
        print('\n ВСЕГО ОДИН ИГРОК В ИГРЕ')
    else:
        print('\n НЕКОРРЕКТНЫЕ ДАННЫЕ')





def game(player_list, retired_players_list, w_1, winner, attempt_counter):

    while len(retired_players_list) < len(player_list)-1:

        for name in player_list:

            if name in retired_players_list or name == winner: # Чтобы перешагнуть через элемент с индексом ноль
                                                   # и не брать тех кто находится в ass_list
                attempt_counter = 0
                continue

            while attempt_counter != 3:

                attempt_counter += 1
                w_2 = input(f'       {name} enter a word starting with a letter: {w_1[-1].upper()},'
                            f' attempt {attempt_counter} : ').lower()

                if w_2 and w_1[-1] == w_2[0]:
                    attempt_counter = 0
                    print(f'\nOK {name}, DONE !\n')
                    winner = name
                    w_1 = w_2
                    break
                if w_2 == 'StoppedGame':
                    print(f'\nStopped ! -----{name} is out of the game-----\n')
                    retired_players_list.append(name)
                    break

                elif w_1 != w_2 and attempt_counter < 3:
                    print(f'\nINCORRECT INPUT {name} !\n')
                    continue
                elif w_1 != w_2 and attempt_counter == 3:
                    print(f'\n-----{name} is out of the game-----\n')
                    attempt_counter = 0
                    retired_players_list.append(name)
                    break

    return f'Game winner {winner}'

create_players_list(player_names)

# print('                             Game winner - ', winner)



















