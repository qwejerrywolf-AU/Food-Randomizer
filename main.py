import random
from datetime import datetime, timedelta
from data_handler import load_dishes, save_history, load_history
from user_input import get_user_preferences
from history_manager import generate_weekly_report
from data_handler import add_dish
from user_input import get_new_dish_input

def filter_dishes(dishes, preferences):
    # Filter dishes based on user preferences
    filtered = []
    for dish in dishes:
        # Check cuisine preference
        if preferences["cuisines"] and dish["cuisine"] not in preferences["cuisines"]:
            continue
        # Check spicy restriction
        if preferences["reject_spicy"] and dish["taste"] == "spicy":
            continue
        # Check budget level
        if preferences["budget"] and dish["budget"] != preferences["budget"]:
            continue
        # Check calorie limit
        if preferences["max_calories"] and dish["calories"] > preferences["max_calories"]:
            continue
        filtered.append(dish)
    return filtered

def main():
    dishes = load_dishes()
    while True:
        print("\n=== Food Randomizer🍔🍕🍱🍜🥟🌯🍟 ===")
        print("1. Recommend Dish")
        print("2. Generate Weekly Report")
        print("3. Exit")
        print("4. Add New Dish")
        choice = input("Please select an option (1/2/3/4): ")
        
        if choice == "1":
            preferences = get_user_preferences()
            filtered = filter_dishes(dishes, preferences)
            
            if not filtered:
                print("No dishes match your criteria. Please broaden your filters!")
            else:
                while True:
                    dish = random.choice(filtered)
                    print(f"\n=== Today's Recommendation ===")
                    print(f"Dish: {dish['name']}")
                    print(f"Taste: {dish['taste']}")
                    print(f"Description: {dish['description']}")
                    print("================================")
                    accept = input("Accept this recommendation? (y/n): ").lower()
                    
                    if accept == "y":
                        history = load_history()
                        history.append({
                            "timestamp": datetime.now().isoformat(),
                            "name": dish["name"],
                            "cuisine": dish["cuisine"],
                            "taste": dish["taste"],
                            "budget": dish["budget"],
                            "calories": dish["calories"]
                        })
                        save_history(history)
                        print("Record saved!")
                        break
                    else:
                        retry = input("Try another recommendation? (y/n): ").lower()
                        if retry != "y":
                            break
        
        elif choice == "2":
            generate_weekly_report()
        
        elif choice == "3":
            print("Goodbye!")
            break

        elif choice == "4":
            new_dish = get_new_dish_input()
            add_dish(new_dish)
            print("✅ Dish added successfully!")
        
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()