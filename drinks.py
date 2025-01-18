import random


def whatToDrink(base_liquor_options):
    base_liquor_dict = {
        'tequila': [
            'margarita',
            'original johnny silverhand',
            'tequila corpse reviver',
            'tequila soda',
            'french intervention'],
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
            'gin rickey'],
        'whiskey': [
            'boulevardier',
            'manhattan',
            'old fashioned',
            'whiskey sour',
            'gold rush',
            'whiskey highball',
            'whiskey & coke'],
        'absinthe': [
            'straight absinthe with sugar',
            'necromancer'],
        'other': [
            'chirulin',
            'pisco sour',
            'espresso martini',
            'sidecar',
            'protein cocktail abomination']
    }

    weighted_liquors = []
    for liquor in base_liquor_options:
        for cocktail in base_liquor_dict[liquor]:
            weighted_liquors.append(liquor)
    chosen_liquor = random.choice(weighted_liquors)

    chosen_liquor_string = "Base: " + chosen_liquor
    cocktail_string = "Cocktail: " + \
        random.choice(base_liquor_dict[chosen_liquor])
    return "==================\n" + chosen_liquor_string + "\n" + cocktail_string + "\n=================="


liquor_list = ['gin', 'whiskey', 'tequila', 'absinthe']
print(whatToDrink(liquor_list))
