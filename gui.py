from nicegui import ui


class EmployeeAppUI:
    def __init__(self,add_callback,get_callback,delete_callback,search_callback,stats_callback) -> None:
        
        
        
        
        
        
        self.build_ui()

    def build_ui(self) -> None:
        ui.query('body').style('margin: 0; background-color: #F5F7F7;')

        with ui.column().classes('w-full gap-0'):

            # HEADER
            with ui.row().classes('w-full justify-center mt-3'):
                ui.label('Employee Management System') \
                    .classes('text-white text-4xl font-bold p-4 text-center w-[95%]') \
                    .style('background-color: #6CA6A6; border-radius: 15px;')

            with ui.row().classes('w-full items-start no-wrap').style('padding: 12px; gap: 16px;'):

                # EMPLOYEE DETAILS
                with ui.card().classes('shadow-2 w-[350px]').style('background-color: #EAF2F2; min-height: 560px;'):

                    ui.label('Employee Details') \
                        .classes('text-2xl font-bold mb-3 text-gray-800')

                    ui.input("Employee's ID").classes('w-full mb-2')
                    ui.input('Full Name').classes('w-full mb-2')
                    ui.input('Address').classes('w-full mb-2')
                    ui.input('Department').classes('w-full mb-2')
                    ui.input('Position').classes('w-full mb-2')
                    ui.input('Salary').classes('w-full mb-2')

                    with ui.row().classes('w-full gap-2 mt-4'):
                        ui.button('Add').props('color=green').classes('flex-1')
                        ui.button('Update').props('color=blue').classes('flex-1')

                    with ui.row().classes('w-full gap-2 mt-2'):
                        ui.button('Delete').props('color=red').classes('flex-1')
                        ui.button('Clear').props('color=grey').classes('flex-1')

                # EMPLOYEE RECORDS
                with ui.card().classes('shadow-2 flex-1').style('background-color: #EAF2F2; min-height: 560px;'):

                    ui.label('Employee Records') \
                        .classes('text-2xl font-bold mb-3 text-gray-800')

                    # SEARCH BAR
                    with ui.row().classes('w-full bg-white p-3 rounded items-center gap-3 mb-4'):

                        ui.input('Search value').classes('flex-1')

                        ui.select(
                            ['ID', 'Name'],
                            value='ID',
                            label='Search by'
                        ).classes('w-40')

                        ui.button('Search').props('color=blue')
                        ui.button('Show All').props('color=grey')

                    # TABLE
                    columns = [
                        {'name': 'id', 'label': 'ID', 'field': 'id'},
                        {'name': 'name', 'label': 'Name', 'field': 'name'},
                        {'name': 'address', 'label': 'Address', 'field': 'address'},
                        {'name': 'department', 'label': 'Department', 'field': 'department'},
                        {'name': 'position', 'label': 'Position', 'field': 'position'},
                        {'name': 'salary', 'label': 'Salary', 'field': 'salary'},
                    ]

                    ui.table(
                        columns=columns,
                        rows=[],
                        row_key='id',
                    ).classes('w-full bg-white')


app = EmployeeApp()
ui.run(title='Employee Management System')
