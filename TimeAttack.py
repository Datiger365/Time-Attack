import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Attack")

FPS = 60
RUN_SPEED = 7


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# CORRECT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
# INCORRECT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
# RUN_SOUND
# MUSIC

MATH_FONT = pygame.font.SysFont('comicsans', 20)
FONT = pygame.font.SysFont('American Captain', 30)

# PLAYER = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
# PLAYER_SIZED = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)


BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Japanese-Castle-Night.jpg')), (WIDTH*2, HEIGHT*2))

#def welcome_screen():


def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    
    #WIN.blit(YELLOW_SPACESHIP_SIZED, (yellow.x, yellow.y))
    #WIN.blit(RED_SPACESHIP_SIZED, (red.x, red.y))

    red_health_text = MATH_FONT.render("Health: ", 1, WHITE)
    yellow_health_text = MATH_FONT.render("Health: ", 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))


    pygame.display.update()

#def yellow_movement_handler(keys_pressed, yellow):
#    if keys_pressed[pygame.K_a] and yellow.x - VEL > -10: # Left
#        yellow.x -= VEL
#    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width <= BORDER.x + 10: # Right
#        yellow.x += VEL
#    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # Up
#        yellow.y -= VEL
#    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # Down
#        yellow.y += VEL      

#def red_movement_handler(keys_pressed, red):
#    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # Left
#        red.x -= VEL
#   if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 25: # Right
#        red.x += VEL
#    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # Up
#        red.y -= VEL
#    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # Down
#        red.y += VEL  

def draw_winner(text):
    draw_text = FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width()/2, HEIGHT // 2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
    


        keys_pressed = pygame.key.get_pressed()

        draw_window()

    main()

if __name__ == "__main__":
    main()