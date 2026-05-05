no = 123
mul = 1

while no > 0:
    rem = no % 10
    mul = mul * rem
    no = no // 10

print("Multiplication of digits:", mul)