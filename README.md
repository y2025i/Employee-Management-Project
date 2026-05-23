# Employee Management System 🏢

## 📖 Project Overview

This project was developed for the **Advanced Programming** module (BSc BIT, Spring 2026). It is a browser-based web application built with **Python** and **NiceGUI**, using a clear separation of frontend, backend, and database layers. 

The application is an **Employee Management System** that allows administrative staff to manage employee records directly from the browser. It supports adding, updating, searching, and deleting employees, and displays real-time statistics such as total employees, average salary, and top department.

***

## 🎯 Project Goals and Motivation

- Apply **advanced OOP concepts** and **design patterns** in a realistic project.
- Build a **web-based** application (not CLI) using **NiceGUI** as the UI layer. 
- Use a **relational database (SQLite)** with a modern **ORM (SQLModel)** instead of raw SQL.
- Demonstrate clean separation between:
  - UI (View),
  - Application logic (Controller),
  - Persistence (Model).

From a business perspective, the goal is to provide a simple but powerful tool for managing employee data, including quick search and aggregate statistics.

***

## 🏗️ Architecture & Design Patterns

The application follows an MVC-like structure adapted for NiceGUI:

### 1. View – `gui.py`

- Implemented with **NiceGUI** components (cards, tables, inputs, buttons).
- Contains **no direct database calls**; it only uses callback functions passed from `main.py`.
- Features:
  - Employee Details form (ID, Name, Address, Department, Position, Salary).
  - Dependent dropdowns: **Position** options change dynamically based on selected **Department**.
  - Search bar with **Search** and **Show All** buttons.
  - Employee table with **single row selection**, used to auto-fill the form for updates or deletion.
  - Live statistics dashboard showing:
    - Total Employees
    - Average Salary
    - Top Department

### 2. Controller – `main.py`

- Acts as the **bridge** between the UI and the database layer.
- On startup:
  - Calls `database.init_db()` to ensure tables exist.
- Defines a set of **callback functions**:
  - `add_employee_to_db(...)`
  - `get_employees_from_db()`
  - `delete_employee_from_db(emp_id)`
  - `search_employees_in_db(query)`
  - `get_application_stats()`
  - `update_employee_in_db(...)`
- These callbacks are passed into `EmployeeAppUI`:

```python
EmployeeAppUI(
    add_callback=add_employee_to_db,
    get_callback=get_employees_from_db,
    delete_callback=delete_employee_from_db,
    search_callback=search_employees_in_db,
    stats_callback=get_application_stats,
    update_callback=update_employee_in_db,
)
```

- The NiceGUI route `@ui.page('/')` is used for **browser tab isolation**: each tab has its own UI state.

### 3. Model – `database.py`

- **Database:** SQLite (`employees.db` file).
- **ORM:** `SQLModel` (built on top of SQLAlchemy + Pydantic).
- **Design Pattern:**  
  - Uses a **Singleton** (`DatabaseConnection`) to ensure only one database engine instance is created and reused:

    ```python
    class DatabaseConnection:
        _instance = None
        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.engine = create_engine("sqlite:///employees.db", echo=False)
                SQLModel.metadata.create_all(cls._instance.engine)
            return cls._instance
    db = DatabaseConnection()
    ```

- **ORM Model:**

  ```python
  class Employee(SQLModel, table=True):
      id: Optional[int] = Field(default=None, primary_key=True)
      name: str
      address: Optional[str] = None
      department: Optional[str] = None
      position: Optional[str] = None
      salary: Optional[float] = None
  ```

- **Key functions:**
  - `add_employee(name, address, department, position, salary) -> bool`
    - Validates and converts salary to float, creates and commits an `Employee`.
  - `get_all_employees() -> List[Dict]`
    - Returns all employees in a dict format that the UI table can directly consume.
  - `update_employee(emp_id, ...) -> bool`
    - Finds an employee by ID, updates fields, and persists changes.
  - `delete_employee(emp_id) -> bool`
    - Deletes an employee if it exists.
  - `search_employees(query_str) -> List[Dict]`
    - Case-insensitive search over `name`, `address`, `department`, and `position` using `ilike` and `or_`.
  - `get_db_stats() -> Dict[str, Any]`
    - Computes:
      - `total`: number of employees.
      - `avg_salary`: average of all non-null salaries (rounded to 2 decimals).
      - `top_dept`: department with the most employees (or `"N/A"` if none).

