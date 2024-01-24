import pygame
pygame.init()
# Setting game window dimensions
window_width = 800
window_height = 600
game_display = pygame.display.set_mode((window_width, window_height))
# Loading the images
bg_image1 = pygame.image.load('bg.png')
bg_image2 = pygame.image.load('front.png')

bg_image1 = pygame.transform.scale(bg_image1, (window_width, window_height))
bg_image2 = pygame.transform.scale(bg_image2, (window_width, window_height))
# Images initial position
x1 = 0
x2 = 0
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Drawing images at positions (x1,0) and (x2,0)
    game_display.blit(bg_image1, (x1, 0))
    game_display.blit(bg_image2, (x2, 0))
    pygame.display.update()
pygame.quit()