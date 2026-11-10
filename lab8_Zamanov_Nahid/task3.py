def build_username(first, last, year=""):
    """Return a username like first.last, with year added if given."""
    username = first.lower() + "." + last.lower()
    if year:
        username += str(year)
    return username


print(build_username("Aysel", "Mammadova"))       # aysel.mammadova
print(build_username("Kamran", "Aliyev", 2005))   # kamran.aliyev2005
