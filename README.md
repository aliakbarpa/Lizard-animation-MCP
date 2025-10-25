# Animated Skeleton Lizard Follower

## Description
A lightweight Python application featuring a skeleton-based 6-legged lizard with articulated spine and joints that smoothly follows your mouse cursor with realistic bone animation and dynamically changing colors. Supports fullscreen mode!

## Features
- 💀 Skeleton-based design with visible bones and joints
- ✨ Smooth mouse-following animation with articulated spine
- 🦎 Longer body with 8 spine segments
- 🦴 Anatomically inspired with ribs, vertebrae, and skull
- 🦵 6 articulated legs with joints (3 pairs)
- 🎨 Dynamically changing rainbow colors
- ⚫ Black background for maximum contrast
- 🖥️ Fullscreen support (F11)
- 🚀 Optimized for minimal resource usage
- 🎮 60 FPS smooth animation

## Requirements
- Python 3.8 or higher
- Pygame library

## Installation

1. Install Python (if not already installed)
2. Install Pygame:
```bash
pip install pygame
```

## Usage

### Method 1: Using Batch File (Easiest)
Double-click `run_lizard.bat`
- Automatically checks for Python and Pygame
- Installs Pygame if missing
- Runs the application

### Method 2: Using Python Directly
Run the application:
```bash
python lizard_follower.py
```

### Method 3: Create Standalone Executable
Double-click `build_executable.bat` to create an .exe file
- Creates a standalone executable in the `dist` folder
- No Python needed to run the .exe
- Takes 2-3 minutes to build

OR use the quick build:
```bash
quick_build.bat
```

### Controls:
- Move your mouse around the window to control the lizard
- Press ESC or close the window to exit

## Technical Details

### Optimization Features:
- Efficient rendering with minimal draw calls
- Simple geometric shapes (circles, ellipses, lines)
- Smooth interpolation for movement
- 60 FPS cap to prevent excessive CPU usage
- No image loading - all procedurally drawn

### Skeleton Lizard Components:
- Triangular skull with eye sockets and jaw
- 8-segment articulated spine (vertebrae)
- Visible rib cage
- 6 jointed legs with upper and lower bones (3 pairs)
- Segmented tail with wave animation
- All bones connected with joint nodes
- Dynamic color cycling through HSV spectrum
- Realistic skeletal movement with follow-through animation

## Performance
- Typical CPU usage: <5%
- Memory usage: ~30-40 MB
- Smooth 60 FPS on most systems

## Controls
- **Mouse Movement**: Control lizard position
- **F11**: Toggle fullscreen mode
- **ESC**: Exit fullscreen OR exit application
- **X Button**: Close window

## License
Free to use and modify

## Author
aliqqqxoox2002x@gmail.com/alpha
