import csv
from faker import Faker

fake = Faker("uk_UA")


def generate_employee(gender):
    if gender == "male":
        first_name = fake.first_name_male()
        middle_name = fake.middle_name_male()
    else:
        first_name = fake.first_name_female()
        middle_name = fake.middle_name_female()

    return {
        "Прізвище": fake.last_name(),
        "Ім’я": first_name,
        "По батькові": middle_name,
        "Стать": "Чоловіча" if gender == "male" else "Жіноча",
        "Дата народження": fake.date_of_birth(minimum_age=16, maximum_age=85).strftime("%d-%m-%Y"),
        "Посада": fake.job(),
        "Місто проживання": fake.city(),
        "Адреса проживання": fake.address(),
        "Телефон": fake.phone_number(),
        "Email": fake.email()
    }


employees = []

for _ in range(1200):
    employees.append(generate_employee("male"))
for _ in range(800):
    employees.append(generate_employee("female"))

with open("employees.csv", mode="w") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(employees)

print("Ok")
