import datetime

# Get the current date
current_date = datetime.datetime.now()

# Get the user's input date
print("Enter a date in the format YYYYMMDD:")
user_input = input()

# Add dashes to the user's input date
formatted_date = user_input[:4] + "-" + user_input[4:6] + "-" + user_input[6:]

# Parse the user's input date
user_date = datetime.datetime.strptime(formatted_date, "%Y-%m-%d")

# Calculate the difference between the two dates
date_difference = user_date - current_date

# Print the number of days remaining
print(f"There are {date_difference.days} days remaining until {formatted_date}.")