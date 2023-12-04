# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:31:18 2023

@author: David
"""

# read file
f = open("input.txt", "r")
code = f.read() 
code = code.split("\n")

def extract_numbers(line):
    
    # find numbers in this line    
    start_idx = [];
    stop_idx = [];
    this_num = [];
    all_nums = [];
    last_char_is_num = False;
    
    for idx, ch in enumerate(line): 
        #print(idx,ch)
        if (ch.isdigit()==True) & (last_char_is_num==False): 
            this_num = ch;
            start_idx.extend([idx]);            
            last_char_is_num = True;
            if (idx==len(line)-1):
                all_nums.extend([int(this_num)]);
                this_num = [];
                stop_idx.extend([idx]);
            else:
                continue;
            #print('start ',ch)
        if (ch.isdigit()==True) & (last_char_is_num==True):
            this_num = this_num+ch;
            if (idx==len(line)-1):
                all_nums.extend([int(this_num)]);
                this_num = [];
                stop_idx.extend([idx]);
            else:
                continue;            
            #print('append ',ch)
        if (ch.isdigit()==False) & (last_char_is_num==True):
            stop_idx.extend([idx-1]);
            last_char_is_num = False;
            all_nums.extend([int(this_num)]);
            this_num = [];
            continue;
            #print('stop ',ch)
        
    return all_nums, start_idx, stop_idx

def extract_symbols(line):
    
    symbol_idx = [];
    for i,ch in enumerate(line):
        if (not(ch.isdigit())) & (not(ch=='.')):
            symbol_idx.extend([i]);
    return symbol_idx



ans = 0;
for i, line in enumerate(code):
    
    print('##################################')
    
    # numbers of current line
    all_nums = []; start_idx = []; stop_idx = [];
    all_nums, start_idx, stop_idx = extract_numbers(line);
    
    # symbols of current line, above and below
    symbol_idx_this = []; symbol_idx_above = []; symbol_idx_below = [];
    symbol_idx_this = extract_symbols(line);
    if i>0: symbol_idx_above = extract_symbols(code[i-1]);
    if (i<len(code)-1): symbol_idx_below = extract_symbols(code[i+1]);
    
    if i>0: 
        print(i-1,code[i-1]);
        
    print(i,line);
    if (i<len(code)-1): 
        print(i+1,code[i+1]);
    
    
    for idx,num in enumerate(all_nums):
        
        # look for adjacent symbol
        adjacent_flag = False;
        
        for sx in symbol_idx_above: 
            if (start_idx[idx]==sx) | ((start_idx[idx]-1)==sx) | ((stop_idx[idx])==sx) | ((stop_idx[idx]+1)==sx) | (((start_idx[idx])<=sx) & ((stop_idx[idx])>=sx)):
                print('Line ',i,'Hit above: ',num);
                adjacent_flag = True;
        if i>0:
            for sx in symbol_idx_this: 
                if ((start_idx[idx]-1)==sx) | ((stop_idx[idx]+1)==sx):
                    print('Line ',i,'Hit this: ',num);
                    adjacent_flag = True;
        if (i<len(code)):
            for sx in symbol_idx_below: 
                if (start_idx[idx]==sx) | ((start_idx[idx]-1)==sx) | ((stop_idx[idx])==sx) | ((stop_idx[idx]+1)==sx) | (((start_idx[idx])<=sx) & ((stop_idx[idx])>=sx)):
                    print('Line ',i,'Hit below: ',num);
                    adjacent_flag = True;
                
        if (adjacent_flag==True):
            #print(ans,'+',num,'=',ans+num)
            ans += num;
    #print(ans)
    
    print('##################################')

print(ans)

#%% part 2

def extract_stars(line):
    
    symbol_idx = [];
    for i,ch in enumerate(line):
        if (ch=='*'):
            symbol_idx.extend([i]);
    return symbol_idx

ans = 0;
for i, line in enumerate(code):
    
    #print('##################################')
    
    # numbers of current line
    all_nums_this = []; start_idx_this = []; stop_idx_this = [];
    all_nums_this, start_idx_this, stop_idx_this = extract_numbers(line);
    
    # symbols of current line, above and below
    symbol_idx_this = []; 
    symbol_idx_this = extract_stars(line);

    if i>0: 
        #print(i-1,code[i-1]);
        all_nums_above = []; start_idx_above = []; stop_idx_above = [];
        all_nums_above, start_idx_above, stop_idx_above = extract_numbers(code[i-1]);
        
    #print(i,line);
    if (i<len(code)-1): 
        #print(i+1,code[i+1]);
        all_nums_below = []; start_idx_below = []; stop_idx_below= [];
        all_nums_below, start_idx_below, stop_idx_below= extract_numbers(code[i+1]);
    
    
    for idx,starpos in enumerate(symbol_idx_this):
        
        gear_part = [];
                
        for ii, part in enumerate(all_nums_this): 
            if (start_idx_this[ii]-1==starpos) | (stop_idx_this[ii]+1==starpos):
                #print('Line ',i,'Hit this: ',part);
                gear_part.extend([part]);
        for ii, part in enumerate(all_nums_above): 
            if ((start_idx_above[ii]-1<=starpos) & (stop_idx_above[ii]+1>=starpos)):
                #print('Line ',i,'Hit above: ',part);
                gear_part.extend([part]);
        for ii, part in enumerate(all_nums_below): 
            if ((start_idx_below[ii]-1<=starpos) & (stop_idx_below[ii]+1>=starpos)):
                #print('Line ',i,'Hit below: ',part);
                gear_part.extend([part]);
                
        print(gear_part)
        
        gear = 0;
        if (len(gear_part)>1): gear = gear_part[0]*gear_part[1];
        ans += gear;
    #print('##################################')

print(ans)