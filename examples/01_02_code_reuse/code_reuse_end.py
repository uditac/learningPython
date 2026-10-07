""" A Functional Breakfast """

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')

def make_chicken():
    #mix_and_cook()
    chicken = 'a juicy chicken'
    return chicken

def make_omelette(ingredients):
    mix_and_cook()
    make_chicken()
    omelette = f'a {ingredients} omelette'
    return omelette

def make_pancake(ingredients):
    mix_and_cook()
    pancake = f'a {ingredients} pancake'
    return pancake

# make breakfast for two
barron_breakfast = make_omelette('cheese')  
olivia_breakfast = make_pancake('bacon')
#udita_breakfast = make_chicken()
print(f'Barron is having {barron_breakfast}\n')
print(f'Olivia is having {olivia_breakfast}\n')
#print(f'Udita is having {udita_breakfast}\n')
