# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ageInInt = int(age)
yearsRemaining = 90 - ageInInt
daysRemaining = yearsRemaining*365
weeksRemaining = yearsRemaining*52
monthsRemaining = yearsRemaining*12

message = f"You have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left"
print(message)


