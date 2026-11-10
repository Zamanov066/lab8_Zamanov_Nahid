def print_student_card(name, group, year):
    """Print a student card with name, group and year."""
    print("Name: " + name)
    print("Group: " + group)
    print("Year: " + str(year))


# Positional arguments
print_student_card("Aysel Mammadova", "CE-101", 1)

# Keyword arguments (order changed)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")

# Deliberate error (commented out):
# print_student_card("Aysel", "CE-101")
# TypeError: print_student_card() missing 1 required positional argument: 'year'
