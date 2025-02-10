students = (
    ("Ria", 24, 3.85),
    ("Zara", 22, 3.60),
    ("Noah", 26, 3.95),
    ("Mia", 21, 3.75)
)
SortedStudents = sorted(students, key=lambda x: x[2], reverse=True)  
print(SortedStudents)
