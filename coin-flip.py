import random
#heads and tails counter
hc=0
tc=0
for i in range(100): # same as range(0,100,1) or range(0,100)
    coin = random.randint(1,2)
    if coin == 1:
        print("heads ", hc," times")
        hc+=1
    else:
        print("tails ", tc," times")
        tc+=1
print(f"after 100 flips, we flipped {hc} heads, and {tc} tails.")