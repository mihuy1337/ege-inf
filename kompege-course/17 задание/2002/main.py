nums = [int(i) for i in open('17_2002.txt')]

fours = [
    [nums[ind], nums[ind + 1], nums[ind + 2], nums[ind + 3]] for ind in range(0, len(nums)-3)
]
m = []
mn_sum = []
for four in fours:
    if (srt := sorted(four, reverse=True)) == four:
        if srt[0]-srt[-1] > 1000:
            m.append(four)
            mn_sum.append(sum(srt))
print(m, mn_sum)
print(len(m), min(mn_sum))