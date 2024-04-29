student_score= {
    "avi": 87,
    "ram": 55,
    "hanuman":71,
    "bajranbali": 100,
}
student_grade={}

for student in student_score:
    score= student_score[student]
    if  score>90:
        student_grade[student]=""
    elif score>80:
        student_grade[student]="Exceeds Expectation"
    elif score>70:
        student_grade[student]="acceptable"
    elif score<70 :
        student_grade[student]="fail"
print(student_grade)