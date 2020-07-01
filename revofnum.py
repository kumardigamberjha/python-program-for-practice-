n = int(input("Enter a number you want to be reversed: "))
rev = 0

while(n>0):
    dig= n%10
    print("dig ", dig)
    rev= rev*10 + dig
    print("rev: ", rev)
    n//= 10 
    print("n: ", n)
print("The rev of number is: ", rev)





