from nicegui import ui
from gui import EmployeeAppUI
import database

# Start Database
database.init_db()

def add_employee_to_db(name, address, dept, pos, salary):
    return database.add_employee(name, address, dept, pos, salary)

def get_employees_from_db():
    return database.get_all_employees()

def delete_employee_from_db(emp_id):
    return database.delete_employee(emp_id)

def search_employees_in_db(query_str):
    return database.search_employees(query_str)

def get_application_stats():
    return database.get_db_stats()

# ADVANCED: Güncelleme Köprüsü
def update_employee_in_db(emp_id, name, address, dept, pos, salary):
    return database.update_employee(emp_id, name, address, dept, pos, salary)


@ui.page('/')
def main_page():
    EmployeeAppUI(
        add_callback=add_employee_to_db,
        get_callback=get_employees_from_db,
        delete_callback=delete_employee_from_db,
        search_callback=search_employees_in_db,
        stats_callback=get_application_stats,
        update_callback=update_employee_in_db  # Yeni eklenen callback!
    )

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Employee Management System')