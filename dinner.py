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
                                               'snow peas']                     
          }                       

dinner_tonight = random.choice(list(dinners))
dinner_ingredient = dinners[dinner_tonight]
print ('Tonight\'s dinner is:' ,dinner_tonight, '\n')
print ('Please gather the following ingredients:\n'+'\n'.join(dinner_ingredient))
