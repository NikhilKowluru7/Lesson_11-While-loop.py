number = int(input("Enter a number: "))

if number < 0:
    number = -number

count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number //= 10
        count += 1

print("There are",count,"digits!")
