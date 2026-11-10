"""Helper functions for Lab 8."""


def add_vat(price, vat_percent=18):
    """Return the price with VAT added."""
    return price + price * vat_percent / 100


def build_username(first, last, year=""):
    """Return a username like first.last, with year added if given."""
    username = first.lower() + "." + last.lower()
    if year:
        username += str(year)
    return username


def make_student(name, score, group=""):
    """Return a dictionary describing a student."""
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student


def add_bonus(scores, bonus):
    """Add bonus to every score in place (max 100). Returns nothing."""
    for i in range(len(scores)):
        scores[i] = min(scores[i] + bonus, 100)


def with_bonus(scores, bonus):
    """Return a new list with bonus added (max 100); original is unchanged."""
    new_scores = []
    for score in scores:
        new_scores.append(min(score + bonus, 100))
    return new_scores


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
