from arts import logo2
print(logo2)


information =[]
biggest_bid = 0
no_players = False
winner_position = 0
while not no_players:
    bidder = {}
    name = input("What is your name?: ")
    bidder["name"] = name
    bid = int(input("What is your bid?: "))
    bidder["bid"] = bid
    other_bidders = input("Are there any other bidders?Type 'yes' or 'no'.\n")
    information.append(bidder)
    if other_bidders == 'no':
        no_players = True
for i in range (0, len(information)):
    current_bid = information[i]["bid"]
    if current_bid > biggest_bid:
        biggest_bid = current_bid
        winner_position = i
         
winner_name = information[winner_position]["name"]
winner_bid = information[winner_position]["bid"]
print(f"The winner is {winner_name} with a bid of ${winner_bid}") 
         
     

