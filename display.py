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
clock =  pygame.time.Clock()

#grab screen dimensions
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

#get_weather()


# Load images
image_paths = [os.path.join("./images", image) for image in os.listdir("./images")]
images = [pygame.image.load(image_path) for image_path in image_paths]
image_index = 0
last_image_change = time.time()
image_display_duration = 15 # seconds

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
    screen.blit(pygame.transform.scale(images[image_index], (screen_width, screen_height)), (0,0))    
    

    #Display time
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    font = pygame.font.Font(None, 36)
    time_surface = font.render(now, True, (255, 255, 255))

    #Calculate time location
    time_loc = time_surface.get_rect()
    time_loc.topleft = (10, 10)

    screen.blit(time_surface, time_loc)

    pygame.display.flip()
    clock.tick(1)


pygame.quit()