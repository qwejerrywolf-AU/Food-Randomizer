from datetime import datetime, timedelta
from data_handler import load_history

def generate_weekly_report():
    # Generate weekly consumption statistics report
    history = load_history()
    spicy_count = 0
    total_calories = 0
    cuisine_count = {}
    
    # Calculate time range for the past week
    one_week_ago = datetime.now() - timedelta(days=7)
    
    for record in history:
        record_time = datetime.fromisoformat(record["timestamp"])
        if record_time >= one_week_ago:
            # Count spicy dishes
            if record["taste"] == "spicy":
                spicy_count += 1
            # Accumulate calories
            total_calories += record["calories"]
            # Count cuisine types
            cuisine = record["cuisine"]
            cuisine_count[cuisine] = cuisine_count.get(cuisine, 0) + 1
    
    # Print formatted report
    print("\n=== Weekly Diet Report ===")
    print(f"Spicy dishes count: {spicy_count}")
    print(f"Total calories intake: {total_calories}")
    print("Cuisine distribution:")
    for cuisine, count in cuisine_count.items():
        print(f"  - {cuisine}: {count} times")