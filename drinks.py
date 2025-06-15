import random
from datetime import datetime


def whatToDrink(base_liquor_options):
    base_liquor_dict = {
        'tequila': [
            'margarita',
            'original johnny silverhand',
            'tequila corpse reviver',
            'tequila soda',
            'french intervention',
            'naked & famous'],
        'gin': [
            'cooperstown',
            'martini (dry)',
            'martini (perfect)',
            'martini (dirty)',
            'white negroni',
            'negroni',
            'the last word',
            'corpse reviver #2',
            'bees knees',
            'gin rickey',
            'alaska',
            'french pearl',
            'perfect white negroni (from the Wells in DC)',
            'bijou'],
        'whiskey': [
            'boulevardier',
            'manhattan',
            'old fashioned',
            'whiskey sour',
            'gold rush',
            'whiskey highball',
            'whiskey & coke',
            'pickleback shot',
            'Snoopy'],
        'absinthe': [
            'straight absinthe with sugar',
            'necromancer'],
        'rum': [
            'mai tai',
            'rum old fashioned'
        ],
        'non-liquor': [
            'blue moon',
            'guinness',
            'cranberry long drink',
            'peach long drink',
        ],
        'other': [
            'chirulin',
            'pisco sour',
            'espresso martini',
            'sidecar',
            'protein cocktail abomination']
    }

    # random.seed(datetime.now().timestamp())

    # weighted_liquors = []
    # for liquor in base_liquor_options:
    #     for cocktail in base_liquor_dict[liquor]:
    #         weighted_liquors.append(liquor)
    # chosen_liquor = random.choice(weighted_liquors)
    chosen_liquor = random.choice(base_liquor_options)

    chosen_liquor_string = "Base: " + chosen_liquor
    cocktail_string = "Cocktail: " + \
        random.choice(base_liquor_dict[chosen_liquor])
    return "==================\n" + chosen_liquor_string + "\n" + cocktail_string + "\n=================="


liquor_list = [
    'gin',
    'whiskey',
    # 'tequila',
    'absinthe',
    'rum'
    # 'non-liquor',
    # 'other'
]
print(whatToDrink(liquor_list))
# print(whatToDrink(['whiskey']))
