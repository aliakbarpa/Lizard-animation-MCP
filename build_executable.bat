@echo off
echo ========================================
echo    Building Lizard Follower Executable
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo PyInstaller is not installed. Installing now...
    pip install pyinstaller
    if errorlevel 1 (
        echo ERROR: Failed to install PyInstaller
        pause
        exit /b 1
    )
    echo PyInstaller installed successfully!
    echo.
)

REM Check if pygame is installed
python -c "import pygame" >nul 2>&1
if errorlevel 1 (
    echo Pygame is not installed. Installing now...
    pip install pygame
    if errorlevel 1 (
        echo ERROR: Failed to install Pygame
        pause
        exit /b 1
    )
    echo Pygame installed successfully!
    echo.
)

echo Building executable file...
echo This may take a few minutes...
echo.

REM Build the executable with icon
if exist lizard_icon.ico (
    echo Building with lizard icon...
    pyinstaller --onefile --windowed --name="LizardFollower" --icon=lizard_icon.ico --add-data "lizard_icon.ico;." lizard_follower.py
) else (
    echo Icon not found, building without icon...
    pyinstaller --onefile --windowed --name="LizardFollower" lizard_follower.py
)

if errorlevel 1 (
    echo.
    echo ERROR: Failed to build executable
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo.
echo The executable file is located at:
echo dist\LizardFollower.exe
echo.
echo You can now run LizardFollower.exe without Python installed!
echo.
pause
