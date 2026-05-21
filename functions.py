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
        self.search_val.value = "