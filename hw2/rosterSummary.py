# Initialize an empty dictionary to store student data by major
student_data = {}

# Read the input file and populate the student data dictionary
with open('roster1.dat', 'r') as input_file:
    for line in input_file:
        name, major, gpa, credits = line.strip().split(',')
        gpa = float(gpa)
        credits = int(credits)
        if major not in student_data:
            student_data[major] = []
        student_data[major].append((name, gpa, credits))

# Initialize an empty dictionary to store summary data by major
summary_data = {}

# Calculate the summary data for each major and store it in the summary data dictionary
for major, students in student_data.items():
    count = len(students)
    total_gpa = sum(student[1] for student in students)
    total_credits = sum(student[2] for student in students)
    avg_gpa = total_gpa / count
    avg_credits = total_credits / count
    summary_data[major] = (avg_gpa, avg_credits, count)

# Write the summary data to the output file
with open('roster1.out', 'w') as output_file:
    for major, summary in summary_data.items():
        avg_gpa, avg_credits, count = summary
        output_file.write(f"{major},{avg_gpa},{avg_credits},{count}\n")
