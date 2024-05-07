# To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))  # made it integer
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2
facility = "audio system" if attendees > 100 else "projector"
print(facility)

# Task 3
print("Veggie Delight Caterers") if input("Would you like vegetarian food? (yes/no) ") == "yes" else print("Gourmet Meals Caterers")