
lst = list(range(1, 100))

print("Multiples of 5 and 6")
for x in lst:
    if x % 5 == 0 and x % 6 == 0:
        print(x, end=" ")
