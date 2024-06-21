# Lesson 4: Assignments | Regex

# 1. Python Regular Expressions Mastery

import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def validate_names(names):
    pattern = re.compile(r"^[A-Z][a-z]+\s([A-Z][a-z]+|([A-Z]\.\s)?[A-Z][a-z]+)$")
    valid_names = []

    for name in names:
        if re.match(pattern, name):
            valid_names.append(name)
        else:
            print("invalid name.")
    return valid_names

print(validate_names(names))



      


