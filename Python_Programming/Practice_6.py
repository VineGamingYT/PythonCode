#Sum of first n natural no. using loops in a simple function

n = int(input("Enter the number: "))

def calc_sum(a):
    sum = 0
    for i in range(1,a+1):
        sum += i
    return sum

res = calc_sum(n)
print("Sum of first",n,"natural no. is",res)