# Write your code here
import random


# rules = {
#     'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
#     'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
#     'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
#     'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
#     'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
#     'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
#     'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
#     'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
#     'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
#     'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
#     'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
#     'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
#     'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
#     'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
#     'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']
# }
rating = {}
rules = {}


def winner_selection(user_choice, computer_choice):
    global user_score
    global rules
    if user_choice in rules[computer_choice]:
        return f'Lose -> Sorry, but computer chose {computer_choice}'
    elif user_choice == computer_choice:
        user_score += 50
        return f'Draw -> There is a draw ({computer_choice})'
    elif user_choice not in rules[computer_choice]:
        user_score += 100
        return f'Win -> Well done. Computer chose {computer_choice} and failed'


username = input('Enter your name: ')
print(f'Hello, {username}')
with open('rating.txt') as rating_file:
    for line in rating_file:
        rating[line.split()[0]] = int(line.split()[1])
if username in rating.keys():
    user_score = rating[username]
else:
    user_score = 0
user_options = input()
if user_options == '':
    options_list = ['scissors', 'paper', 'rock']
else:
    options_list = user_options.split(',')[::-1]
half_len = len(options_list) // 2
for i in range(len(options_list)):
    if i <= half_len:
        rules[options_list[i]] = options_list[i + 1:i + half_len + 1]
    else:
        rules[options_list[i]] = options_list[i + 1:] + options_list[:i - half_len]
print("Okay, let's start")
user_option = input()
while user_option != '!exit':
    if user_option == '!rating':
        print(f'Your rating: {user_score}')
    elif user_option not in options_list:
        print('Invalid input')
    else:
        computer_option = random.choice(options_list)
        print(winner_selection(user_option, computer_option))
    user_option = input()
print('Bye!')
