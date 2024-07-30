# This script is responsible for displaying all elements

import pygame
import time
from datetime import datetime
from PIL import Image
from weather import get_weather
import os

pygame.init()

# set up screen in fullscreen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Smart Display")
clock = pygame.time.Clock()

# grab screen dimensions
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Load images
image_paths = [os.path.join("./images", image) for image in os.listdir("./images")]
images = [pygame.image.load(image_path) for image_path in image_paths]
image_index = 0
last_image_change = time.time()
image_display_duration = 15  # seconds

weather = get_weather()
last_weather_update = time.time()

# Main Loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Display image slideshow
    if time.time() - last_image_change >= image_display_duration:
        image = images[image_index]
        image_index = (image_index + 1) % len(images)
        last_image_change = time.time()
    screen.blit(
        pygame.transform.scale(images[image_index], (screen_width, screen_height)),
        (0, 0),
    )

    # Display time
    now = datetime.now().strftime("%m/%d/%Y %I:%M %p")
    time_font = pygame.font.Font("./ChakraPetch-Bold.ttf", 60)
    time_surface = time_font.render(now, True, (255, 255, 255))
    time_shadow = time_font.render(now, True, (0, 0, 0))
    time_outline = time_font.render(now, True, (0, 0, 0))

    # Calculate time location
    time_loc = time_surface.get_rect()
    time_loc.topleft = (10, 10)
    time_shadow_loc = time_shadow.get_rect()
    time_shadow_loc.topleft = (14, 14)

    outline_loc = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x, y) != (0, 0)]
    for offset in outline_loc:
        screen.blit(time_outline, (time_loc.left + offset[0], time_loc.top + offset[1]))

    screen.blit(time_shadow, time_shadow_loc)
    screen.blit(time_surface, time_loc)

    # Display weather
    current_time = time.time()
    if current_time - last_weather_update >= 3600:  # 1 hour in seconds
        weather = get_weather()
        last_weather_update = current_time

    temperature = weather["temperature"]
    precipitation_probability = weather["precipitation_probability"]
    cloud_cover = weather["cloud_cover"]

    # Cloud Cover Values
    if cloud_cover <= 10:
        cloud_cover_text = "Sunny"
    elif cloud_cover <= 30:
        cloud_cover_text = "Partly Sunny"
    elif cloud_cover <= 60:
        cloud_cover_text = "Partly Cloudy"
    else:
        cloud_cover_text = "Cloudy"

    weather_font = pygame.font.Font("./ChakraPetch-Bold.ttf", 36)

    # declare weather surfaces

    temperature_surface = weather_font.render(f"{temperature}F", True, (255, 255, 255))
    temperature_shadow = weather_font.render(f"{temperature}F", True, (0, 0, 0))
    temperature_outline = weather_font.render(f"{temperature}F", True, (0, 0, 0))

    cloud_cover_surface = weather_font.render(cloud_cover_text, True, (255, 255, 255))
    cloud_cover_shadow = weather_font.render(cloud_cover_text, True, (0, 0, 0))
    cloud_cover_outline = weather_font.render(cloud_cover_text, True, (0, 0, 0))

    precipitation_surface = weather_font.render(
        f"{precipitation_probability}%", True, (255, 255, 255)
    )
    precipitation_shadow = weather_font.render(
        f"{precipitation_probability}%", True, (0, 0, 0)
    )
    precipitation_outline = weather_font.render(
        f"{precipitation_probability}%", True, (0, 0, 0)
    )

    # Calculate weather location

    temperature_loc = temperature_surface.get_rect()
    temperature_loc.topright = (screen_width - 10 , 10)
    temperature_shadow_loc = temperature_shadow.get_rect()
    temperature_shadow_loc.topright = (screen_width - 6, 14)

    for offset in outline_loc:
        screen.blit(temperature_outline, (temperature_loc.left + offset[0], temperature_loc.top + offset[1]))

    cloud_cover_loc = cloud_cover_surface.get_rect()
    cloud_cover_loc.topright = (screen_width - 10, 50)
    cloud_cover_shadow_loc = cloud_cover_shadow.get_rect()
    cloud_cover_shadow_loc.topright = (screen_width - 6, 54)

    for offset in outline_loc:
        screen.blit(cloud_cover_outline, (cloud_cover_loc.left + offset[0], cloud_cover_loc.top + offset[1]))
    
    precipitation_loc = precipitation_surface.get_rect()
    precipitation_loc.topright = (screen_width - 10, 90)
    precipitation_shadow_loc = precipitation_shadow.get_rect()
    precipitation_shadow_loc.topright = (screen_width - 6, 94)

    for offset in outline_loc:
        screen.blit(precipitation_outline, (precipitation_loc.left + offset[0], precipitation_loc.top + offset[1]))

    screen.blit(temperature_shadow, temperature_shadow_loc)
    screen.blit(temperature_surface, temperature_loc)

    screen.blit(cloud_cover_shadow, cloud_cover_shadow_loc)
    screen.blit(cloud_cover_surface, cloud_cover_loc)

    screen.blit(precipitation_shadow, precipitation_shadow_loc)
    screen.blit(precipitation_surface, precipitation_loc)
    

    # Display
    pygame.display.flip()
    clock.tick(1)


pygame.quit()
