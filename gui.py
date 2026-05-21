from nicegui import ui


class EmployeeAppUI:
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
        self.build_ui()



    def build_ui(self) -> None:
        ui.query('body').style('margin: 0; background-color: #F5F7F7;')

        with ui.column().classes('w-full gap-4'):
            
            # HEADER
            with ui.row().classes('w-full justify-center mt-3'):
                ui.label('Employee Management System') \
                    .classes('text-white text-4xl font-bold p-4 text-center w-[95%]') \
                    .style('background-color: #6CA6A6; border-radius: 15px;')
            #Statistics
            stats = self.stats_callback()
            with ui.row().classes('w-[95%] mx-auto justify-between gap-4'):
                with ui.card().classes('flex-1 items-center p-3 shadow-1').style('background-color: #EAF2F2;'):
                    ui.label('Total Employees').classes('text-gray-600 text-sm')
                    self.stat_total = ui.label(str(stats['total'])).classes('text-2xl font-bold text-gray-800')
                with ui.card().classes('flex-1 items-center p-3 shadow-1').style('background-color: #EAF2F2;'):
                    ui.label('Average Salary').classes('text-gray-600 text-sm')
                    self.stat_avg = ui.label(f"${stats['avg_salary']}").classes('text-2xl font-bold text-gray-800')
                with ui.card().classes('flex-1 items-center p-3 shadow-1').style('background-color: #EAF2F2;'):
                    ui.label('Top Department').classes('text-gray-600 text-sm')
                    self.stat_dept = ui.label(stats['top_dept']).classes('text-2xl font-bold text-gray-800')
            with ui.row().classes('w-full items-start no-wrap').style('padding: 12px; gap: 16px;'):

                # EMPLOYEE DETAILS
                with ui.card().classes('shadow-2 w-[350px]').style('background-color: #EAF2F2; min-height: 560px;'):

                    ui.label('Employee Details').classes('text-2xl font-bold mb-3 text-gray-800')

                    self.employee_id=ui.input("Emplotee's ID").classes("w-full mb-2").props('readonly placeholder="Select from table"')
                    self.name=ui.input("Full Name").classes("w-full mb-2")
                    self.Address=ui.input("Address").classes("w-full mb-2")
                    self.department =ui.select(list(self.dept_positions.keys()), label='Department',on_change=self.update_positions).classes("w-full mb-2")
                    self.position=ui.select([],label='Position').classes('w-full mb-2') #add select from list
                    self.salary=ui.input('Salary').classes('w-full mb-2')

                    with ui.row().classes('w-full gap-2 mt-4'):
                        ui.button('Add',on_click=self.handle_add).props('color=green').classes('flex-1')
                        ui.button('Update', on_click=self.handle_update).props('color=blue').classes('flex-1')

                    with ui.row().classes('w-full gap-2 mt-2'):
                        ui.button('Delete Selected',on_click=self.handle_delete).props('color=red').classes('flex-1')
                        ui.button('Clear',on_click=self.clear_form).props('color=grey').classes('flex-1')

                # EMPLOYEE RECORDS
                with ui.card().classes('shadow-2 flex-1').style('background-color: #EAF2F2; min-height: 560px; max-width: 800px;'):

                    ui.label('Employee Records').classes('text-2xl font-bold mb-3 text-gray-800')

                    # SEARCH BAR
                    with ui.row().classes('w-full bg-white p-3 rounded items-center gap-3 mb-4'):

                        self.search_val=ui.input('Search value', on_change=self.handle_search).classes('flex-1')
                        ui.button("Search",on_click=lambda: self.handle_search(self.search_val)).props("color=blue")
                        ui.button("Show All",on_click=self.refresh_ui).props("color=gray")
                    

                    # TABLE
                    columns = [
                        {'name': 'id', 'label': 'ID', 'field': 'id'},
                        {'name': 'name', 'label': 'Name', 'field': 'name'},
                        {'name': 'address', 'label': 'Address', 'field': 'address'},
                        {'name': 'department', 'label': 'Department', 'field': 'department'},
                        {'name': 'position', 'label': 'Position', 'field': 'position'},
                        {'name': 'salary', 'label': 'Salary', 'field': 'salary'},
                    ]            



                    self.table =ui.table(columns=columns,row=self.get_callback(),row_key="id",selection="single").classes("w-full bg-white").on("selection,self.handle_table_select")
                             
#here will be the functions. 



app = EmployeeAppUI()
ui.run(title='Employee Management System')
