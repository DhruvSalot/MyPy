# Importing exit module for latter use:
import sys
# User input:
number = int(input("Enter a number: "))

# Defining collatz() function:
def collatz():
    global number
    if     number < 0:
               print ('The number should be a positive integer.')
               sys.exit()
    elif   number == 0 or number == 1:
               print (number)
               sys.exit()
    elif   number % 2 == 0 :
               print (number // 2)
               number = number // 2
    elif   number % 2 == 1:
               print (3 * number + 1)
               number = 3 * number + 1

# looping around using while :
while True:
    collatz()
