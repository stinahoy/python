student = {
    "first name" : "Ola",
    "last name" : "Nordmann",
    "favourite course" : "Programmering 1"
}

fult_navn = f"{student['first name']} {student['last name']}"
print("Fult navn:", fult_navn)

student["favourite course"] = "ITF10219 Programering 1"

student["age"] = 20

print("Oppdatert student info:", student)
