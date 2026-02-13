@echo off
setlocal

:: Navigate to the backend directory
cd /d "%~dp0..\backend"
if %errorlevel% neq 0 (
    echo [ERROR] Could not find backend directory at %~dp0..\backend
    pause
    exit /b 1
)

set "VENV_DIR=final_venv"

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b 1
)

:: Check if virtual environment exists
if not exist "%VENV_DIR%" (
    echo [INFO] Creating virtual environment...
    python -m venv "%VENV_DIR%"
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
)

:: Activate virtual environment
echo [INFO] Activating virtual environment...
call "%VENV_DIR%\Scripts\activate"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b 1
)

:: Install dependencies
echo [INFO] Installing dependencies...
python -m pip install --upgrade pip
if exist "requirements.txt" (
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install dependencies.
        pause
        exit /b 1
    )
) else (
    echo [WARNING] requirements.txt not found.
)

:: Check MongoDB Connection
echo [INFO] Checking MongoDB connection...
python verify_db.py
if %errorlevel% neq 0 (
    echo [ERROR] MongoDB check failed.
    echo [HINT] Ensure MongoDB is running or MONGO_URI is set correctly in backend/.env
    echo [HINT] If using local MongoDB, make sure MongoDB Community Server is installed and the service is started.
    pause
    exit /b 1
)

:: Start the server and open the browser
echo [INFO] Starting backend server...
start "" "http://localhost:5000/police/login"
python app.py

if %errorlevel% neq 0 (
    echo [ERROR] Backend server crashed.
    pause
    exit /b 1
)

pause
endlocal