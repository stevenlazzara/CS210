import numpy as np

# Read data from file and convert to numpy array
data = np.loadtxt('roster2.dat', delimiter=',', dtype={
    'names': ('name', 'age', 'major', 'gpa'),
    'formats': ('U50', 'i4', 'U4', 'f8')
})

# Compute and print average GPA of all students
avg_gpa = data['gpa'].mean()
print(avg_gpa)

# Compute and print maximum GPA of students majoring in CS
max_cs_gpa = data[data['major'] == 'CS']['gpa'].max()
print(max_cs_gpa)

# Compute and print number of students with a GPA over 3.5
num_high_gpa = np.sum(data['gpa'] > 3.5)
print(num_high_gpa)

# Compute and print average GPA of students who are at least 25 years old
avg_old_gpa = data[data['age'] >= 25]['gpa'].mean()
print(avg_old_gpa)

# Compute and print major with highest average GPA among students at most 22 years old
young_data = data[data['age'] <= 22]
max_avg_gpa = 0
best_major = ''
for major in np.unique(young_data['major']):
    avg_gpa = young_data[young_data['major'] == major]['gpa'].mean()
    if avg_gpa > max_avg_gpa:
        max_avg_gpa = avg_gpa
        best_major = major
print(best_major)
