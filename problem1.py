# Manny Pagan
# Sept 24th Python Course
# Assignment 2
# Due: Oct 3rd


# Problem 1: Most Clocks Are Normal, But Some Are Cuckoo!
# ### Skill you're practicing: Writing conditionals.
# For this problem, put your solution into a file called `problem1.py`.
# You're making a program for your coworkers that displays a message on their desktop's idle screen. Depending on the time of day, you want to print a different quote. You'll create a variable, `time`, which has an integer value between zero and 23, representing the hour of the day in [military time](https://www.thebalancecareers.com/military-time-3356971), which is a 24-hour clock. Write a conditional statement with Python code that prints exactly one message using the following rules:
# If the time of day is before 9 a.m. --> print the quote "Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day."
# Otherwise if the time of day is before or exactly 4 p.m. --> print the quote "Working hard or hardly working?"
# Otherwise, if the time of day is before 8 p.m. --> print the quote "How did it get so late so soon?"
# Otherwise if the time of day is before 10 p.m. --> print the quote "A day without sunshine is like, you know, night."
# Otherwise, for any time 10 p.m. or later --> print the quote "Burning the midnight oil!"

def time_message():
    if hour < 9:
        print("Morning is wonderful! It's only drawback is that it comes at such an inconvenient time of day!")
    elif hour < 16:
        print("Working hard or hardly working!")
    elif hour < 20:
        print("How did it get so late so soon?")
    elif hour < 22:
        print("A day without sunshine is like, you know, night")
    else:
        print("Burning the midnight oil!")

hour = 2
time_message()

hour = 6
time_message()

hour = 9
time_message()

hour = 22
time_message()

hour = 23
time_message()

