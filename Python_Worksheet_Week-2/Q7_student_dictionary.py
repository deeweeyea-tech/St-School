students = {
    "Divya": {"marks": 89, "grade": "B"},
    "Rayyan": {"marks": 94, "grade": "A"},
    "Rita": {"marks": 67, "grade": "C"},
    "Tenam": {"marks": 78, "grade": "B"},
    "Amulya": {"marks": 55, "grade": "D"},
}

print("Student Details")
for name in students:
    print("Name:", name)
    print("Marks:", students[name]["marks"])
    print("Grade:", students[name]["grade"])
    print()

# Finding highest marks
highest_name = ""
highest_marks = 0

for name in students:
    if students[name]["marks"] > highest_marks:
        highest_marks = students[name]["marks"]
        highest_name = name

print("Student with highest marks:", highest_name)
print("Marks:", highest_marks)