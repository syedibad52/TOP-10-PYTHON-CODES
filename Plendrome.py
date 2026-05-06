no = 121

temp = no
rev = 0

while no > 0:
    rem = no % 10
    rev = rev * 10 + rem
    no = no // 10

if rev == temp:
    print("Palindrome")
else:
    print("Not a palindrome")