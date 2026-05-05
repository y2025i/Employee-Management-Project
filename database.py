import sqlite3
from typing import List, Dict, Any


DB_NAME = "employees.db"


def get_connection():
    """Open a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # rows -> dict-like access
    return conn


def init_db() -> None:
    """Create the employees table if it does not exist."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            position TEXT,
            salary REAL
        );
        """
    )

    conn.commit()
    conn.close()


def add_employee(emp_id: str, name: str, department: str,
                 position: str, salary: str) -> bool:
    """Insert a new employee into the database. Returns True if success."""
    try:
        conn = get_connection()
        cur = conn.cursor()

        # convert salary to float if possible
        salary_value = float(salary) if salary not in (None, "") else None

        cur.execute(
            """
            INSERT INTO employees (id, name, department, position, salary)
            VALUES (?, ?, ?, ?, ?);
            """,
            (emp_id, name, department, position, salary_value),
        )

        conn.commit()
        conn.close()
        return True

    except sqlite3.IntegrityError:
        # ID already exists
        conn.close()
        return False


def get_all_employees() -> List[Dict[str, Any]]:
    """Return all employees as a list of dictionaries."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, department, position, salary FROM employees;")
    rows = cur.fetchall()
    conn.close()

    return [
        {
            "id": row["id"],
            "name": row["name"],
            "department": row["department"],
            "position": row["position"],
            "salary": row["salary"],
        }
        for row in rows
    ]

def delete_employee(emp_id: str) -> bool:
    """Delete employee by ID. Returns True if a row was deleted."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM employees WHERE id = ?;", (emp_id,))
    deleted_rows = cur.rowcount

    conn.commit()
    conn.close()

    return deleted_rows > 0