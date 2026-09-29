username = input("enter the username: ")

def validate_username(username):
    if len(username) < 3 or len(username) > 30:
        return False, "Username must be between 3 - 30 characters long."
    if username[0].isdigit():
        return False, "Username cannot start with a digit."
    
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890._"
    for char in username:
        if char not in allowed_chars:
            return False, "Username contains forbidden characters."
    if ".." in username or "__" in username:
        return False, "Username cannot contain consecutive periods or underscores."
    if not any(char.isalpha() for char in username):
        return False, "Username must contain at least one letter."
    return True, "Username is valid."
is_valid, message = validate_username(username)


def suggest_handles(username):
    suggestions = []

    suggestion1 = username[:10] + "_1"
    suggestions.append(suggestion1)

    cleaned = ""
    for char in username:
        if char.isalnum() or char in "._":
            cleaned += char 
    if cleaned:
        suggestions.append(cleaned[:20]) 

    if username[0].isdigit():
        suggestion3 = "harsh_" + username[:15]
        suggestions.append(suggestion3)
    else:
        suggestion3 = username[:15] + "_yt"
        suggestions.append(suggestion3)

    return suggestions 

is_valid, message = validate_username(username)
print(f"\n{message}")

if not is_valid:
    print("\nSuggestions:")
    suggestions = suggest_handles(username)
    for i, suggestion in enumerate(suggestions, start=1):
        print(f"{i}. {suggestion}")



