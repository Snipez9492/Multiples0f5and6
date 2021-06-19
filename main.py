lst = list(range(1, 100))

print("Multiples of 5 and 6")
for x in lst:
    if x % 5 == 0 and x % 6 == 0:
        print(x, end=" ")

print("-" * 20)
print("Multiples of 5 and 6, using list comprehension.")
nums = [i for i in lst if i % 5 == 0 and i % 6 == 0]
print(nums)
