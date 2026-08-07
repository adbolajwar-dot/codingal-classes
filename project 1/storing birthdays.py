# Personal Goals Display
 
# Import the keyword module
import keyword
 
# Create variables using valid Python identifier names
person_name = input("Enter your name: ")
goal_name = input("Enter your personal goal: ")
target_month = input("Enter the target month: ")
daily_minutes = 30
 
# Print multiple values together
print("\nName:", person_name)
print("Goal:", goal_name)
print("Target Month:", target_month)
print("Daily Practice:", daily_minutes, "minutes")
 
# Start a new line using \n
print("\nMy Personal Goal Plan\n")
 
# Change how the print statement ends
print("Goal Status:", end=" ")
print("Not Started")
 
print("Progress Reminder:", end=" - ")
print("Practice every day!")
 
# Display the complete goal summary
print(
    "\n",
    person_name,
    "plans to work on",
    goal_name,
    "for",
    daily_minutes,
    "minutes every day."
)
 
# Print Python's reserved words
print("\nPython keywords are...\n")
print(keyword.kwlist)