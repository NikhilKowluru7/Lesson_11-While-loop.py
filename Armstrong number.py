number = int(input("Enter the number you want to find the armstrong to: "))
temp = number
sum = 0
while temp>0:
    digit = temp%10
    sum = sum+digit**3
    temp=temp//10
if sum ==number:
    print("Your number is an armstrong!")
else:
    print("Your number is not an armstrong!")