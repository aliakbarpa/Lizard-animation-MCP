@echo off
echo ========================================
echo    Skeleton Lizard - Complete Setup
echo ========================================
echo.
echo This will:
echo 1. Install required packages (Pillow)
echo 2. Create the lizard icon
echo 3. You can then run or build the application
echo.
pause

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Install Pillow for icon creation
echo Installing Pillow...
pip install Pillow pygame
if errorlevel 1 (
    echo WARNING: Failed to install some packages
)

REM Create icon
echo.
echo Creating lizard icon...
python create_icon.py

if errorlevel 1 (
    echo ERROR: Failed to create icon
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo Icon created: lizard_icon.ico
echo.
echo You can now:
echo - Double-click run_lizard.bat to run the application
echo - Double-click build_executable.bat to create .exe file
echo.
pause
