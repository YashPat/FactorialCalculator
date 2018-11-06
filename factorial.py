def factorial(x):
    temp = str(x)
    list = []
    total = 0
    firstTime = True
    for a in range(x):
        list.append(a+1)
    for b in list:
        if firstTime == True:
            total += int(b)
            firstTime = False
        if firstTime == False:
            total *= int(b)
    return total

print (factorial(int(input("Enter a number to calculate a factorial for: "))))