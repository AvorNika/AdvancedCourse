# раздел 10.5 Вложенные словари и генераторы словарей, задание 16
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

# result = []
#
# for i in range(len(student_ids)):
#     dict1 = {}
#     dict1[student_names[i]] = student_grades[i]
#     dict2 = {}
#     dict2[student_ids[i]] = dict1
#     result.append(dict2)

#result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_ids))]

result = [{x: {y: z}} for x, y, z in zip(student_ids, student_names, student_grades)]

print(result)
