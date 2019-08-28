#Variable
name = "Seungwook"
nationality = "Korea"
phone_number = "010-6641-6667"

print("Hi, my name is %s. I'm from %s" % (name, nationality))
print("My phone number is %s." % (phone_number))

#Function
def hello():
    print("Hello World!")
    print("My name is Kevin")

hello()

#Parameter
def hello(name):
    print("Hello %s!" %(name))
    print("My name is Kevin")

hello("Emily")

def print_sum(a,b):
    print(a+b)

print_sum(3,5)