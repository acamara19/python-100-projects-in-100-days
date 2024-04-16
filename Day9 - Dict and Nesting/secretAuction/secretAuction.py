from replit import clear

from art import logo

print(logo)
print("Welcome to the secret auction program.")

secret_auction_log = {}
play_round_end = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not play_round_end:
    name = input("What is your name?: ")
    bidding = int(input("What's your bid?: "))
    secret_auction_log[name] = bidding
    should_continue = input("Are there any other bidders? Type `yes` or `no`.\n")
    if should_continue == 'no':
        play_round_end = True
        find_highest_bidder(secret_auction_log)
    elif should_continue == 'yes':
        clear()


