no = 123456
odd = 0
even = 0

while no>0:

    rem = no%10
    if rem%2==0:
        even = even + 1
    else:
        odd = odd + 1
    no = no//10

print("The sum of the even digits in the given number is:",even)
print("The sum of the odd digits in the given number is:",odd)