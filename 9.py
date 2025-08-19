numbers = [1, 1, [1, [1], [4, 1]]]

def sumArray(array):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += sumArray(element)
        else:
            sum += element

    return sum

    

print(sumArray(numbers))