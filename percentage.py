def find_percentage():
    n = int(input("Enter the number of students: "))
    student_marks = {}  

    for i in range(n):
        data = input("Please enter the student's name followed by their 3 marks separated by spaces: ").split()
        name = data[0]  
        marks = list(map(float, data[1:]))  
        student_marks[name] = marks  
    
    query_name = input("Which student's average do you want to find? ")
    
    if query_name in student_marks:  
        avg = sum(student_marks[query_name]) / len(student_marks[query_name])  
        print(f"{query_name}'s average marks are: {avg:.2f}")  
        print("Sorry, that student is not in the list.")  


find_percentage()
