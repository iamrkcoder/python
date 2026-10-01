#sum of digits
num = 12345
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print("Sum = ", sum)

#count number

num = 123456
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits =", count)
 

