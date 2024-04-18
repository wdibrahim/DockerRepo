employees = []

def add_employee(name, age, department, position):
    employees.append({"name": name, "age": age, "department": department, "position":position})

def view_employees():
    for employee in employees:
        print(f"Name: {employee['name']}, Age: {employee['age']}, Department: {employee['department']}, Position: {employee['position']}")


def search_employee(name):
    for employee in employees:
        if employee["name"].lower() == name.lower():
            print(f"Name: {employee['name']}, Age: {employee['age']}, Department: {employee['department']}, Position: {employee['position']}")
            return
    print("Employee not found!!")

add_employee("Aayam", 29, "IT", "Developer")
add_employee("Ahmed", 39, "IT", "Developer")

print("All Employees: ")
view_employees()

search_employee("Aayam")