@echo off
echo Installing PyInstaller and building executable...
pip install pyinstaller pygame
pyinstaller --onefile --windowed --name="LizardFollower" lizard_follower.py
echo.
echo Done! Executable is in the 'dist' folder
pause
