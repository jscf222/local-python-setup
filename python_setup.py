print('Hello from inside a file!')
# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello():
    print('Hey there user!')
hello()

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(apple,carrot,banana):
    return[apple,carrot,banana]
print(pack('apple','carrot','banana'))


# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.

def eat_lunch(food):
    if len(food) == 0:
        print('First I eat carrots')
    else:
        for items in range(len(food)):
            if items == 0:
                print(f'Next I eat {food[0]}')
            else:
                print(f'My lunchbox is empty!')

eat_lunch([])
eat_lunch(["apple", "banana"])