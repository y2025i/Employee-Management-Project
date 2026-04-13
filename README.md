Employee Management System 🏢

# Employee Management System 🏢

## 📖 Project Overview
This project is developed for the **Advanced Programming** module (BSc BIT). It is a fully-fledged browser-based web application built using Python, focusing on a robust architecture with a frontend, backend logic, and persistent database storage.

We have chosen to create a comprehensive Employee Management System that allows HR or administrative staff to manage employee records seamlessly from their web browser.

## 🎯 Project Goals and Justification
The main goal of this project is to apply object-oriented programming concepts in a web environment. By migrating traditional desktop GUI applications to a modern browser-based architecture using **NiceGUI**, we aim to demonstrate our understanding of client-server separation, application state management, and database persistence via ORMs.

## 🏗️ Software Architecture
Following the module's requirements, our application is structured into the required layers:

### 1. Presentation Layer (Client-Side View)
- The browser acts as a thin client.
- The UI components are rendered using a generic engine based on Vue.js and Quasar.
- It contains no business logic or persistent application state.

### 2. Application Logic (Server-Side Frontend & Backend)
- Built using **NiceGUI** (`https://nicegui.io`), allowing us to run the Python app in the browser.
- UI components (e.g., `ui.button`, `ui.input`) are instantiated as Python objects on the server.
- The state of these objects (values, visibility) resides on the server.
- Object-oriented programming principles are used to organize business logic into modular, reusable, and self-contained units.

### 3. Persistence Layer (Database)
- **Database:** SQLite
- We interact with the physical data store using an **Object-Relational Mapper (ORM)**, completely avoiding direct SQL statements to ensure code security and maintainability.

## 👤 User Stories & Use Cases
- **As an Admin**, I want to add new employees so that the company records stay up to date.
- **As an Admin**, I want to update existing employee titles or salaries to reflect promotions.
- **As an Admin**, I want to search for specific employees by ID or name to quickly find their information.
- **As an Admin**, I want to delete former employees from the active database.
- **Use Case 1 (Add Employee):** Admin enters ID, Name, Title, Salary, and Address. The system validates the inputs and saves the new object via ORM to the SQLite database.
- **Use Case 2 (Display All):** The system fetches all employee objects from the database via ORM and dynamically generates a table view on the client-side browser.

## 📦 Libraries and Technologies
- **Python 3.x**
- **NiceGUI:** For server-side UI component generation.
- **SQLAlchemy (or chosen ORM):** For database interactions.
- **SQLite:** As the persistent database.

## 👥 Work Distribution and Contribution
*Note: Contribution is actively tracked via GitHub activity (commits, pull requests, and issue tracking).*

1. Zeljko Prelic - Application Logic & UI Components:** Responsible for building the NiceGUI interface, organizing the server-side Python objects, and connecting frontend actions to backend logic.
2. Aykut Gül - Persistence Layer & ORM:** Responsible for setting up the SQLite database, defining data models, and implementing ORM queries (SQLAlchemy) to replace raw SQL.
3. Yücel Isbaran - Architecture & Integration:** Responsible for ensuring the strict separation between the Presentation Layer and Application Logic, handling project documentation, and integrating the ORM with the UI components.

## 🚀 Installation and Run Instructions
1. Clone the repository: `git clone [repository-url]`
2. Navigate to the project folder.
3. Install required libraries: `pip install nicegui sqlalchemy`
4. Run the main file: `python main.py`
5. The application will automatically open in your default web browser (usually at `http://localhost:8080`).

## 📅 Milestones & Deadlines
- **Final Submission:** May 24, 2026, at 11:55 PM (Moodle Upload)
- **Final Presentation:** Includes live demo, source code explanation, and QA session.

📝 License
This project is created by Yücel Isbaran, Aykut Gül and Zeljko Prelic