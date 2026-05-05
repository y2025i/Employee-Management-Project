from nicegui import ui


class EmployeeAppUI:
    def __init__(self, add_callback, get_callback, delete_callback) -> None:
        """UI layer. It does NOT talk to the database directly.
        add_callback: function to add an employee (defined in main.py)
        get_callback: function to load all employees (defined in main.py)
        delete_callback: function to delete an employee by ID (defined in main.py)
        """
        self.add_callback = add_callback
        self.get_callback = get_callback
        self.delete_callback = delete_callback
        self.build_ui()

    def build_ui(self) -> None:
        ui.query('body').style('margin: 0; padding: 50px; background-color: #222831; ' \
        'background-image: radial-gradient(rgba(255, 255, 255, 0.171) 2px, transparent 0); ' \
        'background-size: 30px 30px; background-position: -5px -5px;')

        with ui.column().classes('w-full h-screen gap-0 '):
            # Header
            ui.label('Employee Management System') \
                .classes('w-full text-center text-black text-4xl font-bold p-5') \
                .style('background-color: #ECD5BC; ')

            with ui.row().classes('w-full flex-1 items-stretch').style('padding: 20px 0; gap: 20px;'):

                # ---------- LEFT SIDE: FORM ----------
                with ui.card().classes('shadow-2 w-[350px]').style('background-color: #ECD5BC; min-height: 550px;'):
                    ui.label('Employee Details') \
                        .classes('text-black text-2xl font-bold mb-4')

                    self.employee_id = ui.input("Employee's ID").classes('w-full mb-3')
                    self.name = ui.input('Full Name').classes('w-full mb-3')
                    self.department = ui.input('Department').classes('w-full mb-3')
                    self.position = ui.input('Position').classes('w-full mb-3')
                    self.salary = ui.input('Salary').classes('w-full mb-3')

                    with ui.row().classes('w-full justify-between mt-4'):
                        ui.button('Add', on_click=self.handle_add)
                        ui.button('Clear', on_click=self.clear_form)

                # ---------- RIGHT SIDE: TABLE + DELETE ----------
                with ui.card().classes('shadow-2 flex-1').style('background-color: #ECD5BC; min-height: 550px;'):
                    ui.label('Employee Records') \
                        .classes('text-black text-2xl font-bold mb-4')

                    columns = [
                        {'name': 'id', 'label': 'ID', 'field': 'id'},
                        {'name': 'name', 'label': 'Name', 'field': 'name'},
                        {'name': 'department', 'label': 'Department', 'field': 'department'},
                        {'name': 'position', 'label': 'Position', 'field': 'position'},
                        {'name': 'salary', 'label': 'Salary', 'field': 'salary'},
                    ]

                    # initial rows from database via callback
                    self.table = ui.table(
                        columns=columns,
                        rows=self.get_callback(),
                        row_key='id',
                        ).classes('w-full text-black').style('background-color: #ECDFCC;')

                    # Delete by ID controls
                    with ui.row().classes('w-full items-center mt-4 gap-2'):
                        self.delete_id = ui.input('ID to delete').classes('flex-1')
                        ui.button('Delete', on_click=self.handle_delete, color='negative')

    def handle_add(self) -> None:
        """Called when the Add button is clicked."""
        if not self.employee_id.value or not self.name.value:
            ui.notify('ID and Name are required!', color='red')
            return

        # --- Salary validation on the frontend ---
        if self.salary.value not in (None, ""):
            try:
                float(self.salary.value)
            except ValueError:
                ui.notify('Salary must be a numeric value!', color='red')
                return

        success = self.add_callback(
            self.employee_id.value,
            self.name.value,
            self.department.value,
            self.position.value,
            self.salary.value,
        )

        if success:
            # refresh table from database
            self.table.rows = self.get_callback()
            self.table.update()
            ui.notify('Employee added successfully!', color='green')
            self.clear_form()

    def handle_delete(self) -> None:
        """Delete employee by ID using the delete_callback."""
        emp_id = self.delete_id.value
        if not emp_id:
            ui.notify('Please enter an ID to delete.', color='red')
            return

        success = self.delete_callback(emp_id)
        if success:
            self.table.rows = self.get_callback()
            self.table.update()
            ui.notify(f'Employee with ID {emp_id} deleted.', color='green')
            self.delete_id.value = ''

    def clear_form(self) -> None:
        """Clear all form inputs."""
        self.employee_id.value = ''
        self.name.value = ''
        self.department.value = ''
        self.position.value = ''
        self.salary.value = ''