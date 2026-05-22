# Employee Management System 🏢

## 📖 Project Overview
This project is developed for the **Advanced Programming** module (BSc BIT). It is a fully-fledged browser-based web application built using Python. By moving away from traditional CLI applications, we implemented a robust web architecture with a frontend, backend logic, and persistent database storage.

We have created a comprehensive Employee Management System that allows administrative staff to manage employee records seamlessly from their web browser, featuring real-time statistics, dynamic filtering, and a modern UI.

## 🎯 Project Goals and Justification
The main goal of this project is to apply advanced Object-Oriented Programming (OOP) concepts and Design Patterns in a web environment. 
By utilizing **NiceGUI**, we demonstrate our understanding of client-server separation, browser session isolation, and database persistence via modern ORMs.

## 🏗️ Software Architecture & Design Patterns
Following the module's requirements and best practices, our application strictly follows the **MVC (Model-View-Controller)** design pattern:

### 1. View (Presentation Layer - `gui.py`)
- The browser acts as a thin client.
- Built using **NiceGUI** (based on Vue.js and Quasar) and styled with **Tailwind CSS**.
- Contains no direct database logic. It dynamically reacts to user inputs (e.g., dependent comboboxes for Department/Position).

### 2. Controller (Application Logic - `main.py`)
- Acts as the bridge between the View and the Model.
- Implements **Browser Tab Isolation** using NiceGUI's `@ui.page('/')` decorator, ensuring that multiple users/tabs have independent UI states.

### 3. Model (Persistence Layer - `database.py`)
- **Database:** SQLite
- **ORM:** We use **SQLModel** (SQLAlchemy + Pydantic) to interact with the database, strictly avoiding raw SQL queries.
- **Design Pattern:** The database connection utilizes the **Singleton Pattern** (`DatabaseConnection`) to ensure only one database engine pool is created across the application.

## ✨ Advanced Features
- **Live Statistics Dashboard:** Real-time calculation of Total Employees, Average Salary, and Top Department.
- **Dynamic Dependent Comboboxes:** The "Position" dropdown automatically updates based on the selected "Department".
- **Live Search & Filtering:** Instant table filtering by Name, Department, Position, or Address.
- **Smart Form Auto-Fill:** Selecting an employee from the table automatically populates the form for easy updating or deletion.
- **Auto-Incrementing IDs:** IDs are handled automatically by the database to ensure data integrity.
- **Auto-Formatting:** Inputs like employee names are automatically formatted (Title Case) before saving.

## 👤 User Stories & Use Cases
- **As an Admin**, I want to add new employees so that the company records stay up to date.
- **As an Admin**, I want to update existing employee details (e.g., salary, department) to reflect promotions.
- **As an Admin**, I want to search for specific employees dynamically to quickly find their information.
- **As an Admin**, I want to see real-time company statistics (Average Salary, etc.) to monitor company metrics.
- **As an Admin**, I want to securely delete former employees from the active database by simply selecting them from the table.

## 📦 Libraries and Technologies
- **Python 3.x**
- **NiceGUI:** For server-side UI component generation and routing.
- **SQLModel:** As the modern Object-Relational Mapper (ORM).
- **SQLite:** As the persistent relational database.

## 👥 Work Distribution and Contribution
*Note: Contribution is actively tracked via GitHub activity (commits, pull requests, and issue tracking).*

1. **Zeljko Prelic - View Layer & UI Components:** Responsible for building the initial NiceGUI interface layout, defining the Tailwind CSS styling, and setting up the visual components (forms, tables, buttons).
2. **Yücel Isbaran - Model Layer & Basic Operations:** Responsible for designing the initial database schema, creating the base CRUD operations, and setting up the foundational SQLite logic.
3. **Aykut Gül - Controller Layer, Integration & Advanced Features:** Acted as the project integrator. Refactored the database to **SQLModel**, implemented the **MVC & Singleton** architectures, established browser session isolation (`@ui.page`), and added advanced features (Live Search, Stats Dashboard, Dynamic Comboboxes, and Update functionality).

## 🚀 Installation and Run Instructions
1. Clone the repository: `git clone [repository-url]`
2. Navigate to the project folder.
3. Install required libraries: 
   ```bash
   pip install nicegui sqlmodel