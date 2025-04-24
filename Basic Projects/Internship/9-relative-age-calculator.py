def relative_age_calculator():
# Get the user input age as a number
    age = input("Enter animal age (in years): ")
    while age.isnumeric() == False or age < 1 or age > 100:
        age = input("Invalid Input. Enter animal age: ")
# Get the user input type as a string
    type = input("Enter 'd' for dog, 'c' for cat or 'e' for elephant.\nEnter the type of animal: ")
    while type not in ["d", "c", "e", "dog", "cat", "elephant"]:
        type = input("Invalid Input. Enter animal type: ")
# Calculate the equivalent age    
    if type in ["d", "dog"]:
        print(f"Equivalent human age: {7*int(age)}")
    elif type in ["c", "cat"]:
        print(f"Equivalent human age: {6*int(age)}")
    elif type in ["e", "elephant"]:
        print(f"Equivalent human age: {3*int(age)}")    
relative_age_calculator()
