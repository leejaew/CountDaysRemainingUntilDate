import datetime

# Get the current date
current_date = datetime.datetime.now()

# Get the user's input date
print("Enter a date in the format YYYY-MM-DD:")
user_input = input()

# Parse the user's input date
user_date = datetime.datetime.strptime(user_input, "%Y-%m-%d")

# Calculate the difference between the two dates
date_difference = user_date - current_date

# Print the number of days remaining
print(f"There are {date_difference.days} days remaining until {user_input}.")