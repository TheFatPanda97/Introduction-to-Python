""" Dear Shawn,
    I writing this to inform you that I am no longer coming to
    your class.

    I've had a great time learning about coding. I really enjoyed my time in your class; it was a great learning
    environment. where everyone
    only wanted to improve. Of course, you're a great teacher as you only wanted to benefit the knowledge of the future
    generation. Not only that, you pushed our skills to the next level and constantly aided when we needed help.
    Overall, I just want to thank you for providing an amazing opportunity to discover the wonders of
    coding and python. You've really proved to me that python is more than just a language.
    Thanks, Jeff Tony

    









































































































































































































    Bye!












    """


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

    return marks / weight


def calc_needed(mark, desired, final_weight):
    """ (int, int, int) -> float
    Returns the mark needed on the final exam to attain
    the desired mark desired with the current mark
    mark, and the weight of the final exam final_weight

    Here is the formula used.

    Required = (Goal - Current * (100 - Final Weight)) / Final Weight

    >>> calc_needed(75, 50, 75)
    25.0

    CREATE TWO MORE TEST CASES
    """

    return (desired - mark * (100 - final_weight)) / final_weight


def get_input(message):
    """ (str) -> int/string
    Returns the input from the user.
    This function should output a message.

    No test cases necessary.
    """
    message = input(message)
    print(message, '?', " that\'s so trash!")
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
# Ask them what grade they want on the final exam, check if it's possible, calculate it and then print it.
desired = int(get_input("What is your desired final mark in the course?"))
if calc_needed(average, desired, 100 - total_weight) * 100 > 100:
    print("Error")
else:
    print(calc_needed(average, desired, 100 - total_weight) * 100)

"""
Psych 
"""
