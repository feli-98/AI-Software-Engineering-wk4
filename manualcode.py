# Manual function to sort a list of dictionaries by a specific key
def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

# Example with missing key in one dictionary
people = [
    {"name": "Feli", "age": 30},
    {"name": "Siri"},  
    {"name": "Alexa", "age": 35}
]

# Sort by 'age'
sorted_people = sort_dicts_by_key(people, "age")

# Output result
print("Sorted list by age:")
for person in sorted_people:
    print(person)



