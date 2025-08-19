

def getFibonaciSequence():
    first = 0
    second = 1
    fibonaciSequence = []
    for _ in range(51):
        result = first + second
        first = second
        second = result
        fibonaciSequence.append(result)
    return fibonaciSequence

    
    
def getElementFromFibonaciSequence(position):
    if type(position) is not int:
        return "error"
    else:
        return getFibonaciSequence()[position - 1]
    
print(getElementFromFibonaciSequence(5))