import random


def is_won(user, computer):
    return (user == 'r' and computer == 'p') or (user == 'p' and computer == 'c') or (user == 'c' and computer == 'r')


def play():
    print("'r' for rock, 'p' for paper and 's' for scissors")
    user = input("You   ->").lower()
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer -> {computer}")

    if user == computer:
        return "It's a tie!"

    if is_won(user, computer):
        return "You won!"

    return "You lost!"


def game():
    print("Welcome to Rock, Paper, Scissors!")
    print("How many rounds should be done?")
    rounds = int(input("You -> "))

    while rounds > 0:
        print(f"Remaining rounds: {rounds}")
        result = play()
        print(f"{result}")
        rounds -= 1


game()
