cars=['audi','ferrari','ford focus','toyota sienna hybrid']
groceries=['grapes','oranges','bananas']
def car_adder(thing_to_add,target_list):
    if thing_to_add[0].lower() in 'abcdefg':
        print("This car starts with A-G")
        target_list.append(thing_to_add)
    else:
        print("This car starts with H-Z and we are not allowing it in our club")
car_adder('bmw',cars)
car_adder('honda',cars)
car_adder('cinnamon',groceries)
car_adder('apples',groceries)
print(cars)
print(groceries)
def addTwo(num):
    return num+2
print(addTwo(3))
def addThree(num):
    return num+3
print(addThree(addTwo(5)))
def namePrinter(first, last, middle=''):
    return f"The name's {last}, {first} {middle} {last}."
print(namePrinter("James","Bond","Freddy"))
def giveMeMyGroceries(thing_to_add):
    grocery_list=['graped','oranges','bananas']
    grocery_list.append(thing_to_add)
    return grocery_list
print(giveMeMyGroceries('spaghetti'))