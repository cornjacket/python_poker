import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    random.seed()
    all_hands = []
    deck_len = len(deck)
    num_occurences = [0] * deck_len
    #print "deck_len = "+str(deck_len)
    for i in range(numhands):
        hand = []
        for j in range(n):
            done = False
            while not done:    
                #print str(i)+" "+str(j)
                card_index = random.randint(0,deck_len-1)
                #print "card_index = "+str(card_index)
                #print num_occurences[card_index]
                if num_occurences[card_index] == 0:
                    num_occurences[card_index] += 1
                    hand.append(mydeck[card_index])
                    done = True
                #else:
                #    print "Duplicate"+str(mydeck[card_index])
        all_hands.append(hand)
        #print "hands update"
        #print all_hands
    return all_hands

for hand in deal(5):
    print hand
