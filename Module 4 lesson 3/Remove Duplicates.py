# Dictionary of students (id -> name)
student_data = {
    "id1": {"name": "Sara", "class": "V", "subject_intergration":"english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_intergration":"english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject_intergration":"english, math, science"},
    "id4": {"name": "Surya", "class": "VI", "subject_intergration":"english, math, science"},
}

result = {}
seen_keys = [] # using a list instead of a set

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_intergration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)