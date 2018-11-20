"""While loops continues to execute a block of code while some condition remains True
A while loop statement in Python programming language repeatedly executes a target
statement as long as a given condition is True.
syntax:
while expression:
    statement(s)"""

# simple while loop example
x = 0

while x < 5:
    x += 1
    print(f'The current value is {x}')

# using break keyword
while x < 5:
    x += 1
    break
    print(f'The current value is {x}')  # this line is unreachable
