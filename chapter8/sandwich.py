def make_sandwich(*ingredients):
    """Makes a sandwich with the user's choice of ingredients"""
    print("Preparing your sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f" - {ingredient}")
    print()