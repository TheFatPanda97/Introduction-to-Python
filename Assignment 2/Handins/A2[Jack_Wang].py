def calc_avg(marks, weight) -> float:


    """ () ->
    Returns ... COMPLETE THIS

    >>> calc_avg(50, 50)
    100.0
    >>> calc_avg(33, 44)
    75.0
    >>> calc_avg(18, 25)
    72.0
    """

    # COMPLETE THE FUNCTION BODY

    return marks / weight * 100.0

def calc_needed(mark, desired, final_weight):
    """ () ->
    Returns the mark needed on the final exam to attain
    the desired mark desired with the current ark
    mark, and the weight of the final exam final_weight

    Here is the formula used.

    The original formula is wrong
    Required = (Goal - Current * (100 - Final Weight)) / Final Weight

    here is the correct formula:
    Required = (Goal * 100 - Current * (100 - Final Weight)) / Final Weight

    >>>calc_needed(75, 50, 75)
    25 - correct answer is 41.666666667

    CREATE TWO MORE TEST CASES
    >>> calc_needed(60, 80, 60)
    93.333333

    >>> calc_needed(80, 90, 50)
    100.0
    """
    return (desired * 100.0 - mark * (100.0 - final_weight)) / final_weight

def get_input(message):
    """ (str) -> int/string
    Returns the input from the user.
    This function should output a message.

    No test cases necessary.
    """
    print(message)
    return input()

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
print(average)
print(total_weight)
print("-----------------------------")
# Ask them what grade they want on the final exam, and calculate it then print.
desired = int(get_input("What is your desired final mark in the course?"))

print(calc_needed(average, desired, 100 - total_weight))