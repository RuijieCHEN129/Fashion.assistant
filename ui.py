def get_user_preferences():
    """
    Prompt user for age, weather, and occasion preferences.
    Returns a dict: {'age': int, 'weather': str, 'occasion': str}
    """
    while True:
        try:
            age = int(input("Enter your age: ").strip())
            break
        except ValueError:
            print("Please enter a valid integer for age.")
    weather = input("Enter current weather (sunny, rainy, cold, hot): ").strip().lower()
    occasion = input("Enter occasion (casual, work, outside for night): ").strip().lower()
    valid_occasions = {'casual', 'work', 'outside for night'}
    if occasion not in valid_occasions:
        print(f"Unknown occasion '{occasion}', defaulting to 'casual'.")
        occasion = 'casual'
    return {'age': age, 'weather': weather, 'occasion': occasion}


def display_suggestions(suggestions):
    """
    Display outfit suggestions and image paths.
    """
    if not suggestions:
        print("No matching outfits.")
        return
    print("\nRecommended outfits:")
    for idx, outfit in enumerate(suggestions, 1):
        print(f"{idx}. Top: {outfit['top']}, Bottom: {outfit['bottom']}, Shoes: {outfit['shoes']}")
        if outfit.get('image'):
            print(f"   Image: {outfit['image']}")


