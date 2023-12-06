# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:00:37 2023

@author: David
"""


# read file
f = open("input.txt", "r")
infos = f.read() 
infos = infos.split("\n")

tmp = infos[0].split(':')[1:][0].split(' ')
times = [];
for val in tmp: 
    if val.isdigit(): times.append(int(val));
    
tmp = infos[1].split(':')[1:][0].split(' ')
dists = [];
for val in tmp: 
    if val.isdigit(): dists.append(int(val));

ans = 1;
for i, time in enumerate(times):
    
    dist_travelled=[];
    for j in range(time+1):
        dist_travelled.append(j*(time-j));
        
    count = 0;
    for dist in dist_travelled:
        if dist>dists[i]:
            count+=1;
    print(count)
    
    if count>0:
        ans = ans*count;
print(ans)

#%%

tmp = infos[0].split(':')[1:][0].split(' ')
times = [];
for val in tmp: 
    if val.isdigit(): times.append(val);
long_time = times[0];
for time in times[1:]:
    long_time = long_time+time;
long_time = int(long_time)  

tmp = infos[1].split(':')[1:][0].split(' ')
dists = [];
for val in tmp: 
    if val.isdigit(): dists.append(val);
long_dist = dists[0];
for dist in dists[1:]:
    long_dist = long_dist+dist;
long_dist = int(long_dist)

    
dist_travelled=[];
for j in range(long_time+1):
    dist_travelled.append(j*(long_time-j));
    
count = 0;
for dist in dist_travelled:
    if dist>long_dist:
        count+=1;
print(count)
   
