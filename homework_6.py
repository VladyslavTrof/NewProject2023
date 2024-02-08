
people = [{"name": "Bobby", "age": 15}, {"name": "Chloe", "age": 18}, {"name": "James", "age": 45}, {"name": "Anna", "age": 15}, {"name": "Tom", "age": 22}]

min_age = min(people, key=lambda person: person["age"])["age"]

youngest_names = []
for person in people:
  if person["age"] == min_age:
    youngest_names.append(person["name"])

max_length = len(max(people, key=lambda person: len(person["name"]))["name"])

longest_names = []
for person in people:
  if len(person["name"]) == max_length:
    longest_names.append(person["name"])

total_age = sum(person["age"] for person in people)
average_age = total_age / len(people)

print(f"Youngest people in this list: {youngest_names}")
print(f"Longest names in this list: {longest_names}")
print(f"Average age of everyone in this list : {average_age}")
