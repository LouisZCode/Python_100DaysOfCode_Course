"""Blind Auction Program!"""

bidders = {}
bid_stop = False

while bid_stop == False:

    go_on = input('Do you want to add a Bid?\n')

    if go_on == "yes":

        new_bidder = str(input('tell me your name\n'))
        bid = int(input('how much?\n'))

        bidders[new_bidder] = bid

        print(bidders)
    
    elif go_on == "no":
        bid_stop = True
        max_value = 0
        winner = ''

        for i in bidders:
            value_bid = bidders[i]
            if value_bid > max_value:
                max_value = value_bid
                winner = i

        print(f'The highes bidder and now buyer is {winner}!!!')


