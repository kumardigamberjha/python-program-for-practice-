n= int(input("Enter a number: "))
totsum= 0
while(n>0):
    dig= n%10
    totsum+= dig  #tot= tot + dig
    n//= 10
print("sum of digits of number is: ", totsum)