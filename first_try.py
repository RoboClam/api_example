if(True):
    print("I am true!")

if(False):
    print("I am true!")

def mult_two(firstValue,secondValue):
    print("A value: ")
    print(firstValue)

    print("B value: ")
    print(secondValue)
    return firstValue*secondValue

returnValue = mult_two(10, 10) # this is where the return comes back to

mult_two(returnValue, 5)

