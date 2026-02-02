logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Secret Auction...!")
end_bidders = False

bidders={}

while not end_bidders:
    user_name = input("What is your name? ").title()
    user_bid = int(input("Enter your bid: $"))
    user_choice = input("Type 'yes' if there are any other bidders, otherwise 'no': \n").lower()
    print(20 * "\n")
    if user_choice == 'yes':
        bidders[user_name] = user_bid
    else:
        bidders[user_name] = user_bid
        end_bidders = True

print(bidders)

max_bid = 0
winner =""
for user_name in bidders:

    if bidders[user_name] > max_bid:
        max_bid = bidders[user_name]
        winner = user_name

print(f"The winner is {winner} with a bid of ${max_bid}.\nCongratulations {winner}...!")
