def my_function(counter):
    print("counter: {}".format(counter))

my_function(12)
print("------------")

def my_function(counter=89):
    return counter + 1

print(my_function())

print("-------------")

def my_function(counter=89):
    print("counter: {}".format(counter))

my_function()
