def secret_bding():
    bids = {}
    biding = True

    while biding:
        name = input("What is your name? ")
        bid_amount = input("What is your bid amount? ")

        bids[name] = bid_amount

        if input("Are there more bidders? (Yes, No) ") == "Yes":
            print("\n" * 20)
            continue
        else:
            biding = False

    name_of_big_bid = max(bids, key=bids.get)

    

    return (f"{name_of_big_bid} won the bid with a bid of ${bids[name_of_big_bid]}")

print(secret_bding())

