x = 5


def x_is_one():
    x = 1
    print(x)


print(x)

# x printed is local variable x
x_is_one()

print(x)


def x_is_two():
    global x
    x = 2
    print(x)


# global statement in x_is_two() changes x value to 2
x_is_two()

# x printed is now 2 because x_is_two() has changed global x to 2
print (x)


def next_number():
    global x
    x = x + 1


x = 0
print(x)
next_number()
print(x)
