def greet_user(name):
    """
    Function to greet the user with their name.
    
    Args:
        name (str): The name of the user.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the application."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))