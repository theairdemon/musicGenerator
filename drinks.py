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
            'white negroni',
            'negroni',
            'the last word',
            'corpse reviver #2',
            'bees knees'],
        'whiskey': [
            'boulevardier',
            'manhattan',
            'old fashioned',
            'whiskey sour',
            'gold rush'],
        'other': [
            'chirulin',
            'espresso martini',
            'sidecar']
    }

    if len(base_liquor_options) == 0:
        chosen_liquor = random.choice(base_liquor_dict.keys())
    else:
        chosen_liquor = random.choice(base_liquor_options)

    return random.choice(base_liquor_dict[chosen_liquor])


print(whatToDrink(base_liquor_options=['tequila', 'gin', 'whiskey']))
