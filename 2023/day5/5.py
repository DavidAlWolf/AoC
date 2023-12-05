# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:36:09 2023

@author: David
"""


# read file
f = open("input.txt", "r")
almanac = f.read() 
almanac = almanac.split("\n")

seeds = almanac[0];
seeds = seeds.split(" ");
seeds.remove("seeds:")
seed_to_soil = almanac[3:18];
soil_to_fert = almanac[21:38];
fert_to_water = almanac[41:80];
water_to_light = almanac[83:98];
light_to_temp = almanac[101:140];
temp_to_hum = almanac[143:180];
hum_to_loc = almanac[183:];

def apply_map(source_number, input_map):

    destination_number = source_number;    
    
    for line in input_map:
        
        vals = line.split(" ");
        cur_dest = int(vals[0]);
        cur_source = int(vals[1]);
        cur_range = int(vals[2]);
        
        if ((source_number>=cur_source) & (source_number<=(cur_source+cur_range))):
            #print('Found map entry');
            destination_number = cur_dest+(source_number-cur_source);
        
        
    #     if (cur_range>0):
    #         for i in range(cur_range):
    #             source.extend([cur_source+i]);
    #             destination.extend([cur_dest+i]);
        
    # for idx, mapping in enumerate(source):
    #     if (source_number==mapping):
    #         destination_number=destination[idx];
    #         print('Found map entry');
    
    return destination_number

#%% part 1
locations = [];
for seed in seeds:
    #print('Seed: ',seed)
    locations.extend([apply_map(apply_map(apply_map(apply_map(apply_map(apply_map((apply_map(int(seed),seed_to_soil)),soil_to_fert),fert_to_water),water_to_light),light_to_temp),temp_to_hum),hum_to_loc)])
    
print(min(locations))

#%% part 2

def inverse_map(destination_number, input_map):

    source_number = destination_number;    
    
    for line in input_map:
        
        vals = line.split(" ");
        cur_dest = int(vals[0]);
        cur_source = int(vals[1]);
        cur_range = int(vals[2]);
        
        if ((destination_number>=cur_dest) & (destination_number<=(cur_dest+cur_range))):
            #print('Found map entry');
            source_number = cur_source+(destination_number-cur_dest);
        
    return source_number;
        
# expand seeds
seeds = almanac[0];
seeds = seeds.split(" ");
seeds.remove("seeds:")

i=0;
found_seed = False;
while (found_seed==False):
    if (i%1000000==0):
        print(i)
    put_seed = inverse_map(inverse_map(inverse_map(inverse_map(inverse_map(inverse_map(inverse_map(i,hum_to_loc),temp_to_hum),light_to_temp),water_to_light),fert_to_water),soil_to_fert),seed_to_soil);
    for j in range(0,len(seeds),2):
        if ((put_seed>=int(seeds[j])) & (put_seed<=(int(seeds[j])+int(seeds[j+1])))):
            print('Found minimum:',i)
            found_seed=True;
        
    i+=1;


    
    