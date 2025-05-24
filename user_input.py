CUISINE_OPTIONS = {
    1: "Australian",
    2: "Chinese",
    3: "Western",
    4: "Japanese",
    5: "Thai",
    6: "Indian",
    7: "Korean"
}

def get_user_preferences():
    #Collect user preferences for dish filtering
    print("\n=== Set Your Dining Preferences ===")
    
    # Cuisine selection
    print("Available cuisines: 1.Australian 2.Chinese 3.Western 4.Japanese 5.Thai 6.Indian 7.Korean (enter numbers separated by commas)")
    cuisine_choice = input("Select cuisines (press enter to skip): ").strip()
    selected_cuisines = []
    if cuisine_choice:
        selected_ids = [int(id) for id in cuisine_choice.split(",")]
        selected_cuisines = [CUISINE_OPTIONS[id] for id in selected_ids]
    
    # Spicy preference
    reject_spicy = input("Avoid spicy dishes?🌶️🌶️ (y/n): ").lower() == "y"
    
    # Budget selection
    budget = input("Budget option💰💰: 1.Low 2.Medium 3.High (enter number, press enter to skip): ").strip()
    budget_options = {"1": "low", "2": "medium", "3": "high"}
    selected_budget = budget_options.get(budget, None)
    
    # Calorie limit
    max_calories = None
    if input("Set calorie limit?🍔 (y/n): ").lower() == "y":
        max_calories = int(input("Enter maximum calories (e.g. 500): "))
    
    return {
        "cuisines": selected_cuisines,
        "reject_spicy": reject_spicy,
        "budget": selected_budget,
        "max_calories": max_calories
    }

def get_new_dish_input():
    # Collect new dish details with validation
    print("\n=== Add New Dish ===")
    
    # Name
    name = input("Dish name: ").strip()
    while not name:
        print("⚠️⚠️Name cannot be empty!")
        name = input("Dish name: ").strip()
    
    # Cuisine
    print("Select cuisine (enter number):")
    for num, cuisine in CUISINE_OPTIONS.items():
        print(f"{num}. {cuisine}")
    cuisine_choice = input("> ").strip()
    while not cuisine_choice.isdigit() or int(cuisine_choice) not in CUISINE_OPTIONS:
        print("⚠️⚠️Invalid input! Enter a number from the list.")
        cuisine_choice = input("> ").strip()
    cuisine = CUISINE_OPTIONS[int(cuisine_choice)]
    
    # Taste
    taste = input("Taste (e.g. spicy/sweet): ").strip()
    while not taste:
        print("⚠️⚠️Taste cannot be empty!")
        taste = input("Taste: ").strip()
    
    # Description
    description = input("Description: ").strip()
    while not description:
        print("⚠️⚠️Description cannot be empty!")
        description = input("Description: ").strip()
    
    # Budget
    print("Budget: 1.Low 2.Medium 3.High")
    budget = input("Enter number: ").strip()
    while budget not in ["1", "2", "3"]:
        print("⚠️⚠️Invalid input! Enter 1/2/3.")
        budget = input("> ").strip()
    budget = {"1": "low", "2": "medium", "3": "high"}[budget]
    
    # Calories
    calories = input("Calories: ").strip()
    while not calories.isdigit() or int(calories) <= 0:
        print("⚠️⚠️Invalid input! Enter a positive integer.")
        calories = input("Calories: ").strip()
    
    return {
        "name": name,
        "cuisine": cuisine,
        "taste": taste,
        "description": description,
        "budget": budget,
        "calories": int(calories)
    }