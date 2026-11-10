from utils import make_student


def add_student(students, name, score):
    """Add a student dictionary to the students list."""
    students.append(make_student(name, score))


def average_score(students):
    """Return the average score, or 0 if the list is empty."""
    if not students:
        return 0
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)


def top_student(students):
    """Return the student with the highest score, or None if empty."""
    if not students:
        return None
    best = students[0]
    for student in students:
        if student["score"] > best["score"]:
            best = student
    return best


def print_report(students):
    """Print every student, the average score and the top student."""
    for student in students:
        print(student["name"] + ": " + str(student["score"]))
    print("Average: " + str(average_score(students)))
    best = top_student(students)
    if best is not None:
        print("Top student: " + best["name"] + " (" + str(best["score"]) + ")")
    else:
        print("Top student: none")


students = []
while True:
    print("1 Add student, 2 Report, 3 Quit")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(students, name, score)
    elif choice == "2":
        print_report(students)
    elif choice == "3":
        break
    else:
        print("Invalid choice, try again.")
