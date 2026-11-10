def make_student(name, score, group=""):
    """Return a dictionary describing a student."""
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student


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
