from nicegui import ui


class EmployeeAppUI:
<<<<<<< HEAD
    def __init__(self, add_callback, get_callback, delete_callback, search_callback, stats_callback, update_callback) -> None:
        self.add_callback=add_callback
        self.get_callback=get_callback
        self.search_callback=search_callback
        self.delete_callback=delete_callback
        self.stats_callback=stats_callback
        self.update_callback=update_callback

        #departments and Positions 
        self.dept_positions = {
            "IT": ["Software Engineer", "Data Analyst", "System Admin"],
            "Human Resources": ["HR Specialist", "Recruiter", "HR Manager"],
            "Finance": ["Financial Analyst", "Accountant", "Finance Manager"],
            "Marketing": ["Marketing Executive", "SEO Specialist"],
            "Sales": ["Sales Representative", "Sales Manager"],
            "Operations": ["Operations Coordinator"],
            "Management": ["Director", "CEO"]
                                            }       
=======
    def __init__(self, add_callback, get_callback, delete_callback) -> None:
        """UI layer. It does NOT talk to the database directly.
        add_callback: function to add an employee (defined in main.py)
        get_callback: function to load all employees (defined in main.py)
        delete_callback: function to delete an employee by ID (defined in main.py)
        """
        self.add_callback = add_callback
        self.get_callback = get_callback
        self.delete_callback = delete_callback
>>>>>>> 5a630fd117b97f180a5cffb53250181777b57f10
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

<<<<<<< HEAD
                    self.employee_id=ui.input("Emplotee's ID").classes("w-full mb-2").props('readonly placeholder="Select from table"')
                    self.name=ui.input("Full Name").classes("w-full mb-2")
                    self.Address=ui.input("Address").classes("w-full mb-2")
                    self.department =ui.select(list(self.dept_positions.keys()), label='Department',on_change=self.update_positions).classes("w-full mb-2")
                    self.position=ui.select([],label='Position').classes('w-full mb-2') #add select from list
                    self.salary=ui.input('Salary').classes('w-full mb-2')
=======
                    self.employee_id = ui.input("Employee's ID").classes('w-full mb-3')
                    self.name = ui.input('Full Name').classes('w-full mb-3')
                    self.department = ui.input('Department').classes('w-full mb-3')
                    self.position = ui.input('Position').classes('w-full mb-3')
                    self.salary = ui.input('Salary').classes('w-full mb-3')
>>>>>>> 5a630fd117b97f180a5cffb53250181777b57f10

                    with ui.row().classes('w-full justify-between mt-4'):
                        ui.button('Add', on_click=self.handle_add)
                        ui.button('Clear', on_click=self.clear_form)

<<<<<<< HEAD
                    ui.label('Employee Records').classes('text-2xl font-bold mb-3 text-gray-800')

                    # SEARCH BAR
                    with ui.row().classes('w-full bg-white p-3 rounded items-center gap-3 mb-4'):

                        self.search_val=ui.input('Search value', on_change=self.handle_search).classes('flex-1')
                        ui.button("Search",on_click=lambda: self.handle_search(self.search_val)).props("color=blue")
                        ui.button("Show All",on_click=self.refresh_ui).props("color=gray")
                    

                    # TABLE
=======
                # ---------- RIGHT SIDE: TABLE + DELETE ----------
                with ui.card().classes('shadow-2 flex-1').style('background-color: #ECD5BC; min-height: 550px;'):
                    ui.label('Employee Records') \
                        .classes('text-black text-2xl font-bold mb-4')

>>>>>>> 5a630fd117b97f180a5cffb53250181777b57f10
                    columns = [
                        {'name': 'id', 'label': 'ID', 'field': 'id'},
                        {'name': 'name', 'label': 'Name', 'field': 'name'},
                        {'name': 'department', 'label': 'Department', 'field': 'department'},
                        {'name': 'position', 'label': 'Position', 'field': 'position'},
                        {'name': 'salary', 'label': 'Salary', 'field': 'salary'},
                    ]            



                    self.table =ui.table(columns=columns,row=self.get_callback(),row_key="id",selection="single").classes("w-full bg-white").on("selection,self.handle_table_select")
                             
#here will be the functions. 

<<<<<<< HEAD
=======
                    # initial rows from database via callback
                    self.table = ui.table(
                        columns=columns,
                        rows=self.get_callback(),
                        row_key='id',
                        ).classes('w-full text-black').style('background-color: #ECDFCC;')
>>>>>>> 5a630fd117b97f180a5cffb53250181777b57f10

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