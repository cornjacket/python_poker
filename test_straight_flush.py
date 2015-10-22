def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    #pick first element ranks[0] and build and array from it
    start = ranks[0]
    stop  = ranks[0]-5
    match = range(start,stop,-1) # decending order
    if ranks == match:
        return True
    return False

if not straight([10, 9, 8, 7, 6]):
    print "Error 1 1"
    
if straight([10, 6, 5, 4, 2]):
    print "Error 1 2"


def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
    suits = [s for r,s in hand] # grab the suits
    kind  = suits[0]
    for suit in suits:
        if suit != kind:
            return False
    return True

if not flush(["TC","AC","KC","QC","9C"]):
    print "Error 2 1"
if flush(["TC","AC","KC","QC","9D"]):
    print "Error 2 2"


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
    

def my_two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # see my notes for explanation of algorithm
    return_value = () # empty set
    count = 0 # if this gets to 4, then we have two pair
    for r in ranks:
        if ranks.count(r) == 2:
            count += 1
            # need to check if r is in return value already before adding
            if r not in return_value:
                return_value = return_value + (r,) # add r to the tuple
    if count == 4: return return_value
    return None
            
                


if not kind(4,[10, 10, 10, 10, 7]) == 10:   print "Error 3 1"
if not kind(3,[10, 10, 10, 10, 7]) == None: print "Error 3 2"
if not kind(3,[14, 13, 8, 8, 8]) == 8:      print "Error 3 3"
if not kind(2,[14, 13, 8, 8, 8]) == None:   print "Error 3 4"
if not kind(2,[14, 13, 12, 7, 7]) == 7:     print "Error 3 5"
if not kind(1,[14, 13, 12, 7, 7]) == 14:    print "Error 3 6"



if not two_pair([10,10,10,10,7]) == None: print "Error 4 1"
if not two_pair([10,10,7,7,5]) == (10,7): print "Error 4 2"
if not two_pair([10,10,10,5,5]) == None:  print "Error 4 3"
if not two_pair([10,3,3,2,2]) == (3,2):   print "Error 4 4"

print "No news is good news"
