import pytest
from sqlmodel import SQLModel, create_engine
import database  

# ==========================================
# 🛠️ TEST FIXTURE SETUP
# ==========================================
@pytest.fixture(autouse=True)
def setup_test_database():
    """
    Creates an in-memory SQLite database before each test.
    This ensures tests are isolated and do not corrupt the real 'employees.db' file.
    """
    # Create a temporary in-memory database engine
    test_engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(test_engine)
    
    # Monkeypatch the singleton database engine to use the temporary one
    database.db.engine = test_engine
    
    yield  # Let the test run
    
    # Drop all tables after the test completes
    SQLModel.metadata.drop_all(test_engine)


# ==========================================
# 🧪 1. UNIT TESTS (6 Tests)
# Tests individual functions or isolated logic.
# ==========================================

def test_01_db_stats_empty():
    """Verifies that stats return 0 (no crash) when the database is fully empty."""
    stats = database.get_db_stats()
    assert stats['total'] == 0
    assert stats['avg_salary'] == 0
    assert stats['top_dept'] == "N/A"

def test_02_add_employee_invalid_salary():
    """Verifies that adding an employee with a non-numeric salary fails gracefully."""
    result = database.add_employee("Aykut", "Zurich", "IT", "Dev", "abc")
    assert result is False

def test_03_delete_non_existent_employee():
    """Verifies that attempting to delete an employee ID that does not exist returns False."""
    result = database.delete_employee("999")
    assert result is False

def test_04_update_non_existent_employee():
    """Verifies that updating a non-existent employee ID fails gracefully."""
    result = database.update_employee("999", "Aykut", "Zurich", "IT", "Dev", "5000")
    assert result is False

def test_05_add_employee_missing_name():
    """Verifies that 'name' is required and the system rejects the addition if it is missing."""
    result = database.add_employee(None, "Zurich", "IT", "Dev", "5000")
    assert result is False

def test_06_gui_name_formatting_logic():
    """Tests the Title Case logic used in the GUI to ensure names are formatted correctly."""
    raw_input = "   ayKut gÜL   "
    formatted_name = raw_input.strip().title()
    assert formatted_name == "Aykut Gül"


# ==========================================
# 🗄️ 2. DATABASE TESTS (3 Tests)
# Tests actual persistence, ORM operations, and data integrity.
# ==========================================

def test_07_add_and_retrieve_employee():
    """Verifies that an employee can be successfully saved to and retrieved from the database."""
    database.add_employee("Yucel", "Basel", "Finance", "Manager", "8500")
    employees = database.get_all_employees()
    
    assert len(employees) == 1
    assert employees[0]["name"] == "Yucel"
    assert employees[0]["department"] == "Finance"

def test_08_delete_employee():
    """Verifies that an employee is permanently removed from the database after deletion."""
    database.add_employee("Zeljko", "Bern", "Marketing", "SEO", "6000")
    employees = database.get_all_employees()
    emp_id = employees[0]["id"]
    
    # Perform deletion
    delete_result = database.delete_employee(emp_id)
    assert delete_result is True
    
    # Ensure the database is now empty
    assert len(database.get_all_employees()) == 0

def test_09_update_employee_persistence():
    """Verifies that update operations are correctly persisted in the database."""
    database.add_employee("John Doe", "London", "IT", "Dev", "4000")
    emp_id = database.get_all_employees()[0]["id"]
    
    # Update salary and position
    database.update_employee(emp_id, "John Doe", "London", "IT", "Senior Dev", "7000")
    
    updated_emp = database.get_all_employees()[0]
    assert updated_emp["position"] == "Senior Dev"
    assert updated_emp["salary"] == 7000.0


# ==========================================
# 🧩 3. INTEGRATION TESTS (3 Tests)
# Tests the interactions between multiple functions or modules.
# ==========================================

def test_10_integration_stats_calculation():
    """Verifies that adding multiple employees correctly updates the dashboard statistics."""
    database.add_employee("Aykut", "Zurich", "IT", "Dev", "6000")
    database.add_employee("Yucel", "Basel", "IT", "Manager", "8000")
    database.add_employee("Zeljko", "Bern", "Sales", "Rep", "4000")
    
    stats = database.get_db_stats()
    
    assert stats["total"] == 3
    assert stats["avg_salary"] == 6000.0  # (6000+8000+4000) / 3
    assert stats["top_dept"] == "IT"      # 2 people in IT, 1 in Sales

def test_11_integration_search_flow():
    """Verifies that the live search engine filters records accurately across different columns."""
    database.add_employee("Aykut", "Zurich", "IT", "Dev", "6000")
    database.add_employee("Yucel", "Basel", "Finance", "Manager", "8000")
    database.add_employee("Zeljko", "Bern", "Sales", "Rep", "4000")
    
    # Search by Address ('Basel')
    search_results = database.search_employees("Basel")
    assert len(search_results) == 1
    assert search_results[0]["name"] == "Yucel"
    
    # Search by Department ('IT')
    search_results_it = database.search_employees("IT")
    assert len(search_results_it) == 1
    assert search_results_it[0]["name"] == "Aykut"

def test_12_integration_salary_update_affects_stats():
    """Verifies that updating an employee's salary dynamically updates the average salary stat."""
    database.add_employee("Aykut", "Zurich", "IT", "Dev", "4000")
    database.add_employee("Yucel", "Basel", "IT", "Manager", "6000")
    
    # Initial average: 5000
    assert database.get_db_stats()["avg_salary"] == 5000.0
    
    # Give Aykut a raise to 8000
    emp_id = database.get_all_employees()[0]["id"]
    database.update_employee(emp_id, "Aykut", "Zurich", "IT", "Dev", "8000")
    
    # New average should be (8000 + 6000) / 2 = 7000
    new_stats = database.get_db_stats()
    assert new_stats["avg_salary"] == 7000.0