name = input("Enter student name: ")
if name == "":
    print("Invalid name. Try again.")
    name = input("Enter student name: ")

score1 = input("Enter Activity 1 score: ")
if not score1.isdigit():
    print("Invalid score. Try again.")
    score1 = input("Enter Activity 1 score: ")

score2 = input("Enter Activity 2 score: ")
if not score2.isdigit():
    print("Invalid score. Try again.")
    score2 = input("Enter Activity 2 score: ")

average = (int(score1) + int(score2)) / 2

print("Student:", name)
print("Average:", average)
