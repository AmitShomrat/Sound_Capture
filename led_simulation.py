import pygame

# Global LED properties (shared state)
left_led_color = (255, 0, 0)  # Default red
right_led_color = (0, 255, 0)  # Default green
left_led_brightness = 20  # Default brightness %
right_led_brightness = 80  # Default brightness %

def update_led_properties(left_color, right_color, left_brightness, right_brightness):
    """
    Update global LED properties for visualization.
    """
    global left_led_color, right_led_color, left_led_brightness, right_led_brightness
    left_led_color = left_color
    right_led_color = right_color
    left_led_brightness = left_brightness
    right_led_brightness = right_brightness


def draw_leds(screen, width, height, background_color):
    """
    Draw LEDs with glow effects on the Pygame screen.
    """
    screen.fill(background_color)

    # Left LED glow and LED
    left_glow_color = tuple(min(int(c * left_led_brightness / 100), 255) for c in left_led_color)
    pygame.draw.circle(screen, left_glow_color, (50, height - 350), 150)
    pygame.draw.circle(screen, left_led_color, (50, height - 350), 50)

    # Right LED glow and LED
    right_glow_color = tuple(min(int(c * right_led_brightness / 100), 255) for c in right_led_color)
    pygame.draw.circle(screen, right_glow_color, (width - 50, height - 350), 150)
    pygame.draw.circle(screen, right_led_color, (width - 50, height - 350), 50)
