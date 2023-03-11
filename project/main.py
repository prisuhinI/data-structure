employees = {}


def add_employee(employee_id, employee_name, employee_department, employee_salary):
    employees[employee_id] = {'name': name, 'department': department, 'salary': salary}


def remove_employee(employee_id):
    if employee_id in employees:
        del employees[employee_id]


def update_employee(employee_id, name=None, department=None, salary=None):
    if employee_id in employees:
        if name:
            employees[employee_id]['name'] = name
        if department:
            employees[employee_id]['department'] = department
        if salary:
            employees[employee_id]['salary'] = salary


def search_employee(employee_id):
    if employee_id in employees:
        return employees[employee_id]
    else:
        return None


def print_all_employees():
    for employee_id in employees:
        print(f"{employee_id}: {employees[id]['name']} "
              f"({employees[employee_id]['department']}) - ${employees[employee_id]['salary']}")


def menu():
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Search Employee")
    print("5. Print All Employees")
    print("6. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        employee_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        department = input("Enter employee department: ")
        salary = input("Enter employee salary: ")
        add_employee(employee_id, name, department, salary)
    elif choice == '2':
        employee_id = input("Enter employee ID to remove: ")
        remove_employee(employee_id)
    elif choice == '3':
        employee_id = input("Enter employee ID to update: ")
        name = input("Enter new employee name (leave blank to keep current value): ")
        department = input("Enter new employee department (leave blank to keep current value): ")
        salary = input("Enter new employee salary (leave blank to keep current value): ")
        update_employee(employee_id, name, department, salary)
    elif choice == '4':
        employee_id = input("Enter employee ID to search: ")
        result = search_employee(id)
        if result:
            print(f"{result['name']} ({result['department']}) - ${result['salary']}")
        else:
            print("Employee not found.")
    elif choice == '5':
        print_all_employees()
    elif choice == '6':
        break
    else:
        print("Invalid choice.")
    