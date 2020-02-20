def compute_grade(grade: object):
    try:
        grade = float(grade)
        if grade > 1.0:
            print("Bad Score")
        elif grade >= float(0.9):
            print("A")
        elif grade >= float(0.8):
            print("B")
        elif grade >= float(0.7):
            print("C")
        elif grade >= float(0.6):
            print("D")
        elif grade < float(0.6):
            print("F")
        else:
            print("Bad Score")
    except:
        print("bad score")


compute_grade(input("Enter grade from 0.0 to 1.0: "))

