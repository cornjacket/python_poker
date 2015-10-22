# this branch to check for low straight in hand, and if so, then rank the Ace
# as a one.

def poker(hands):
    "Return the best hand: poker([hand, ...]) => hand"
    return max(hands, key=hand_rank)

# note that card_ranks will sort the card values in sorted order for tie breakers, so hand_rank depends on that

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks)) # 2 3 4 5 6 -> (8, 6), 6 7 8 9 T -> (8, 10)
    elif kind(4, ranks): # kind is overloaded - boolean and int return
        return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 3 -> (7, 9, 3)
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks) 
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks) 
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2,ranks), ranks)
    else:                                          # high card
        return (0, ranks)

# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...
"""def convert(x):
    if x == 'T': return 10
    elif x == 'J': return 11
    elif x == 'Q': return 12
    elif x == 'K': return 13
    elif x == 'A': return 14
    else: return int(x)
"""

# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5
    #pick first element ranks[0] and build and array from it
    #start = ranks[0]
    #stop  = ranks[0]-5
    #match = range(start,stop,-1) # decending order
    #if ranks == match:
    #    return True
    #return False


def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
    suits = [s for r,s in hand]
    return len(set(suits)) == 1
    #suits = [s for r,s in hand] # grab the suits
    #kind  = suits[0]
    #for suit in suits:
    #    if suit != kind:
    #        return False
    #return True

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    #ranks = [r for r,s in cards]
    #ranks = map(convert, ranks)

    # otherwise rank the Ace as a high card
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks


def my_card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    #ranks = [r for r,s in cards]
    #ranks = map(convert, ranks)

    # need to check for low straight here, and if so return 1 as Ace rank
    ranks = ['-A23456789TJQK-'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    if straight(ranks):
        return ranks
    else:
        # otherwise rank the Ace as a high card
        ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
        ranks.sort(reverse=True)
        return ranks

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pair = kind(2,ranks)
    # reversed creates an iterator, assume list converts to a list
    # goes from lowest to highest now
    low_pair = kind(2, list(reversed(ranks))) # how does list(...) work
    if pair and low_pair != pair:
        return (pair, low_pair)
    else:
        return None


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks: # ranks coming in has highest value first
        if ranks.count(r) == n: return r # count counts the number of occurences in ranks
    return None

def my_kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # declare frequency array to keep track of number of each card
    num_values = len('--23456789TJQKA')
    num_occurences = [0] * num_values
    #print "length = "+str(len('--23456789TJQKA'))
    #print num_occurences
    for rank in ranks:
        num_occurences[rank] += 1
    # now we have a count for each rank
    # lets iterate through the array and see if we can find the val==n
    # start at the largest rank since that is the order expected for tie breakers
    for idx in range(num_values-1, 2, -1):
        if num_occurences[idx] == n:
            return idx
    return None
    


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # straight flush
    fk = "9D 9H 9S 9C 7D".split() # four of a kind
    fh = "TD TC TH 7C 7D".split() # full house
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
    ah = "AS 2S 3S 4S 6C".split() # A high
    sh = "2S 3S 4S 6C 7D".split() # 7 high

    # corner case where ah > s1 unless addressed
    assert poker([s1, ah]) == s1

    assert poker([s1, s2, ah, sh]) == s2
    
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert poker([sf, fk, fh]) == sf
    # Add 2 new assert statements here. The first 
    # should check that when fk plays fh, fk 
    assert poker([fh, fk]) == fk
    # is the winner. The second should confirm that
    # fh playing against fh returns fh.
    assert poker([fh, fh]) == fh

    # Add 2 new assert statements here. The first 
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second 
    assert poker([sf]) == sf
    # should check for the case of 100 hands.
    assert poker([sf] + 99*[fk]) == sf

    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) == (6,10,7)


    return "tests pass"

print test()
