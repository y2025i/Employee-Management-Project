from nicegui import ui


class EmployeeApp:
    def __init__(self) -> None:
        self.build_ui()

    def build_ui(self) -> None:
        ui.query('body').style('margin: 0;')

        with ui.column().classes('w-full gap-0'):

            ui.label('Employee Management System') \
                .classes('w-full text-center text-white text-4xl font-bold p-4') \
                .style('background-color: blue;')

            with ui.row().classes('w-full items-start').style('padding: 10px; gap: 20px;'):

                with ui.card().classes('shadow-2 w-[350px]').style('background-color: red; min-height: 550px;'):
                    ui.label('Employee Details') \
                        .classes('text-white text-2xl font-bold mb-4')

                    self.employee_id = ui.input("Employee's ID") \
                        .classes('w-full mb-3')
                    self.name = ui.input('Full Name') \
                        .classes('w-full mb-3')
                    self.department = ui.input('Department') \
                        .classes('w-full mb-3')
                    self.position = ui.input('Position') \
                        .classes('w-full mb-3')
                    self.salary = ui.input('Salary') \
                        .classes('w-full mb-3')

                    with ui.row().classes('w-full justify-between mt-4'):
                        ui.button('Add', on_click=self.add_employee)
                        ui.button('Clear', on_click=self.clear_form)

                with ui.card().classes('shadow-2 flex-1').style('background-color: red; min-height: 550px;'):
                    ui.label('Employee Records') \
                        .classes('text-white text-2xl font-bold mb-4')

                    columns = [
                        {'name': 'id', 'label': 'ID', 'field': 'id'},
                        {'name': 'name', 'label': 'Name', 'field': 'name'},
                        {'name': 'department', 'label': 'Department', 'field': 'department'},
                        {'name': 'position', 'label': 'Position', 'field': 'position'},
                        {'name': 'salary', 'label': 'Salary', 'field': 'salary'},
                    ]

                    self.rows = []
                    self.table = ui.table(
                        columns=columns,
                        rows=self.rows,
                        row_key='id',
                    ).classes('w-full bg-white')

    def add_employee(self) -> None:
        if not self.employee_id.value or not self.name.value:
            ui.notify('ID i ime su obavezni!', color='red')
            return

        self.rows.append({
            'id': self.employee_id.value,
            'name': self.name.value,
            'department': self.department.value,
            'position': self.position.value,
            'salary': self.salary.value,
        })

        self.table.rows = self.rows
        self.table.update()
        ui.notify('Zaposleni uspješno dodat!', color='green')
        self.clear_form()

    def clear_form(self) -> None:
        self.employee_id.value = ''
        self.name.value = ''
        self.department.value = ''
        self.position.value = ''
        self.salary.value = ''


app = EmployeeApp()
ui.run(title='Employee Management System')
