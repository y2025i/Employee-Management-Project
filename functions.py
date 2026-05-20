 def update_positions(self, event):
        selected = event.value
        if selected:
            self.position.options = self.dept_positions[selected]
        else:
            self.position.options = []
        self.position.value = None
        self.position.update()
