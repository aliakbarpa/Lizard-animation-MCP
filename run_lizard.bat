@echo off
echo ========================================
echo    Skeleton Lizard Follower
echo ========================================
echo.
echo Starting the lizard animation...
echo Press ESC to exit the application
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
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

REM Run the application
python lizard_follower.py

if errorlevel 1 (
    echo.
    echo Application closed with an error.
    pause
)
