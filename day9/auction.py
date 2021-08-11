from art import logo
print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    heighest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > heighest_bid:
            heighest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${heighest_bid}")


while not bidding_finished:
    name = input("what is your name?: ")
    price = int(input("what is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? type 'yes or no'.")
    if should_continue == "no":
        bidding_finished = True
find_highest_bidder(bids)