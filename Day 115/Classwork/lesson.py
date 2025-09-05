person = {
    "name": "Luka",
    "hobby": "Footbal",
    "academy": "Mountain Sports School",
    "age": 19,
    "city": "Kutaisi"
}


person_copy = person.copy()
print(person.get("academy"))
print(person.items())
print(person.keys())
print(person.values())

removed_value = person.pop("age")
print(removed_value)

removed_item = person.popitem()
print(removed_item)

person.update({"city": "Rustavi", "hobby": "hiking"})

person.clear()
print(person)
