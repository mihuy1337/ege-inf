from itertools import *
count = 0
for i in permutations('АБИКОЛУН', 8):
    stroke = ''.join(i)
    stroke_new = stroke.replace('Б', 'Н')\
        .replace('К', 'Н')\
        .replace('Л', 'Н')\
        .replace('И', 'А')\
        .replace('О', 'А')\
        .replace('У', 'А')

    if ('НН' not in stroke_new) and ('АА' not in stroke_new):
        print(stroke_new, stroke)
        count+=1

print(count)