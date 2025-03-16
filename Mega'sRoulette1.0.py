import os
import random
import time

def get_random_numbers(count):
    return [random.randint(1, 6) for _ in range(count)]

def check_loss(user_input, random_numbers):
    return user_input in random_numbers

def get_valid_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if 1 <= user_input <= 6:
                return user_input
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

x = random.randint(1, 6)
print("RUSSIAN ROULETTE GAME v1.0 - @Mega6503 | Welcome!")
print("Getting everything ready...")
time.sleep(1)
print("Rolling the dice...")
time.sleep(1)
y = get_valid_input("Let's start easy. Pick a number from 1 to 6. There is only one wrong answer: ")

if y != x:
    print("Congrats, you won!")
    random_numbers = get_random_numbers(2)
    y = get_valid_input("Now there are two wrong answers. Pick a number from 1 to 6: ")
    if not check_loss(y, random_numbers):
        random_numbers = get_random_numbers(3)
        a = get_valid_input("Congrats, you won again! Now there will be a 50/50 chance of losing. Pick a number from 1 to 6: ")
        if not check_loss(a, random_numbers):
            random_numbers = get_random_numbers(4)
            a = get_valid_input("Dammit, you're good! Now the odds are against you. Pick a number from 1 to 6: ")
            if not check_loss(a, random_numbers):
                random_numbers = get_random_numbers(5)
                a = get_valid_input("Last round. 5 WRONG ANSWERS. Pick a number from 1 to 6: ")
                if not check_loss(a, random_numbers):
                    while True:
                        t = input("You won! Your odds of reaching this point were 1.54%. As a reward, you won 50Dh. Would you like to double or nothing? y/n: ")
                        if t == "y":
                            print("greedy ahh💀💀")
                            time.sleep(1)
                            os.system("shutdown /s /t 0")
                        elif t == "n":
                            print("smart choice. goodbye!")
                            break
                        else:
                            print("please enter a valid input")
                            time.sleep(2)
                else:
                    print("you lost, now assume the consequences")
                    time.sleep(1)
                    os.system("shutdown /s /t 0")
            else:
                print("you lost, now assume the consequences")
                time.sleep(1)
                os.system("shutdown /s /t 0")
        else:
            print("you lost, now assume the consequences")
            time.sleep(1)
            os.system("shutdown /s /t 0")
    else:
        print("you lost, now assume the consequences")
        time.sleep(1)
        os.system("shutdown /s /t 0")
else:
    print("you lost, now assume the consequences")
    time.sleep(1)
    os.system("shutdown /s /t 0")
    