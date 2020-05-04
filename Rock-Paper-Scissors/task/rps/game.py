# Write your code here
import random


def winner_selection(user_choice, computer_choice):
    global user_score
    if (user_choice == 'rock' and computer_choice == 'paper'
            or user_choice == 'paper' and computer_choice == 'scissors'
            or user_choice == 'scissors' and computer_choice == 'rock'):
        return f'Lose -> Sorry, but computer chose {computer_choice}'
    elif user_choice == computer_choice:
        user_score += 50
        return f'Draw -> There is a draw ({computer_choice})'
    elif (user_choice == 'paper' and computer_choice == 'rock'
          or user_choice == 'scissors' and computer_choice == 'paper'
          or user_choice == 'rock' and computer_choice == 'scissors'):
        user_score += 100
        return f'Win -> Well done. Computer chose {computer_choice} and failed'


rating = {}
options_list = ['rock', 'paper', 'scissors']
username = input('Enter your name: ')
print(f'Hello, {username}')
with open('rating.txt') as rating_file:
    for line in rating_file:
        rating[line.split()[0]] = int(line.split()[1])
if username in rating.keys():
    user_score = rating[username]
else:
    user_score = 0
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
