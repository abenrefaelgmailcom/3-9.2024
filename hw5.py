
# קלוט 2 מספרים שלמים ) int :b int :a )והדפס את הגדול מבין שניהם
# בדוק בתנאי אם b > a אם כן: הדפס את a אחרת: הדפס את b
# כתוב תרשים זרימה + תוכנית בפייטון

# Start

a: float = float(input("enter a number:"))
b: float = float(input("enter a number:"))

if a > b:
    print(b)
    print(a)

elif b > a:
    print(a)
    print(b)

else:
    print(a)
    print(b)

# End
