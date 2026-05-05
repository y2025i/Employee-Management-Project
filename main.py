from nicegui import ui
from gui import EmployeeAppUI          # Zeljko'nun UI sınıfı
import database                        # Yücel'in veritabanı katmanı


# --- Veritabanını başlat ---
database.init_db()


def add_employee_to_db(emp_id, name, dept, pos, salary):
    """UI'dan gelen veriyi database.py'ye iletir."""
    success = database.add_employee(emp_id, name, dept, pos, salary)
    if not success:
        ui.notify(f'ID {emp_id} already exists in database!', color='red')
    return success



def get_employees_from_db():
    """Tablo için tüm çalışanları çeker."""
    return database.get_all_employees()

def delete_employee_from_db(emp_id):
    """Delete employee via database layer."""
    success = database.delete_employee(emp_id)
    if not success:
        ui.notify(f'No employee found with ID {emp_id}', color='red')
    return success
# --- UI'yi başlat ---
app = EmployeeAppUI(
    add_callback=add_employee_to_db,
    get_callback=get_employees_from_db,
    delete_callback=delete_employee_from_db,
)


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Employee Management System')



