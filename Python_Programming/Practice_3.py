i = 0
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue    #skip the statement in the current iteration
    print(i)
    i += 1