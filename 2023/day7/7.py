# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:53:00 2023

@author: David
"""


# read file
f = open("input.txt", "r")
puzzle = f.read() 
puzzle = puzzle.split("\n")
hands = [line.split(' ')[0] for line in puzzle];
bids = [int(line.split(' ')[1]) for line in puzzle];
index = list(range(len(hands)));

# implement a custom sort
sorted_hands = [];
sorted_bids = [];

def handtype:
    if len(set(list(hand))) == 1: # 5 of a kind
        t = 6;
    if len(set(list(hand))) == 2: # could be four of a kind or full house
        count = 0;
        for char in hand:
            if list(hand)[0] == char: count += 1;
        if (count == 1) | (count==4):
            t = 5;
        else:
            t = 4; # full house
    if len(set(list(hand))) == 3: # could be three of a kind or two pairs
        count = 0;
        for char in hand:
            if list(hand)[0] == char: count += 1;
        if count == 1:
            count = 0;
            for char in hand:
                if list(hand)[1] == char: count += 1;
                if count == 2:
                    t = 2;
                else:
                    t = 3;
        if count == 2:
            t = 2;
        if count == 3: 
            t = 3;
    if len(set(list(hand))) == 4: # one pair
        t = 1;
    if len(set(list(hand))) == 5: # high card
        t = 0;

    return t

def get_char_rank(a):
    if a.isdigit() == True:
        rank = int(a);
    else:
        if a == 'T':
            rank = 10;
        if a == 'J':
            rank = 11;
        if a == 'Q':
            rank = 12;
        if a == 'K':
            rank = 13;
        if a == 'A':
            rank = 14;    
    return rank

for i,hand in enumerate(hands):
    
    print(i,hand)
    if i == 0: sorted_hands.append(hand); sorted_bids.append(bids[i]); continue;
    
    keep_looking = True;
    cur_idx = 0;
    while (keep_looking==True) & (cur_idx<len(sorted_hands)):
        # for every hand, find the right place in the sorted list
        if get_type(hand) < get_type(sorted_hands[cur_idx]):
            sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]);
            keep_looking = False;
        if get_type(hand) == get_type(sorted_hands[cur_idx]):
            if not(hand[0]==sorted_hands[cur_idx][0]):
                if get_char_rank(hand[0]) < get_char_rank(sorted_hands[cur_idx][0]):
                    sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]);
                    keep_looking = False;
            else:
                if not(hand[1]==sorted_hands[cur_idx][1]):
                    if get_char_rank(hand[1]) < get_char_rank(sorted_hands[cur_idx][1]):
                        sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]);
                        keep_looking = False;
                else:
                    if not(hand[2]==sorted_hands[cur_idx][2]):
                        if get_char_rank(hand[2]) < get_char_rank(sorted_hands[cur_idx][2]):
                            sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]);
                            keep_looking = False;
                    else:
                        if not(hand[3]==sorted_hands[cur_idx][3]):
                            if get_char_rank(hand[3]) < get_char_rank(sorted_hands[cur_idx][3]):
                                sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]);
                                keep_looking = False;
                        else:
                            if not(hand[4]==sorted_hands[cur_idx][4]):
                                if get_char_rank(hand[4]) < get_char_rank(sorted_hands[cur_idx][4]):
                                    sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]);
                                    keep_looking = False;
            
          
        cur_idx += 1;
    
    if cur_idx == len(sorted_hands):
        sorted_hands.append(hand); sorted_bids.append(bids[i]);


ans = 0;
for i, bid in enumerate(sorted_bids):
    ans += (i+1)*bid;
    
print(ans)

#%% part 2

f = open("input.txt", "r")
puzzle = f.read() 
puzzle = puzzle.split("\n")
hands = [line.split(' ')[0] for line in puzzle];
bids = [int(line.split(' ')[1]) for line in puzzle];
index = list(range(len(hands)));

# implement a custom sort
sorted_hands = [];
sorted_bids = [];
sorted_types = [];

def get_type(hand):
    
    if len(set(list(hand))) == 1: # 5 of a kind
        t = 6;
    if len(set(list(hand))) == 2: # could be four of a kind or full house
        count = 0;
        for char in hand:
            if list(hand)[0] == char: count += 1;
        if (count == 1) | (count==4):
            t = 5;
        else:
            t = 4; # full house
    if len(set(list(hand))) == 3: # could be three of a kind or two pairs
        count = 0;
        for char in hand:
            if list(hand)[0] == char: count += 1;
        if count == 1:
            count = 0;
            for char in hand:
                if list(hand)[1] == char: count += 1;
                if count == 2:
                    t = 2;
                else:
                    t = 3;
        if count == 2:
            t = 2;
        if count == 3: 
            t = 3;
    if len(set(list(hand))) == 4: # one pair
        t = 1;
    if len(set(list(hand))) == 5: # high card
        t = 0;

    return t

def get_char_rank(a):
    if a.isdigit() == True:
        rank = int(a);
    else:
        if a == 'T':
            rank = 10;
        if a == 'J':
            rank = 1;
        if a == 'Q':
            rank = 12;
        if a == 'K':
            rank = 13;
        if a == 'A':
            rank = 14;    
    return rank

for i,hand in enumerate(hands):
    
    print(i,hand)
    handtype = get_type(hand);            
    
    joker = False; joker_position = [];
    for x,char in enumerate(hand): 
        if char == 'J': 
            joker = True;
            joker_position.append(x);


    if joker==True:
        if len(joker_position)>2: # if you have at least 3 jokers, always best to amke them all the same
            if len(set(list(hand)))==3: 
                handtype = 5;
            else:
                handtype = 6;
        if len(joker_position)==2:
            for x,pos in enumerate(['2','3','4','5','6','7','8','9','T','Q','K','A']):
                for y,pos2 in enumerate(['2','3','4','5','6','7','8','9','T','Q','K','A']):
                    tmp = list(hand);
                    tmp[joker_position[0]] = pos;
                    tmp[joker_position[1]] = pos2;
                    replaced_hand = ''.join(tmp)
                    if get_type(replaced_hand)>handtype:
                        handtype = get_type(replaced_hand);
        else:
            for x,pos in enumerate(['2','3','4','5','6','7','8','9','T','Q','K','A']):
                #print(hand.replace('J', pos))
                if get_type(hand.replace('J', pos))>handtype:
                    handtype = get_type(hand.replace('J', pos));
            
    if i == 0: sorted_hands.append(hand); sorted_bids.append(bids[i]); sorted_types.append(handtype); continue;

    
    keep_looking = True;
    cur_idx = 0;
    while (keep_looking==True) & (cur_idx<len(sorted_hands)):
        # for every hand, find the right place in the sorted list
        if handtype < sorted_types[cur_idx]:
            sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]); sorted_types.insert(cur_idx,handtype);
            keep_looking = False;
        if handtype == sorted_types[cur_idx]:
            if not(hand[0]==sorted_hands[cur_idx][0]):
                if get_char_rank(hand[0]) < get_char_rank(sorted_hands[cur_idx][0]):
                    sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]); sorted_types.insert(cur_idx,handtype);
                    keep_looking = False;
            else:
                if not(hand[1]==sorted_hands[cur_idx][1]):
                    if get_char_rank(hand[1]) < get_char_rank(sorted_hands[cur_idx][1]):
                        sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]); sorted_types.insert(cur_idx,handtype);
                        keep_looking = False;
                else:
                    if not(hand[2]==sorted_hands[cur_idx][2]):
                        if get_char_rank(hand[2]) < get_char_rank(sorted_hands[cur_idx][2]):
                            sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]); sorted_types.insert(cur_idx,handtype);
                            keep_looking = False;
                    else:
                        if not(hand[3]==sorted_hands[cur_idx][3]):
                            if get_char_rank(hand[3]) < get_char_rank(sorted_hands[cur_idx][3]):
                                sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]); sorted_types.insert(cur_idx,handtype);
                                keep_looking = False;
                        else:
                            if not(hand[4]==sorted_hands[cur_idx][4]):
                                if get_char_rank(hand[4]) < get_char_rank(sorted_hands[cur_idx][4]):
                                    sorted_hands.insert(cur_idx,hand); sorted_bids.insert(cur_idx,bids[i]); sorted_types.insert(cur_idx,handtype);
                                    keep_looking = False;
            
          
        cur_idx += 1;
    
    if cur_idx == len(sorted_hands):
        sorted_hands.append(hand); sorted_bids.append(bids[i]); sorted_types.append(handtype);


ans = 0;
for i, bid in enumerate(sorted_bids):
    ans += (i+1)*bid;
    
print(ans)
