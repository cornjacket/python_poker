# CS 212, hw1-1: 7-card stud
#
# -----------------
# User Instructions
#
# Write a function best_hand(hand) that takes a seven
# card hand as input and returns the best possible 5
# card hand. The itertools library has some functions
# that may help you solve this problem.
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools

# allows for multiple jokers

def best_wild_hand(hand = "6C 7C 8C 9C 6D ?R ?B".split()): # ?B
    "Try all values for jokers in all 5-card selections."
    #find all 5 card combos of the 7 card hand just like in best_hand
    all_fiveCardHands = []
    all_combos = itertools.combinations(hand, 5)
    #for idx, combo in enumerate(all_combos): #
    for combo in all_combos:
        #print idx, combo
        fiveCardHand = list(combo)
        # create a list of wildcards
        cards_with_wildcards = filter(lambda x: '?' in x, fiveCardHand)
        if len(cards_with_wildcards) == 0:
            all_fiveCardHands.append(fiveCardHand)
        elif len(cards_with_wildcards) <= 2: # and idx <= 5:
            #print "Wildcard"
            #print fiveCardHand # testing
            all_fiveCardHands += convert_wild_card(fiveCardHand)
            #print all_fiveCardHands
        #else:
        #    print "best_wild_hand: Error: too many wildcards"
    #then for each of the 5 card combos
    #for fiveCardHand in all_fiveCardHands:
    #    print fiveCardHand
    return max(all_fiveCardHands, key=hand_rank)
    
    # Your code here

def convert_wild_card(fiveCardHand = "8C 9C TC ?R ?B".split()):
    black_deck=[r+s for r in '23456789TJQKA' for s in 'SC']
    red_deck=[r+s for r in '23456789TJQKA' for s in 'HD']
    all_hands = []
    cards_with_wildcards = filter(lambda x: '?' in x, fiveCardHand)
    if len(cards_with_wildcards) == 1:
        wildcard = cards_with_wildcards[0]
        #print wildcard
        #print "id = "+str(id(fiveCardHand))
        index = fiveCardHand.index(wildcard)
        #print "index = "+str(index)
        # black or red
        if 'B' in wildcard:
            deck = black_deck
        else:
            deck = red_deck
        for card in deck:
            fiveCardHand[index] = card
            #print "new card = %s fivCardHand = %s" % (card, fiveCardHand)
            all_hands.append(list(fiveCardHand))
            #print fiveCardHand
        #print all_hands
    elif len(cards_with_wildcards) == 2:
        first_wildcard = cards_with_wildcards[0]
        second_wildcard = cards_with_wildcards[1]
        first_index = fiveCardHand.index(first_wildcard)
        second_index = fiveCardHand.index(second_wildcard)
        if 'B' in first_wildcard:
            first_deck = black_deck
            second_deck = red_deck
        else:
            first_deck = red_deck
            second_deck = black_deck
        #print "Two wild cards"
        #print "first wild card = %s second wild card = %s" % (first_wildcard, second_wildcard)
        #print "first index = %s second index = %s" % (first_index, second_index)        
        for first_card in first_deck:
            fiveCardHand[first_index] = first_card
            for second_card in second_deck:
                fiveCardHand[second_index] = second_card
                all_hands.append(list(fiveCardHand))
                #print fiveCardHand
        # do something
    else:
        print "convert_wild_card: ERROR"
    # remember to return something
    return all_hands


def test_best_wild_hand():
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    return 'test_best_wild_hand passes'


def best_hand(hand = "JD TC TH 7C 7D 7S 7H".split()):
    "From a 7-card hand, return the best 5 card hand."
    #all_combos = itertools.combinations(hand, 5)
    #return max(all_combos, key=hand_rank)
    return max(itertools.combinations(hand,5), key=hand_rank)

    
# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 
    
def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

#print test_best_hand()
#print best_wild_hand()
#convert_wild_card()
print test_best_wild_hand()
