from utils import make_student


def add_student(students, name, score):
    students.append(make_student(name, score))


def average_score(students):
    if not students:
        return 0

    total = 0
    for student in students:
        total += student["score"]

    return total / len(students)


def top_student(students):
    if not students:
        return None

    best = students[0]

    for student in students:
        if student["score"] > best["score"]:
            best = student

    return best


def print_report(students):
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
    print("\n1 Add student, 2 Report, 3 Quit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(students, name, score)

    elif choice == "2":
        print_report(students)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
