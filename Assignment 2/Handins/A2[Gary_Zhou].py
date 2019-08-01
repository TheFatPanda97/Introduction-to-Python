# Introduction to Python
# Due Jul 19, 11:59 PM
# Assignment 2: Mark Calculator
# 100 points
#
# Shawn Hu
# Jul 8 (Edited Jul 10)
# Start by downloading the starter code and reading the assignment criteria.
# Note: when handing in your work, name your file as A2[firstname_lastname].py
#
# A2.docx
# Word
#
# A2_Skeleton.py
# Text
# Your work
# Assigned
# Files you add or create can be viewed and edited by your teacher
# Mark as done or attach work to turn in
# Private comments
# Class comments
#
# Assignment 2: Mark Calculator
def calc_avg(marks, weight):
    """ (int, int) -> float
    Returns ... COMPLETE THIS

    >>> calc_avg(50, 50)
    1.0
    >>> calc_avg(33, 44)
    0.75
    >>> calc_avg(18, 25)
    0.72
    """
    return float(marks / weight)


def calc_needed(mark, desired, final_weight):
    """ (int, int, int) -> float
    Returns the mark needed on the final exam to attain
    the desired mark desired with the current mark
    mark, and the weight of the final exam final_weight

    Here is the formula used.

    Required = (Goal - Current * (100 - Final Weight)) / Final Weight

    >>> calc_needed(75, 50, 75)
    25.0

    >>> calc_needed(100,100,100)
    ERROR cannot divide by zero
    >>> calc_needed(25,50,20)



    CREATE TWO MORE TEST CASES
    """
    desired = 50
    mark = 25
    final_weight = 20
    Required = 100 * (desired - mark * (100 - final_weight)) / final_weight
    if Required > 100 or Required < 0:
        return " It's Impossible"
    else:
        return Required


def get_input(message):
    """ (str) -> int/string
    Returns the input from the user.
    This function should output a message.

    No test cases necessary.
    """
    message = int(input(message))
    print(message)
    return message


counter = int(get_input("How many marks?"))  # What should be passed in?
i = 0
# Define a variable here for the total marks
total_marks = 0
# Define a variable here for the total weight
total_weight = 0

while i < counter:  # DO NOT MODIFY

    # Get the mark and add it to total marks
    partial_mark = int(get_input("Enter your mark"))
    # Get the weight and add it to total weight
    partial_weight = int(get_input("Enter the weight"))
    total_marks += (partial_mark / 100) * partial_weight
    total_weight += partial_weight
    i += 1  # DO NOT REMOVE

# Calculate and print the average
average = calc_avg(total_marks, total_weight)
print(average * 100)
print("-----------------------------")
# Ask them what grade they want on the final exam, and calculate it then print.
desired = int(get_input("What is your desired final mark in the course?"))

print(calc_needed(average, desired, 100 - total_weight))
