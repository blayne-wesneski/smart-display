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
    now = datetime.now().strftime("%m/%d/%Y %I:%M %p")
    font = pygame.font.Font("./ChakraPetch-Bold.ttf", 60)
    time_surface = font.render(now, True, (255, 255, 255))
    time_shadow = font.render(now, True, (0, 0, 0))
    time_outline = font.render(now, True, (0, 0, 0))

    #Calculate time location
    time_loc = time_surface.get_rect()
    time_loc.topleft = (10, 10)
    time_shadow_loc = time_shadow.get_rect()
    time_shadow_loc.topleft = (14, 14)

    outline_loc = [(x,y) for x in (-1,0,1) for y in (-1,0,1) if (x,y) != (0,0)]
    for offset in outline_loc:
        screen.blit(time_outline, (time_loc.left + offset[0], time_loc.top + offset[1]))

    screen.blit(time_shadow, time_shadow_loc)
    screen.blit(time_surface, time_loc)

    pygame.display.flip()
    clock.tick(1)


pygame.quit()