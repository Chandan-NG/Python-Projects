import random
import data
import art

def get_random_account():
    return random.choice(data.data)

def format_data(account):
    return f"{account['name']}, {account['description']}, from {account['country']}"

def check_winner(a, b):
    if a["follower_count"] > b["follower_count"]:
        return a
    else:
        return b

def h_or_l():
    score = 0
    game_should_continue = True

    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        while account_a == account_b:
            account_b = get_random_account()
        
        print(art.logo)

        print(f"Compare A: {format_data(account_a)}")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        print(25 * "\n")

        winner = check_winner(account_a, account_b)

        guessed_account = account_a if guess == "a" else account_b

        if guessed_account == winner:
            score += 1
            print(f"You're right! Current score: {score}\n")
            account_a = winner
            account_b = get_random_account()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

h_or_l()
