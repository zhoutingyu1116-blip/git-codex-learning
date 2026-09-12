age = input ("How old are you?")
age = int (age)
score = input ("What is your score?")
score = int (score)
has_permission = False

if not has_permission:
    print ("You do not have permission.")
elif age < 10 or age >70:
    print ("You are not allowed.")
elif age < 18:
    print ("You are too young.")
elif score < 60:
    print ("Your score is too low.")
else:
    print ("You are eligible.")

print ("Student check completed.")