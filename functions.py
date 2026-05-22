 def update_positions(self, event):
        selected = event.value
        if selected:
            self.position.options = self.dept_positions[selected]
        else:
            self.position.options = []
        self.position.value = None
        self.position.update()
#additional function

 def handle_table_select(self, e) -> None:
        selected = self.table.selected
        if selected:
            row = selected[0]
            self.employee_id.value = str(row['id'])
            self.name.value = row['name']
            self.address.value = row['address']
            self.department.value = row['department']
            if row['department'] in self.dept_positions:
                self.position.options = self.dept_positions[row['department']]
            self.position.value = row['position']
            self.salary.value = str(row['salary'])


def refresh_ui(self):
        self.table.rows = self.get_callback()
        self.table.update()
        stats = self.stats_callback()
        self.stat_total.text = str(stats['total'])
        self.stat_avg.text = f"${stats['avg_salary']}"
        self.stat_dept.text = stats['top_dept']
        self.search_val.value = ""
        


  def handle_add(self):
        if not self.name.value:
            ui.notify('Name is required!', color='red')
            return
        if self.salary.value not in (None, ""):
            try:
                float(self.salary.value)
            except ValueError:
                ui.notify('Salary must be a numeric value!', color='red')
                return

        formatted_name = self.name.value.strip().title()
        dept_val = self.department.value if self.department.value else ""
        pos_val = self.position.value if self.position.value else ""
        address_val = self.address.value if self.address.value else ""

        success = self.add_callback(formatted_name, address_val, dept_val, pos_val, self.salary.value)
        if success:
            self.refresh_ui()
            ui.notify('Employee added successfully!', color='green')
            self.clear_form()
             #Update Functions
    def handle_update(self):
        if not self.employee_id.value:
            ui.notify('Please select an employee from the table to update!', color='warning')
            return
        if not self.name.value:
            ui.notify('Name is required!', color='red')
            return
        if self.salary.value not in (None, ""):
            try:
                float(self.salary.value)
            except ValueError:
                ui.notify('Salary must be a numeric value!', color='red')
                return

        formatted_name = self.name.value.strip().title()
        dept_val = self.department.value if self.department.value else ""
        pos_val = self.position.value if self.position.value else ""
        address_val = self.address.value if self.address.value else ""

        success = self.update_callback(self.employee_id.value, formatted_name, address_val, dept_val, pos_val, self.salary.value)
        if success:
            self.refresh_ui()
            self.table.selected = []
            ui.notify(f'Employee {self.employee_id.value} updated successfully!', color='blue')
            self.clear_form()
        else:
            ui.notify('Failed to update employee.', color='red')

    def handle_search(self, e):
        query = e.value if hasattr(e, 'value') else e
        if not query:
            self.table.rows = self.get_callback()
        else:
            self.table.rows = self.search_callback(query)
        self.table.update()

    def handle_delete(self):
        selected = self.table.selected
        if not selected:
            ui.notify('Please select an employee from the table first!', color='warning')
            return
        
        emp_id = selected[0]['id']
        if self.delete_callback(emp_id):
            self.refresh_ui()
            self.table.selected = []
            ui.notify(f'Employee {emp_id} deleted.', color='green')
            self.clear_form()

    def clear_form(self) -> None:
        self.employee_id.value = ''
        self.name.value = ''
        self.address.value = ''
        self.department.value = None
        self.position.options = []
        self.position.value = None
        self.salary.value = ''

