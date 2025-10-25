"""
Lightweight Animated Skeleton Lizard Follower
A skeleton-based 6-legged lizard that follows mouse cursor with smooth animation
Supports fullscreen mode
"""
import pygame
import math
import colorsys

# Initialize Pygame
pygame.init()

# Get display info for fullscreen
display_info = pygame.display.Info()
FULLSCREEN_WIDTH = display_info.current_w
FULLSCREEN_HEIGHT = display_info.current_h

# Window settings
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Skeleton Lizard Follower - Press F11 for Fullscreen")
clock = pygame.time.Clock()

# Fullscreen state
is_fullscreen = False

def toggle_fullscreen():
    global screen, is_fullscreen, WIDTH, HEIGHT
    is_fullscreen = not is_fullscreen
    if is_fullscreen:
        screen = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.FULLSCREEN)
        WIDTH, HEIGHT = FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT
    else:
        WIDTH, HEIGHT = 1024, 768
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    return screen

# Skeleton Lizard properties
class SkeletonLizard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.speed = 4
        
        # Skeleton proportions (longer lizard)
        self.spine_segments = 8  # Number of spine segments
        self.segment_length = 20
        self.head_size = 25
        self.skull_width = 20
        self.leg_pairs = 3  # 6 legs total
        self.leg_length = 40
        self.leg_joint_length = 25
        self.rib_length = 15
        
        # Spine position history for smooth body movement
        self.spine_positions = [[x, y] for _ in range(self.spine_segments)]
        
        self.hue = 0  # For color cycling
        
    def update(self, target_x, target_y):
        # Smooth following for head
        dx = target_x - self.spine_positions[0][0]
        dy = target_y - self.spine_positions[0][1]
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist > 5:
            self.spine_positions[0][0] += (dx / dist) * self.speed
            self.spine_positions[0][1] += (dy / dist) * self.speed
        
        # Update spine segments to follow head
        for i in range(1, self.spine_segments):
            dx = self.spine_positions[i-1][0] - self.spine_positions[i][0]
            dy = self.spine_positions[i-1][1] - self.spine_positions[i][1]
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist > self.segment_length:
                ratio = (dist - self.segment_length) / dist
                self.spine_positions[i][0] += dx * ratio * 0.5
                self.spine_positions[i][1] += dy * ratio * 0.5
        
        # Update head position
        self.x = self.spine_positions[0][0]
        self.y = self.spine_positions[0][1]
        
        # Update color hue
        self.hue = (self.hue + 0.3) % 360
        
    def get_color(self):
        # Convert HSV to RGB for dynamic color
        rgb = colorsys.hsv_to_rgb(self.hue / 360, 0.9, 1.0)
        return (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
    
    def draw(self, surface):
        color = self.get_color()
        
        # Calculate angle towards target
        dx = pygame.mouse.get_pos()[0] - self.x
        dy = pygame.mouse.get_pos()[1] - self.y
        head_angle = math.atan2(dy, dx)
        
        time = pygame.time.get_ticks() * 0.005
        
        # Draw tail (extension of spine)
        tail_segments = 5
        last_spine_idx = self.spine_segments - 1
        
        if last_spine_idx >= 1:
            # Calculate direction from second-to-last to last spine segment
            dx = self.spine_positions[last_spine_idx][0] - self.spine_positions[last_spine_idx-1][0]
            dy = self.spine_positions[last_spine_idx][1] - self.spine_positions[last_spine_idx-1][1]
            tail_angle = math.atan2(dy, dx)
            
            # Draw tail segments extending from last spine position
            prev_x = self.spine_positions[last_spine_idx][0]
            prev_y = self.spine_positions[last_spine_idx][1]
            
            for i in range(tail_segments):
                # Add slight wave motion to tail
                wave = math.sin(time * 2 - i * 0.5) * 3
                segment_length = 10
                
                # Calculate tail segment position along the spine direction
                tail_x = prev_x + math.cos(tail_angle) * segment_length
                tail_y = prev_y + math.sin(tail_angle) * segment_length + wave
                
                tail_size = max(2, 8 - i)
                
                # Draw connection line
                pygame.draw.line(surface, color, (int(prev_x), int(prev_y)), 
                               (int(tail_x), int(tail_y)), 3)
                pygame.draw.circle(surface, color, (int(tail_x), int(tail_y)), tail_size)
                
                # Update for next segment
                prev_x = tail_x
                prev_y = tail_y
        
        # Draw spine
        for i in range(len(self.spine_positions) - 1):
            start_pos = (int(self.spine_positions[i][0]), int(self.spine_positions[i][1]))
            end_pos = (int(self.spine_positions[i+1][0]), int(self.spine_positions[i+1][1]))
            pygame.draw.line(surface, color, start_pos, end_pos, 4)
            
            # Draw vertebrae nodes
            pygame.draw.circle(surface, color, start_pos, 6)
        
        # Draw last vertebra
        last_pos = (int(self.spine_positions[-1][0]), int(self.spine_positions[-1][1]))
        pygame.draw.circle(surface, color, last_pos, 6)
        
        # Draw ribs along spine
        for i in range(1, self.spine_segments - 1):
            if i % 2 == 0:  # Draw ribs on alternating segments
                spine_x, spine_y = self.spine_positions[i]
                
                # Calculate perpendicular angle to spine
                if i < self.spine_segments - 1:
                    dx = self.spine_positions[i+1][0] - spine_x
                    dy = self.spine_positions[i+1][1] - spine_y
                    spine_angle = math.atan2(dy, dx)
                    
                    # Left rib
                    rib_angle_l = spine_angle + math.pi / 2
                    rib_end_x_l = spine_x + math.cos(rib_angle_l) * self.rib_length
                    rib_end_y_l = spine_y + math.sin(rib_angle_l) * self.rib_length
                    pygame.draw.line(surface, color, (int(spine_x), int(spine_y)), 
                                   (int(rib_end_x_l), int(rib_end_y_l)), 2)
                    
                    # Right rib
                    rib_angle_r = spine_angle - math.pi / 2
                    rib_end_x_r = spine_x + math.cos(rib_angle_r) * self.rib_length
                    rib_end_y_r = spine_y + math.sin(rib_angle_r) * self.rib_length
                    pygame.draw.line(surface, color, (int(spine_x), int(spine_y)), 
                                   (int(rib_end_x_r), int(rib_end_y_r)), 2)
        
        # Draw 6 legs (3 pairs along the body)
        leg_positions = [1, 3, 5]  # Which spine segments to attach legs to
        
        for idx, seg_idx in enumerate(leg_positions):
            if seg_idx < len(self.spine_positions):
                spine_x, spine_y = self.spine_positions[seg_idx]
                
                # Calculate perpendicular angle
                if seg_idx < self.spine_segments - 1:
                    dx = self.spine_positions[seg_idx+1][0] - spine_x
                    dy = self.spine_positions[seg_idx+1][1] - spine_y
                    spine_angle = math.atan2(dy, dx)
                    
                    # Animate legs with walking motion
                    leg_wave = math.sin(time * 3 + idx * 2) * 0.4
                    
                    # Left leg
                    leg_angle_l = spine_angle + math.pi / 2 + leg_wave
                    joint_x_l = spine_x + math.cos(leg_angle_l) * self.leg_length
                    joint_y_l = spine_y + math.sin(leg_angle_l) * self.leg_length
                    
                    # Upper leg bone
                    pygame.draw.line(surface, color, (int(spine_x), int(spine_y)), 
                                   (int(joint_x_l), int(joint_y_l)), 4)
                    pygame.draw.circle(surface, color, (int(joint_x_l), int(joint_y_l)), 5)
                    
                    # Lower leg bone
                    foot_angle_l = leg_angle_l + math.pi / 4 + leg_wave * 0.5
                    foot_x_l = joint_x_l + math.cos(foot_angle_l) * self.leg_joint_length
                    foot_y_l = joint_y_l + math.sin(foot_angle_l) * self.leg_joint_length
                    pygame.draw.line(surface, color, (int(joint_x_l), int(joint_y_l)), 
                                   (int(foot_x_l), int(foot_y_l)), 4)
                    pygame.draw.circle(surface, color, (int(foot_x_l), int(foot_y_l)), 4)
                    
                    # Right leg
                    leg_angle_r = spine_angle - math.pi / 2 - leg_wave
                    joint_x_r = spine_x + math.cos(leg_angle_r) * self.leg_length
                    joint_y_r = spine_y + math.sin(leg_angle_r) * self.leg_length
                    
                    # Upper leg bone
                    pygame.draw.line(surface, color, (int(spine_x), int(spine_y)), 
                                   (int(joint_x_r), int(joint_y_r)), 4)
                    pygame.draw.circle(surface, color, (int(joint_x_r), int(joint_y_r)), 5)
                    
                    # Lower leg bone
                    foot_angle_r = leg_angle_r - math.pi / 4 - leg_wave * 0.5
                    foot_x_r = joint_x_r + math.cos(foot_angle_r) * self.leg_joint_length
                    foot_y_r = joint_y_r + math.sin(foot_angle_r) * self.leg_joint_length
                    pygame.draw.line(surface, color, (int(joint_x_r), int(joint_y_r)), 
                                   (int(foot_x_r), int(foot_y_r)), 4)
                    pygame.draw.circle(surface, color, (int(foot_x_r), int(foot_y_r)), 4)
        
        # Draw skull (head)
        head_x, head_y = self.spine_positions[0]
        
        # Skull outline (triangular for reptilian look)
        skull_points = [
            (head_x + math.cos(head_angle) * self.head_size, 
             head_y + math.sin(head_angle) * self.head_size),  # Front point
            (head_x + math.cos(head_angle + 2.5) * self.skull_width, 
             head_y + math.sin(head_angle + 2.5) * self.skull_width),  # Back left
            (head_x + math.cos(head_angle - 2.5) * self.skull_width, 
             head_y + math.sin(head_angle - 2.5) * self.skull_width),  # Back right
        ]
        pygame.draw.polygon(surface, color, skull_points, 3)
        
        # Eye sockets
        eye_offset = 8
        eye1_x = head_x + math.cos(head_angle + 0.4) * eye_offset
        eye1_y = head_y + math.sin(head_angle + 0.4) * eye_offset
        eye2_x = head_x + math.cos(head_angle - 0.4) * eye_offset
        eye2_y = head_y + math.sin(head_angle - 0.4) * eye_offset
        
        pygame.draw.circle(surface, color, (int(eye1_x), int(eye1_y)), 6, 2)
        pygame.draw.circle(surface, color, (int(eye2_x), int(eye2_y)), 6, 2)
        
        # Eye pupils (dark)
        pygame.draw.circle(surface, (0, 0, 0), (int(eye1_x), int(eye1_y)), 3)
        pygame.draw.circle(surface, (0, 0, 0), (int(eye2_x), int(eye2_y)), 3)
        
        # Jaw line
        jaw_length = self.head_size * 0.8
        jaw_x = head_x + math.cos(head_angle) * jaw_length
        jaw_y = head_y + math.sin(head_angle) * jaw_length
        pygame.draw.line(surface, color, (int(head_x), int(head_y)), 
                        (int(jaw_x), int(jaw_y)), 3)

# Create lizard at center
lizard = SkeletonLizard(WIDTH // 2, HEIGHT // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if is_fullscreen:
                    toggle_fullscreen()
                else:
                    running = False
            elif event.key == pygame.K_F11:
                toggle_fullscreen()
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
    
    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Update lizard
    lizard.update(mouse_x, mouse_y)
    
    # Draw
    screen.fill((0, 0, 0))  # Black background
    lizard.draw(screen)
    
    # Draw instructions
    font = pygame.font.Font(None, 24)
    text = font.render("F11: Fullscreen | ESC: Exit", True, (100, 100, 100))
    screen.blit(text, (10, 10))
    
    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS for smooth animation

pygame.quit()
