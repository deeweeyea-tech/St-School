def assign_grade(score):
    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80 :
        return 'C'
    elif score >= 60 and score < 70 :
        return 'D'
    elif score<60 and score >= 0:
        return 'F'
    else:
        return 'Invalid Score'

print(assign_grade(95))
print(assign_grade(85))
print(assign_grade(75))
print(assign_grade(65))
print(assign_grade(55))
print(assign_grade(105))