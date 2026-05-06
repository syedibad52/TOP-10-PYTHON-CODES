no = 145

temp = no  

def fact(no):
    if no == 0 or no == 1:
        return 1
    else:
        return no * fact(no - 1)

sum = 0

while no > 0:
    rem = no % 10
    sum = sum + fact(rem)
    no = no // 10

if temp == sum:
    print("Strong number")
else:
    print("Not a strong number")