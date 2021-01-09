# This program is a recap where I practice Python syntax and other basics.

# Below says hi and asks for name

print('Hi!')
print('what\'s your name?')
myName = input()

print(len(myName))
print('It\'s good to meet you ' + myName)

# Create custom function and call it
def spam():
    bacon = 100
    print(bacon)

spam()


# Input Validation: Try and Exception handling
def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero, whoops.')

print(div42by(2))
print(div42by(0))

print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) >= 4:
        print('That\'s a lot of cats.')
    elif int(numCats) < 0:
        print('You can\'t have negative cats...')
    else:
        print('That\'s not that many cats.')
except ValueError:
    print('Please enter a number.')
