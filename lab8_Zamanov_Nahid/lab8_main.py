import utils
from utils import average
from utils import build_username as make_user
import utils as u
from utils import make_student


def print_student_card(name, group, year):
    """Print a student card with name, group and year."""
    print("Name: " + name)
    print("Group: " + group)
    print("Year: " + str(year))


# ---------- Task 1 ----------
print("--- Task 1 ---")
print_student_card("Aysel Mammadova", "CE-101", 1)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")
# print_student_card("Aysel", "CE-101")  # TypeError: missing 1 required positional argument: 'year'

# ---------- Task 2 ----------
print("--- Task 2 ---")
print(utils.add_vat(100))
print(utils.add_vat(50, 10))
print(utils.add_vat(vat_percent=5, price=80))

# ---------- Task 3 ----------
print("--- Task 3 ---")
print(utils.build_username("Aysel", "Mammadova"))
print(utils.build_username("Kamran", "Aliyev", 2005))

# ---------- Task 4 ----------
print("--- Task 4 ---")
print(make_student("Kamran", 61, "CE-101"))
students = []
while True:
    name = input("Name (quit to stop): ")
    if name == "quit":
        break
    score = int(input("Score: "))
    students.append(make_student(name, score))
for student in students:
    print(student["name"] + ": " + str(student["score"]))

# ---------- Task 5 ----------
print("--- Task 5 ---")
scores = [70, 95, 88, 100]
print(utils.with_bonus(scores, 10))
print(scores)
utils.add_bonus(scores[:], 10)
print(scores)
utils.add_bonus(scores, 10)
print(scores)

# ---------- Task 6 ----------
print("--- Task 6 ---")
print(average(70, 80, 90))
print(average(100))
print(average())
print(utils.make_course("CE101", title="Fundamentals of Programming", credits=6))

# ---------- Task 7 ----------
print("--- Task 7 ---")
print(utils.add_vat(200))
print(average(60, 70))
print(make_user("Nigar", "Hasanova"))
print(u.with_bonus([50, 95], 10))
