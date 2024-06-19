# Space Invaders Game
# By: Adrian Adewunmi
# Date: 28/07/2022
# Version: 1.0
# Description: This is the main file for the Space Invaders game.
#             It contains the main game loop and the main game functions.
#             It also contains the main menu and the game over screen.
#             It also contains the high score screen.
#             It also contains the pause screen.
#             It also contains the game over screen.
# Adapted from: https://www.youtube.com/watch?v=FfWpgLFMI7w
#               https://github.com/attreyabhatt/Space-Invaders-Pygame
import random

import pygame
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Changing the Title and Icon of the Game
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Set Background Image
background = pygame.image.load('background.png')

# Set Background Music
mixer.music.load('audio_background.wav')
mixer.music.play(-1)

# Adding Player Image Into The Game
player_img = pygame.image.load('player.png')
# Player Image Position
playerX = 370
playerY = 480
playerX_change = 0

# Adding Enemy Image Into The Game
# enemy_img = pygame.image.load('images/enemy.png')
# Enemy Image Position
# enemyX = random.randint(0, 736)
# enemyY = random.randint(0, 150)
# enemyX_change = random.randint(0, 5)
# enemyY_change = random.randint(0, 50)

# Create enemy list
enemy_img = []
# Enemy Image Position
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# Function to draw the enemies on the screen
for i in range(num_of_enemies):
    # Adding Enemy Image Into The Game
    enemy_img.append(pygame.image.load('enemy.png'))
    # Enemy Image Position
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(random.randint(0, 5))
    enemyY_change.append(random.randint(0, 50))

# Adding Bullet image into the Game
bullet_img = pygame.image.load('bullet.png')
# Bullet Image Position
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready - You can't see the bullet on the screen
bullet_state = 'ready'
# Show Score Variable
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)


# Show Score Function
def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Show Game Over On Screen
def game_over_text():
    over_text = over_font.render('GAME - OVER!', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# Function to draw the player on the screen
def player(x, y):
    screen.blit(player_img, (x, y))


# Function to draw the enemy on the screen
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


# Function to draw the bullet on the screen
def fire_bullet(x, y):
    global bullet_state
    # Fire - The bullet is currently moving
    bullet_state = 'fire'
    screen.blit(bullet_img, (x + 16, y + 10))


# Function to implement collision between the spaceship (bullet) and the enemy
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Logic for running the game
app_running = True

while app_running:
    # Change the background color
    screen.fill((0, 0, 0))
    # Draw the background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        # Player Movement
        # Keyboard Input
        # If the keystroke is pressed down, the player will move left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.5
            # When space is pressed, the bullet will be fired
            if event.key == pygame.K_SPACE:
                # Add sound effect when bullet is fired
                bullet_sound = mixer.Sound('audio_laser.wav')
                bullet_sound.play()
                # If the bullet is ready, fire the bullet
                if bullet_state == 'ready':
                    # After the bullet is fired, it follows its own path, not following the player
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # If the keystroke is released, the player will stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # PlayerX Movement
    playerX += playerX_change
    # Player Boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Enemy Movement
    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()    
            break
        enemyX[i] += enemyX_change[i]
        # Enemy Boundaries
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1.5
            enemyY[i] += enemyY_change[i]
        # Collision Detection
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # Add sound effect when enemy is hit
            explosion_sound = mixer.Sound('audio_explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Shoot multiple bullets
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    # Bullet Movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Draw the player on the screen
    player(playerX, playerY)
    # Draw the score on the screen
    show_score(textX, textY)
    pygame.display.update()