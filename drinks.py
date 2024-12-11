import random


def whatToDrink(base_liquor_options):
    base_liquor_dict = {
        'tequila': [
            'margarita',
            'original johnny silverhand',
            'tequila corpse reviver'],
        'gin': [
            'cooperstown',
            'martini (dry)',
            'martini (perfect)',
            'white negroni',
            'negroni',
            'the last word',
            'corpse reviver #2',
            'bees knees',
            'gin rickey'],
        'whiskey': [
            'boulevardier',
            'manhattan',
            'old fashioned',
            'whiskey sour',
            'gold rush',
            'whiskey highball'],
        'other': [
            'chirulin',
            'espresso martini',
            'sidecar',
            'straight absinthe',
            'protein cocktail abomination']
    }

    if len(base_liquor_options) == 0:
        chosen_liquor = random.choice(base_liquor_dict.keys())
    else:
        chosen_liquor = random.choice(base_liquor_options)

    return random.choice(base_liquor_dict[chosen_liquor])


liquor_list = ['gin', 'whiskey', 'tequila']
print(whatToDrink(base_liquor_options=liquor_list))

# print('margarita')
