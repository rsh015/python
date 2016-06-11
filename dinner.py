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

           'Seared Shrimp With Chard'       : ['shrimp',
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
                                               'cilantro']
          }

dinner_tonight = random.choice(list(dinners))
dinner_ingredient = dinners[dinner_tonight]
banner = len(dinner_tonight)
banner1 = len('tonight\'s dinner is')
total_banner_len = banner + banner1 + 1
print ('*'*total_banner_len + '\nTonight\'s dinner is' ,dinner_tonight + '\n' + '*' * total_banner_len + '\n')
print ('Please gather the following ingredients:\n'+'-' * 40 + '\n' +'\n'.join(dinner_ingredient))
