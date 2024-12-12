def group_students_by_age(students):
    grouped = {}
    for student in students:
        age = student["age"]
        name = student["name"]
        if age not in grouped:
            grouped[age] = []
        grouped[age].append(name)
    return grouped

students_list = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 22},
    {"name": "Eve", "age": 21},
]

result = group_students_by_age(students_list)
print(result)
