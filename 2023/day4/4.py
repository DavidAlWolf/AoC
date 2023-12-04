# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:56:36 2023

@author: David
"""


# read file
f = open("input.txt", "r")
cards = f.read() 
cards = cards.split("\n")


ans = 0;
for card in cards:
    tmp = card.split("|");
    numbers_you_have = tmp[-1];
    numbers_you_have = numbers_you_have.split(" ")
    numbers = [];
    for num in numbers_you_have: 
        if num.isdigit(): numbers.extend([int(num)]);
    tmp = tmp[0].split(":")
    winning_numbers = tmp[1];
    winning_numbers = winning_numbers.split(" ")
    winners = [];
    for num in winning_numbers: 
        if num.isdigit(): winners.extend([int(num)]);
        
        
    hits = 0;
    for num in numbers:
        for win_num in winners:
            if num==win_num: 
                #print("Hit! ", num)
                hits += 1;
                
    score = 0;
    if hits>0: score = 2**(hits-1);
    
    ans += score;
 
print(ans)
    
#%% part 2


ans = 0;
copy_numbers = [1]*len(cards);
for i, card in enumerate(cards):
    tmp = card.split("|");
    numbers_you_have = tmp[-1];
    numbers_you_have = numbers_you_have.split(" ")
    numbers = [];
    for num in numbers_you_have: 
        if num.isdigit(): numbers.extend([int(num)]);
    tmp = tmp[0].split(":")
    winning_numbers = tmp[1];
    winning_numbers = winning_numbers.split(" ")
    winners = [];
    for num in winning_numbers: 
        if num.isdigit(): winners.extend([int(num)]);
        
    for cnv in range(copy_numbers[i]):
        hits = 0;
        for num in numbers:
            for win_num in winners:
                if num==win_num: 
                    #print("Hit! ", num)
                    hits += 1;
                
        for add in range(hits):
            if ((i+add+1)<len(copy_numbers))==True:
                copy_numbers[i+add+1] = copy_numbers[i+add+1] + 1; 
        
                
for x in copy_numbers: ans += x;
print(ans)
                
    