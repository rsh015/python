#!/usr/bin/env python3

import random

dinners = {'tuna melt'                      : ['tuna in water',
                                               'mayonnaise',
                                               'celery',
                                               'carrots',
                                               'sweet pickle relish',
                                               'hot sauce',
                                               'salt and pepper',
                                               'american cheese',
                                               'tomatoes'],
                                              
           'Sweet and spicy shrimp stir fry': ['cellophane noodles',
                                               'low sodium soy sauce',
                                               'low sodium chicken broth or water',
                                               'light brown sugar',
                                               'cornstarch',
                                               'chilli garlic paste',
                                               'sesame oil',
                                               'vegetable oil',
                                               'miced garlic',
                                               'sweet red peppers',
                                               'onion',
                                               'baby spinach',
                                               'shrimp',
                                               'snow peas'],

           'Seared shrimp with chard'       : ['shrimp',
                                               'kosher salt',
                                               'chard',
                                               'extra virgin olive oil',
                                               'garlic',
                                               'red chile',
                                               'shallot',
                                               'grated ginger',
                                               'light brown sugar',
                                               'black pepper',
                                               'sherry vinegar',
                                               'cilantro'],

           'Bacon and broccoli rice bowl'   : ['white rice',
                                               'bacon',
                                               'broccoli',
                                               'soy sauce',
                                               'sesame oil',
                                               'eggs',
                                               'kosher salt',
                                               'cilantro',
                                               'scalions',
                                               'pickled jalapenos']

          }

dinner_tonight = random.choice(list(dinners))
dinner_ingredient = dinners[dinner_tonight]
size = len(dinner_ingredient)
banner = len(dinner_tonight)
banner1 = len('tonight\'s dinner is')
total_banner_len = banner + banner1 + 1
print ('*'*total_banner_len + '\nTonight\'s dinner is' ,dinner_tonight + '\n' + '*' * total_banner_len + '\n')
#print ('Please gather the following ingredients:\n' + '\n' +'\n'.join(dinner_ingredient))
print ('Please gather the following ingredients:\n')
for i in list(range(1,size+1)):
    print(str(i) + '. ' + dinner_ingredient[i-1])
