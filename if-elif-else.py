# if-elif-else conditions:

print("Celebal Technologies Internship Drive for BTech 2026 Batch. Only for CS/IT students with cgpa 8 and above. Required skills are Python/SQL!!!\n")

name = input("Enter your name: ")
branch = input("Enter your branch: ")
cgpa = float(input("Enter your cgpa: "))
skills = input("Enter your skill: ")

if cgpa < 8.0:
    print("Not eligible for the internship")
elif branch not in['CS','IT']:
    print("Not eligible for the internship")
elif skills not in['Python','SQL']:
    print("Not eligible for the internship")
else:
    print(f"Congratulations {name}, you are eligible for the internship!")
