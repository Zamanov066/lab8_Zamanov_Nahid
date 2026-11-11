def print_student_card(name, group, year):
    """Print a student card with name, group and year."""
    print("Name: " + name)
    print("Group: " + group)
    print("Year: " + str(year))


# Positional arguments
print_student_card(name=input("Enter name:"),group=input("Enter your group:"),year=input("Enter year:"))

