def get_student_marks():
    MAX_STUDENTS = 30
    MAX_MARKS = 50

    try:
        num_students = int(input("Enter the number of students (max 30): "))
        if num_students > MAX_STUDENTS:
            raise ValueError(f"Error: Number of students cannot exceed {MAX_STUDENTS}.")

        marks_input = input(f"Enter marks for {num_students} students (out of {MAX_MARKS}), separated by spaces: ")
        marks = list(map(float, marks_input.split()))

        if len(marks) != num_students:
            raise ValueError(f"Error: You must enter exactly {num_students} marks.")
        if any(mark < 0 or mark > MAX_MARKS for mark in marks):
            raise ValueError(f"Error: Marks must be between 0 and {MAX_MARKS}.")

        unique_marks = sorted(set(marks), reverse=True)
        if len(unique_marks) < 3:
            print("Not enough unique marks to determine the second and third highest.")
        else:
            difference = unique_marks[1] - unique_marks[2]
            print(f"\nSecond highest marks: {unique_marks[1]}")
            print(f"Third highest marks: {unique_marks[2]}")
            print(f"Difference between second and third highest marks: {difference}")

    except ValueError as e:
        print(e)

get_student_marks()