import random
onec=0
twoc=0
thrc=0
fourc=0
fivec=0
sixc=0
for i in range(100):
    die=random.randint(1,6)
    if die==1:
        print("1")
        onec+=1
    elif die==2:
        print("2")
        twoc+=1
    elif die==3:
        print("3")
        thrc+=1
    elif die==4:
        print("4")
        fourc+=1
    elif die==5:
        print("5")
        fivec+=1
    else:
        print("6")
        sixc+=1
print(f"after 100 rolls, we rolled {onec} one, {twoc} twos, {thrc} threes, {fourc} fours, {fivec} fives, and {sixc} sixes.")