no = 19

while no != 1 and no != 4:
    sum = 0
    while no > 0:
        rem = no % 10
        sum += rem * rem
        no = no // 10
    no = sum

if no == 1:
    print("Happy number")
else:
    print("Sad number")