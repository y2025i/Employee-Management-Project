@echo off
color 0A
echo =======================================================
echo     EMPLOYEE MANAGEMENT SYSTEM - AUTO SETUP
echo =======================================================
echo.
echo This script will automatically install all required
echo libraries (NiceGUI, SQLAlchemy etc.) on your computer.
echo Please DO NOT CLOSE this window until the process is done!
echo.
pause
echo.

echo [STEP 1/3] Creating virtual environment (.venv)...
python -m venv .venv
if errorlevel 1 (
    color 0C
    echo.
    echo ERROR: Python is not installed or not added to PATH!
    echo Please install Python and try again.
    pause
    exit /b
)
echo Success!
echo.

echo [STEP 2/3] Activating virtual environment and installing libraries...
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    color 0C
    echo.
    echo ERROR: Something went wrong while installing libraries.
    echo Please check your internet connection and try again.
    pause
    exit /b
)
echo.

color 0A
echo =======================================================
echo    [STEP 3/3] SETUP COMPLETED SUCCESSFULLY!
echo =======================================================
echo.
echo You can now open VS Code and start coding!
echo IMPORTANT: Select the Python Interpreter as '.venv (Workspace)'
echo from the bottom-right corner of VS Code before running the app.
echo.
pause