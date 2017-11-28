import time


"""
Character input by Jeroen on 28-11-2017
"""

# Ask the user for their name
name = input("What's your name? ")

# Ask the user how old he/she is
age = int(input("How old are you? "))

# Get the current year
current_date = time.strftime("%Y")

# Calculate how much years before the users becomes 100 years old
years_left =  100 - age

# Calculate which year the user gets 100
when_onehunderd = int(current_date) + years_left

# Print when the user will be 100
print("Hello {}, You will turn 100 in {}".format(name, when_onehunderd))