from random import randint
from colorama import Fore
from colorama import Style

hits = 0
attempts = 0

while hits < 4:
    print(f'{Fore.BLUE}Guess the number{Style.RESET_ALL}')
    random_number = randint(1,20)
    user_input= 0
    while user_input != random_number:
        user_input = int(input('Input a number: '))
        if user_input > random_number:
            print(f'{Fore.RED}The value is greater{Style.RESET_ALL}')
        elif user_input < random_number:
            print(f'{Fore.RED}The value is less{Style.RESET_ALL}')
        else:
            print(f'{Fore.GREEN}Correct!{Style.RESET_ALL}')
        attempts+=1
    hits+=1

print(f'{Fore.YELLOW}Attempts: {attempts}{Style.RESET_ALL}')