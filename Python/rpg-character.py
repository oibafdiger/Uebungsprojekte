full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif not bool(name):
        return 'The character should have a name'
    elif len(name) >10:
        return 'The character name is too long'
    elif name.count(' '):
        return 'The character name should not contain spaces'

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int) :
        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif  ( strength + intelligence + charisma ) != 7:
        return 'The character should start with 7 points'

    strength_dots = full_dot * strength + empty_dot * (10 - strength)
    intelligence_dots = full_dot * intelligence + empty_dot * (10 - intelligence) 
    charisma_dots = full_dot * charisma + empty_dot * (10 - charisma) 
    return f'{name}\nSTR {strength_dots}\nINT {intelligence_dots}\nCHA {charisma_dots}'

print (create_character('Fabio', 3, 2, 2))