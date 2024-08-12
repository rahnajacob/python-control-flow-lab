# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input('Enter a letter: ').lower()
    if len(letter) > 1:
        print("Please enter a single letter.")
        return
    if (letter.isalpha() != True):
        print("Please enter a string.")
        return
    else:
        if letter in "aeiou":
            print(f"The letter {letter} is a vowel")
            return
        else:
            print(f"The letter {letter} is a consonant")
            return

# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    age = input("Please enter your age: ")
    if age.isdigit() == False:
        print("Please enter a number.")
        return
    if int(age) < 1:
        print("You're very smart for a newborn!")
    elif int(age) < 18:
        print("Not old enough yet!")
    elif int(age) >= 18:
        print("Vote away!")
        return

# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    input_age = input("Please enter the dog's age: ")
    if input_age.isdigit() == False:
        print("Please enter a number.")
        return
    if int(input_age) <= 2:
        age = int(input_age) * 10
        print(f"The dog's age in dog years is {age}.")
    elif int(input_age) > 2:
        age = ((int(input_age) - 2) * 7) + 20
        print(f"The dog's age in dog years is {age}.")
        return 

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    user_is_cold = input("Is it cold? (Y/N): ").lower()
    user_is_raining = input("Is it raining? (Y/N): ").lower()
    if (user_is_cold not in "yn") or (user_is_raining not in "yn"):
        print("Please provide the correct input!")
        return
    is_cold = True if user_is_cold == "y" else False
    is_raining = True if user_is_raining =="y" else False

    if (is_cold and is_raining):
        print("Wear a waterproof coat.")
    elif (is_cold and (not is_raining)):
        print("Wear a warm coat.")
    elif ((not is_cold) and is_raining):
        print("Carry an umbrella.")
    elif ((not is_cold) and (not is_raining)):
        print("Wear light clothing.")
        return


# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    user_month = input("Please enter the month (eg: Jan, Jun, Nov): ")
    if len(user_month) > 3:
        print("Please enter the month in the MMM format.")
        return
    elif (user_month.isalpha() != True):
        print("Please enter the month in string format.")
        return
    elif (user_month not in months):
        print("Please enter the name of the month correctly.")
        return
    str_user_date = input("Please enter the date (eg: 01, 17, 24): ")
    if len(str_user_date) > 2:
        print("Please enter the date in DD format.")
        return
    elif (str_user_date.isdigit() != True):
        print("Please enter the date as a number.")
        return
    elif (int(str_user_date) > 31) and (user_month):
        print("No month has that many days!")
        return
    
    user_date = int(str_user_date)

    if user_month == "Jan" or user_month == "Feb":
        print(f"{user_month} {user_date} is in Winter.")
    elif (user_month == "Mar" and user_date <= 19) or (user_month == "Dec" and user_date > 20):
        print(f"{user_month} {user_date} is in Winter.")
    elif user_month == "Apr" or user_month == "May":
        print(f"{user_month} {user_date} is in Spring.")
    elif (user_month == "Mar" and user_date > 19) or (user_month == "Jun" and user_date <= 20):
        print(f"{user_month} {user_date} is in Spring.")
    elif user_month == "Jul" or user_month == "Aug":
        print(f"{user_month} {user_date} is in Summer.")
    elif (user_month == "Sep" and user_date < 20) or (user_month == "Jun" and user_date > 20):    
        print(f"{user_month} {user_date} is in Summer.")
    elif (user_month == "Oct" or user_month == "Nov"):
        print(f"{user_month} {user_date} is in Fall.")
    elif (user_month == "Sep" and user_date >= 22) or (user_month == "Dec" and user_date <= 20):
        print(f"{user_month} {user_date} is in Fall.")
        return
    
# Call the function
determine_season()


# Level Up


# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

import random

def guess_number():
    target_num = random.randint(0, 20)
    max_guesses = 5
    for i in range(1, max_guesses + 1):
        user_guess = int(input("Input a number between 0 & 20: "))
        if user_guess == target_num:
            print("Congrats, you guessed the number!")
            break
        elif user_guess > target_num:
            print("Guess is too high!")
        elif user_guess < target_num:
            print("Guess is too low!")
        if i == 4:
            print("Last chance!")
        elif i == 5:
            print("Sorry, you failed to guess the number in five attempts.")
            break

# Call the function
guess_number()




