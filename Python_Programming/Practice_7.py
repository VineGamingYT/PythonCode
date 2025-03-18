#Sum of first n natural no. using recursion

n = int(input("Enter the number: "))

def calc_sum(a):
    if (a == 0):
        return 0
    return a + calc_sum(a-1)

res = calc_sum(n)
print("Sum of first",n,"natural no. is",res)