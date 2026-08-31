def add_setting(settings,key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()
    
    if key in settings:
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
     
    settings[key]=value
    return(f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(settings, key_value):
    key= key_value[0].lower()
    value = key_value[1].lower()
    if key in settings: 
        settings[key]=value
        return(f"Setting '{key}' updated to '{value}' successfully!")
    else: 
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(settings, key):
    key = key.lower()
    if key in settings: 
        removed_key_value = settings.pop(key)
        return(f"Setting '{key}' deleted successfully!")
    else:
        return(f"Setting not found!")

def view_settings(settings):
    if not settings:
        return("No settings available.")
    else:
        result = "Current User Settings:\n"
        for key, value in settings.items():
            result += key.capitalize() + ": " + value + "\n"
        return result
        

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}