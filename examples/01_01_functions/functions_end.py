""" A Functional Breakfast """

def make_omelette():
    print('Mixing the ingredients')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')
    omelette = 'a tasty omelette'
    nothing = 'nothing'
    test = 'test'
    return omelette,nothing,test

# make breakfast for two
barron_breakfast = make_omelette()
olivia_breakfast = make_omelette()
udita_breakfast = make_omelette()
print(f'Barron is having {barron_breakfast[0]}\n')
print(f'Olivia is having {olivia_breakfast[1]}\n')
print(f'Udita is having {udita_breakfast[2]}\n')
