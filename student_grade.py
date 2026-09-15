while True: 
    name = input("What is your name?")
    grade = input("What is your grade?")
    grade = int (grade)

    # while grade < 0 or grade > 100:
    #     print ("Invalid grade. Please try again.")
    #     grade = input("What is your grade?")
    #     grade = int (grade)
    
    while True:
        grade = int(input("What is your grade?"))

        if 0 <= grade <= 100:
            break

        print("Invalid grade.")

    # if grade < 60:
    #     print ("Your level is F")
    # elif grade < 70:
    #     print ("Your level is D")
    # elif grade < 80:
    #     print ("Your level is C ")
    # elif grade < 90:
    #     print ("Your level is B")
    # else:
    #     print ("Your level is A")


    if grade < 60:
        level = "F"
    elif grade < 70:
        level = "D"
    elif grade < 80:        
        level = "C"
    elif grade < 90:
        level = "B"
    else:   
        level = "A"

    # print ("Hello", name, "your grade is",grade)
    # print ("Your level is", level)
    print(f"Hello {name}, your grade is {grade}.")
    print(f"Your level is {level}.")

    choice = input ("Continue? (yes/no):")

    if choice =="no":
        break