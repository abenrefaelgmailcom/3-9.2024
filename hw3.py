
# כתוב תוכנית פייטון הקולטת 2 מחרוזות ומדפיסה אותם עם כוכבית ביניהם וגם עם מינוס ביניהם.
# לדוגמא אם נקלטו המחרוזות הבאות : "rocks" "python"
# יודפס:
#
# *python*rocks*
# -python-rocks-

# Start

fname: str = input("what is your first-name?")
lname: str = input("what is your last-name?")
print("*" + fname + " " + lname + "*")
print("-" + fname + " " + lname + "-")

# End