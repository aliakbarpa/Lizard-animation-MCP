@echo off
echo ========================================
echo    Creating Lizard Icon
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if Pillow is installed
python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo Pillow is not installed. Installing now...
    pip install Pillow
    if errorlevel 1 (
        echo ERROR: Failed to install Pillow
        pause
        exit /b 1
    )
    echo Pillow installed successfully!
    echo.
)

echo Creating icon...
python create_icon.py

if errorlevel 1 (
    echo ERROR: Failed to create icon
    pause
    exit /b 1
)

echo.
echo Icon created successfully: lizard_icon.ico
echo.
pause
