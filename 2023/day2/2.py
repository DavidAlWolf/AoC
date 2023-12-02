# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:00:27 2023

@author: David
"""

# read file
f = open("input.txt", "r")
games = f.read() 
games = games.split("G")

ans = 0;

for id,game in enumerate(games):
    #print(game)
    this_game = game.split(';');
    #print(this_game)
    
    impossible = False;
    for this_round in this_game:
        # get numbers of balls
        num_blue = 0;
        num_green = 0;
        num_red = 0;
        for i, c in enumerate(this_round):
            if this_round[i:].startswith('blue'): 
                num_blue = int(this_round[i-3]+this_round[i-2]);
            if this_round[i:].startswith('green'): 
                num_green = int(this_round[i-3]+this_round[i-2]);
            if this_round[i:].startswith('red'): 
                num_red = int(this_round[i-3]+this_round[i-2]);
        
        print(num_blue,num_green,num_red)
        if num_blue > 14: impossible = True;
        if num_green > 13: impossible = True;
        if num_red > 12: impossible = True;
        
        
    if impossible==False: 
        print(id)
        ans += id;
    
print(ans)

#%%
## part 2
games.remove('')
ans = 0;
for id,game in enumerate(games):
    #print(game)
    this_game = game.split(';');
    #print(this_game)
    
    all_blue = []; min_blue = 1;
    all_green = []; min_green = 1;
    all_red = []; min_red = 1;
    for this_round in this_game:
        # get numbers of balls
        for i, c in enumerate(this_round):
            if this_round[i:].startswith('blue'): 
                all_blue.extend([int(this_round[i-3]+this_round[i-2])]);
            if this_round[i:].startswith('green'): 
                all_green.extend([int(this_round[i-3]+this_round[i-2])]);
            if this_round[i:].startswith('red'): 
                all_red.extend([int(this_round[i-3]+this_round[i-2])]);
        
    if len(all_blue)>0: min_blue = max(all_blue);
    if len(all_green)>0: min_green = max(all_green);
    if len(all_red)>0: min_red = max(all_red);
    
    print(min_blue,min_green,min_red)
    power = min_blue*min_green*min_red;
    print(power)
    print(ans)
    ans += power;
    
print(ans)