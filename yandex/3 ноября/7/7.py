from math import *

for i in range(1, 10000):
    v_vid = 640*480*24*i
    v_aud = 1*24*1000*8
    if 25*(1024*1024*1024*8)/(60*60)>v_vid+v_aud:
        print(2**i)
        
