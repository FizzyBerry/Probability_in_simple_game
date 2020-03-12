from random import randint

first_player_wins = 0
second_player_wins = 0
for i in range(100000):
    first_player_sum = 0
    while first_player_sum < 100:
        tmp = randint(1, 100)
        first_player_sum += tmp
        last_added_number_player1 = tmp
    second_player_sum = 0
    while second_player_sum < 200:
        tmp = randint(1, 100)
        second_player_sum += tmp
        last_added_number_player2 = tmp
    if last_added_number_player1 < last_added_number_player2:
        second_player_wins += 1
    else:
        first_player_wins += 1

first_player_wins = round(first_player_wins / 1000, 3)
second_player_wins = round(second_player_wins / 1000, 3)
print(first_player_wins)
print(second_player_wins)