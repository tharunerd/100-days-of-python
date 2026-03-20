student_heights = input("Input a list of student heights: ").split()
student_heights = [float(height) for height in student_heights]

total_height = sum(student_heights)
number_of_students = len(student_heights)

average_height = round(total_height / number_of_students)
print(f"Average height = {average_height}")
