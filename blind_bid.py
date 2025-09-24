bid_dict = {}

bid_on = True

 

while bid_on:

    name = input("Enter tour name:  \n").lower()

    bid = int(input("\nEnter your bid in: \nRS: "))

    bid_dict[name] = bid

    choice = input("\nPress yes if any other person is there else press no: \n").lower()

    if choice == "yes":

      print("\n" * 100)

 

    else:

     bid_on = False

#print(bid_dict)

highest_bidder = max(bid_dict, key=bid_dict.get)

highest_bid = bid_dict[highest_bidder]

 

print(f"Bid is now goes to: {highest_bidder}, with bid: {highest_bid}")