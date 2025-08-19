numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddList = []
evenList = []
for n in numbers:
    if n % 2 == 0:
        evenList.append(n)
    else:
        oddList.append(n)

print(f"even list: {evenList}, odd List: {oddList}")