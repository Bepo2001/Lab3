numbers=[]
while True:
    value = int(input("enter value"))
    numbers.append(value)
    if  len(numbers)==10:
        numbers.sort()
        break

print(numbers[-1])
