@echo off
echo Installing dependencies and building executable...
pip install pyinstaller pygame Pillow

REM Create icon if it doesn't exist
if not exist lizard_icon.ico (
    echo Creating lizard icon...
    python create_icon.py
)

REM Build with icon
if exist lizard_icon.ico (
    pyinstaller --onefile --windowed --name="LizardFollower" --icon=lizard_icon.ico --add-data "lizard_icon.ico;." lizard_follower.py
) else (
    pyinstaller --onefile --windowed --name="LizardFollower" lizard_follower.py
)
echo.
echo Done! Executable is in the 'dist' folder
pause
