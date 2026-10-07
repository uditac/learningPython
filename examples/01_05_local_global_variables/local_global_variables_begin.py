""" A Functional Breakfast """
cheese = 'cheddar cheese'
def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')

def make_omelette():
    cheese = 'swiss cheese'
    mix_and_cook()
    omelette = f'a {cheese} omelette'
    return omelette

def make_pancake():
    global cheese
    cheese = 'cheddar cheese'
    mix_and_cook()
    pancake = f'a {cheese} pancake'
    return pancake

# make breakfast for two
print(f'globalCheese is {cheese}\n')
barron_breakfast = make_omelette()
print(f'global Cheese is {cheese}\n')
olivia_breakfast = make_pancake()
print(f'global Cheese is {cheese}\n')
print(f'Barron is having {barron_breakfast}\n')
print(f'Olivia is having {olivia_breakfast}\n')
