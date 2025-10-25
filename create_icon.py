"""
Create a simple lizard icon for the application
"""
from PIL import Image, ImageDraw

# Create a 256x256 image with transparent background
size = 256
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Define lizard color (green)
lizard_color = (50, 200, 50, 255)
outline_color = (30, 120, 30, 255)

# Draw lizard body (ellipse)
body_bounds = [60, 100, 196, 160]
draw.ellipse(body_bounds, fill=lizard_color, outline=outline_color, width=3)

# Draw head (circle)
head_x, head_y = 200, 130
head_radius = 30
draw.ellipse([head_x-head_radius, head_y-head_radius, 
              head_x+head_radius, head_y+head_radius], 
             fill=lizard_color, outline=outline_color, width=3)

# Draw eyes
eye1_pos = (head_x - 10, head_y - 8)
eye2_pos = (head_x - 10, head_y + 8)
eye_radius = 5
draw.ellipse([eye1_pos[0]-eye_radius, eye1_pos[1]-eye_radius,
              eye1_pos[0]+eye_radius, eye1_pos[1]+eye_radius],
             fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=2)
draw.ellipse([eye2_pos[0]-eye_radius, eye2_pos[1]-eye_radius,
              eye2_pos[0]+eye_radius, eye2_pos[1]+eye_radius],
             fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=2)

# Draw pupils
pupil_radius = 2
draw.ellipse([eye1_pos[0]-pupil_radius, eye1_pos[1]-pupil_radius,
              eye1_pos[0]+pupil_radius, eye1_pos[1]+pupil_radius],
             fill=(0, 0, 0, 255))
draw.ellipse([eye2_pos[0]-pupil_radius, eye2_pos[1]-pupil_radius,
              eye2_pos[0]+pupil_radius, eye2_pos[1]+pupil_radius],
             fill=(0, 0, 0, 255))

# Draw legs (6 legs - 3 on each side)
leg_width = 8
leg_positions = [
    (80, 140), (120, 140), (160, 140),  # Top legs
    (80, 120), (120, 120), (160, 120)   # Bottom legs
]

for i, (x, y) in enumerate(leg_positions):
    if i < 3:  # Top legs
        draw.line([(x, y), (x-15, y+30)], fill=lizard_color, width=leg_width)
        draw.ellipse([x-leg_width, y+30-leg_width, x+leg_width, y+30+leg_width], 
                     fill=lizard_color, outline=outline_color, width=2)
    else:  # Bottom legs
        draw.line([(x, y), (x-15, y-30)], fill=lizard_color, width=leg_width)
        draw.ellipse([x-leg_width, y-30-leg_width, x+leg_width, y-30+leg_width], 
                     fill=lizard_color, outline=outline_color, width=2)

# Draw tail
tail_points = [
    (60, 130),
    (40, 130),
    (20, 125),
    (10, 120),
    (5, 110)
]
for i in range(len(tail_points) - 1):
    width = 10 - i * 2
    draw.line([tail_points[i], tail_points[i+1]], fill=lizard_color, width=max(width, 2))

# Draw tail tip
draw.ellipse([tail_points[-1][0]-3, tail_points[-1][1]-3,
              tail_points[-1][0]+3, tail_points[-1][1]+3],
             fill=lizard_color, outline=outline_color, width=2)

# Save as ICO file with multiple sizes
img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
img_48 = img.resize((48, 48), Image.Resampling.LANCZOS)
img_64 = img.resize((64, 64), Image.Resampling.LANCZOS)
img_128 = img.resize((128, 128), Image.Resampling.LANCZOS)

# Save as .ico with multiple sizes
img.save('lizard_icon.ico', format='ICO', sizes=[(32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

print("Icon created successfully: lizard_icon.ico")
