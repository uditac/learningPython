""" A Functional Breakfast """

def make_omelette(ingredients):
    print('Mixing the ingredients')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')
    omelette = 'a tasty omelette'
    return omelette

def make_pancake():
    print('Mixing the ingredients')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')
    pancake = 'a delicious pancake'
    return pancake

def coffee():
    print('Brewing the coffee')
    print('Pouring the coffee into a cup\n')
    coffee = 'a hot cup of coffee'
    pancake = 'a delicious pancake'
    return coffee,pancake

# make breakfast for two
barron_breakfast = make_omelette()
olivia_breakfast = make_pancake()
make_coffee = coffee()
print(f'Barron is having {barron_breakfast}\n')
print(f'Olivia is having {olivia_breakfast}\n')
print(f'Barron is having {make_coffee[0]} and {make_coffee[1]}\n')
