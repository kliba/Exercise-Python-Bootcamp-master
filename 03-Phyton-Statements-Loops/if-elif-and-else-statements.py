"""Decision making is required when we want to execute a code only if a certain condition is satisfied.
The if…elif…else statement is used in Python for decision making.
Control Flow syntax makes use of colons and indentation (whitespace)
This indentation system is crucial to Python and is what sets it apart from other programming languages
eg:
if some_condition:
    # execute some code
elif some_other_condition:
    # do something different
else:
    # do something else"""

# single if statement
hungry = True

if hungry:
    print('Feed me')

# using if and else statement
hungry = False

if hungry:
    print("Feed me")
else:
    print("I am not hungry")

# using if, elif and else
hungry = False
thirsty = True

if hungry and thirsty:
    print('Give me some food and soda')
elif hungry and not thirsty:  # we can use elif any time as we want. it has to be between if and else
    print('Give me food')
elif not hungry and thirsty:
    print('Give me soda, please')
else:
    print('I am fine, I do not need food and drink')
