scoreStr = "Enter a grade between 0 and 100. "
inputErrorStr = "Invalid input."
rangeErrorStr = "Grades must be between 0 and 100."

score = input(scoreStr) # prompt user for the grade

try:
    score = int(score) # convert the grade to an integer for comparison
    if score > 100 or score < 0: # score out of bounds
        print(rangeErrorStr)
    elif score >= 93: 
        print("Grade: A")
    elif score >= 85:
        print("Grade: B")
    elif score >= 74:
        print("Grade: C")
    elif score >= 63:
        print("Grade: D")
    else: 
        print("Grade: F")
except:
    print(inputErrorStr)
