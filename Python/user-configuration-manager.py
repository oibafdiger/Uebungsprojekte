
def add_setting(dictionary, tuple_key_value):
    key, value = tuple_key_value
    key = key.lower()
    value = value.lower()

    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    dictionary.update({key : value})
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, tuple_key_value):
    key, value = tuple_key_value
    key = key.lower()
    value = value.lower()

    if key not in dictionary:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    dictionary.update({key : value})
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(dictionary, key):
    key = key.lower()
    if not dictionary:
        return 'No settings available.'
    
    if key not in dictionary:
        return 'Setting not found!'

    del dictionary[key]
    return f"Setting '{key}' deleted successfully!"

def view_settings(dictionary):
    if not bool(dictionary) or not isinstance(dictionary, dict):
        return 'No settings available.'
    result = ''
    result += 'Current User Settings:\n'
    for setting, value in dictionary.items():
        result += setting.capitalize() + ': ' + value + '\n'
    
    return result


test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