***

## ✨ Application Features

- **Employee CRUD:**
  - Add new employees with name, address, department, position, and salary.
  - Update selected employee through form auto-fill.
  - Delete selected employee using the table selection and “Delete Selected” button.
- **Auto-formatted input:**
  - Names are trimmed and converted to Title Case before saving (e.g., `"   ayKut gÜL   "` → `"Aykut Gül"`).
- **Dependent dropdowns:**
  - When a department is selected, the position dropdown automatically updates with relevant roles.
- **Search & Filter:**
  - Search bar filters records across multiple fields (name, address, department, position).
  - “Show All” resets the table to all employees.
- **Statistics Dashboard:**
  - Top row shows Total Employees, Average Salary, and Top Department, always based on the current database state.
- **Form auto-fill from table:**
  - Selecting a row in the table automatically fills the Employee Details form for easy update or deletion.

***

## 🧪 Automated Testing

In line with the module’s expectations, the project includes **12 automated tests** written with **pytest**: [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/69401155/19f17c86-9454-4918-9d98-cc4b627d3a61/Email-Yucel-Isbaran-s-Outlook.pdf)

- **Test file:** `test_app.py`
- **In‑memory testing setup:**
  - Uses `sqlite:///:memory:` as a temporary database for each test.
  - The fixture `setup_test_database` redirects `database.db.engine` to this in-memory engine and drops all tables afterwards, ensuring tests do not affect `employees.db`.

### Test Mix (12 tests)

1. **6 Unit Tests**
   - Validate behavior of:
     - `get_db_stats()` on an empty database.
     - `add_employee` with invalid salary (string).
     - `add_employee` with missing name.
     - `delete_employee` on a non-existent ID.
     - `update_employee` on a non-existent ID.
     - Name formatting logic used in the GUI (Title Case).

2. **3 Database Tests**
   - Check persistence and integrity:
     - Adding and retrieving an employee.
     - Deleting an employee and ensuring DB is empty afterwards.
     - Updating an employee and verifying the new salary and position values.

3. **3 Integration Tests**
   - Validate interaction between multiple functions:
     - Stats after adding multiple employees (total, average salary, top department).
     - Search flow (filtering by address and department).
     - Effect of salary updates on the average salary statistic.

Running all tests:

```bash
pytest
```

Output: `12 passed` (all tests successful).

***

## 👤 User Stories

- As an Admin, I want to **add** new employees so that the company records stay up to date.
- As an Admin, I want to **update** existing employee details (e.g., salary, department, position) to reflect promotions and changes.
- As an Admin, I want to **search** employees dynamically by name, department, position, or address to quickly find information.
- As an Admin, I want to **see real-time statistics** (Total Employees, Average Salary, Top Department) to monitor company metrics.
- As an Admin, I want to **delete** employees by selecting them in the table, to keep the database clean and relevant.

***

## 📦 Technologies Used

- **Python 3.x**
- **NiceGUI** – for server-side UI components and routing.
- **SQLModel** – modern ORM combining SQLAlchemy and Pydantic.
- **SQLite** – lightweight relational database.
- **Pytest** – for automated unit, database, and integration tests.

***

## 👥 Work Distribution

> Contributions are also visible via GitHub commits and pull requests.

1. **Zeljko Prelic – View Layer & UI Components**
   - Initial NiceGUI layout and component structure.
   - Styling of forms, buttons, and table.
   - Implementation of the EmployeeAppUI layout and dependent dropdown logic.

2. **Yücel Isbaran – Model Layer & Basic Operations**
   - Initial database schema and CRUD operations.
   - Input validation behavior (salary checks, required fields).
   - Integration of database functions with GUI callbacks.

3. **Aykut Gül – Controller, Integration & Advanced Features**
   - Refactoring to **SQLModel** ORM and Singleton database connection.
   - Wiring of callbacks in `main.py` (MVC bridge).
   - Implementation of search, statistics dashboard, and update/delete flows.
   - Design and implementation of the automated test suite (`test_app.py`).

***

## 🚀 Installation and Run Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Employee-Management-Project
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS / Linux
   ```

3. **Install required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

   (Or manually: `pip install nicegui sqlmodel pytest`)

4. **Run the application:**

   ```bash
   python main.py
   ```

5. **Open in browser:**

   - Navigate to: `http://localhost:8080`

6. **Run tests (optional but recommended):**

   ```bash
   pytest
   ```
