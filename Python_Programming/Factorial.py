n = int(input("Enter the no.: "))

f = 1

for i in range(1,n+1):
    f *= i

print("Factorial of",n,"is",f)