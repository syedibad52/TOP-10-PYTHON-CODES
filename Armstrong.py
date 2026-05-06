no = 153

temp = no
t = no
c = 0

while no>0:

    rem =no%10
    c =c+1
    no =no//10
sum = 0
while temp>0:
    rem = temp%10
    sum = sum + rem**c
    temp = temp//10

if sum == t:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
