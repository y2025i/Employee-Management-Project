'''import sqlite3
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

    return deleted_rows > 0'''

from sqlmodel import Field, SQLModel, create_engine, Session, select, or_
from typing import Optional, List, Dict, Any




class Employee(SQLModel,table=True):
    __tablename__="employees"

    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    address:Optional[str]=None
    depatment:Optional[str]=None
    position:Optional[str]=None
    salary:Optional[float]=None



    class DatabaseConnection:
        _instance=None
        

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls) #DatabaseConnection,cls
                cls._instance.engine=create_engine("sqlite:///employees.db",echo=False)
                SQLModel.metadata.create_all(cls._instance.engine)
                return cls._instance
    db=DatabaseConnection()
    def init_db() -> None:
        SQLModel.metadata.create_all(db.engine)

def add_employee(name: str, address: str, department: str, position: str, salary: str) -> bool:
    try:
        salary_value = float(salary) if salary not in (None, "") else None
        new_emp = Employee(name=name, address=address, department=department, position=position, salary=salary_value)
        with Session(db.engine) as session:
            session.add(new_emp)
            session.commit()
            session.refresh(new_emp)
            return True
    except Exception:
        return False

def get_all_employees() -> List[Dict[str, Any]]:
    with Session(db.engine) as session:
        rows = session.exec(select(Employee)).all()
        return [
            {
                "id": str(row.id),
                "name": row.name,
                "address": row.address if row.address else "",
                "department": row.department if row.department else "",
                "position": row.position if row.position else "",
                "salary": row.salary if row.salary is not None else "",
            }
            for row in rows
        ]

# ADVANCED: Seçilen Personeli Güncelleme Fonksiyonu
def update_employee(emp_id: str, name: str, address: str, department: str, position: str, salary: str) -> bool:
    try:
        int_id = int(emp_id)
        salary_value = float(salary) if salary not in (None, "") else None
        with Session(db.engine) as session:
            emp = session.get(Employee, int_id)
            if emp:
                emp.name = name
                emp.address = address
                emp.department = department
                emp.position = position
                emp.salary = salary_value
                session.add(emp)
                session.commit()
                return True
            return False
    except Exception:
        return False

def delete_employee(emp_id: str) -> bool:
    try:
        int_id = int(emp_id)
        with Session(db.engine) as session:
            emp = session.get(Employee, int_id)
            if emp:
                session.delete(emp)
                session.commit()
                return True
            return False
    except ValueError:
        return False

def search_employees(query_str: str) -> List[Dict[str, Any]]:
    with Session(db.engine) as session:
        pattern = f"%{query_str}%"
        statement = select(Employee).where(
            or_(
                Employee.name.ilike(pattern),
                Employee.address.ilike(pattern),
                Employee.department.ilike(pattern),
                Employee.position.ilike(pattern)
            )
        )
        rows = session.exec(statement).all()
        return [
            {
                "id": str(row.id),
                "name": row.name,
                "address": row.address if row.address else "",
                "department": row.department if row.department else "",
                "position": row.position if row.position else "",
                "salary": row.salary if row.salary is not None else "",
            }
            for row in rows
        ]

def get_db_stats() -> Dict[str, Any]:
    with Session(db.engine) as session:
        rows = session.exec(select(Employee)).all()
        total = len(rows)
        if total == 0:
            return {"total": 0, "avg_salary": 0, "top_dept": "N/A"}
        salaries = [r.salary for r in rows if r.salary is not None]
        avg_salary = sum(salaries) / len(salaries) if salaries else 0
        depts = [r.department for r in rows if r.department not in (None, "")]
        top_dept = max(set(depts), key=depts.count) if depts else "N/A"
        return {"total": total, "avg_salary": round(avg_salary, 2), "top_dept": top_dept}
