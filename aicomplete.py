# AI-suggested function with safer key access
def sort_dicts_by_key_safe(data, key):
    return sorted(data, key=lambda x: x.get(key, float('inf')))
# Example with missing key in one dictionary
people = [
    {"name": "Feli", "age": 30},
    {"name": "Siri"},  
    {"name": "Alexa", "age": 35}
]
# Sort by 'age' using the AI-suggested function
sorted_people = sort_dicts_by_key_safe(people, "age")

# Output result
print("Sorted list by age:")
for person in sorted_people:
    print(person)
