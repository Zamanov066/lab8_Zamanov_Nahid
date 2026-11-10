def average(*numbers):
    """Return the average of the numbers, or 0 if none are given."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def make_course(code, **details):
    """Return a dictionary with the course code and extra details."""
    course = {"code": code}
    for key, value in details.items():
        course[key] = value
    return course


print(average(70, 80, 90))   # 80.0
print(average(100))          # 100.0
print(average())             # 0
print(make_course("CE101", title="Fundamentals of Programming", credits=6))
