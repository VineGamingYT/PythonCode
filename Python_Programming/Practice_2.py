a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

print(a)
val = int(input("Enter the value to searched from the above tuple: "))

i = 0

while i < len(a) :
    if(val == a[i]):
        print("Value found at index:", i)
        break
    i += 1

if(i == len(a)):
    print("Value not Found!")

#Program Ends