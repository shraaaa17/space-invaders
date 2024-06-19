import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 600, 600
PLAYER_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 7
SCORE_FILE = "score.txt"

class Player:
    def _init_(self):
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 10)

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        elif direction == "right" and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

class Enemy:
    def _init_(self):
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
 
 
 #To store the score in MySQL, you'll need to use a MySQL database and Python's MySQL connector library. Here's how you can modify the code to store and retrieve the score from a MySQL database:

#First, make sure you have MySQL installed and running, and create a database and a table to store the score. For example:

#sql
'''
Copy code
CREATE DATABASE space_invaders;
USE space_invaders;
CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    score INT
);
Then, you can modify the Python code as follows:

python
Copy code
'''
 
import pygame
import random
import sys
import

# Constants
WIDTH, HEIGHT = 600, 600
PLAYER_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 7

class Player:
    def _init_(self):
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 10)

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        elif direction == "right" and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

class Enemy:
    def _init_(self):
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)

    def move(self):
        self.rect.y += ENEMY_SPEED

class Bullet:
    def _init_(self, player_rect):
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = player_rect.midtop

    def move(self):
        self.rect.y -= BULLET_SPEED

class Game:
    def _init_(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemies = []
        self.bullet = None
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="space_invaders"
        )

    def spawn_enemy(self):
        enemy = Enemy()
        self.enemies.append(enemy)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("left")
        if keys[pygame.K_RIGHT]:
            self.player.move("right")
        if keys[pygame.K_SPACE] and not self.bullet:
            self.bullet = Bullet(self.player.rect)

    def update_game_state(self):
        if self.bullet:
            self.bullet.move()
            if self.bullet.rect.bottom <= 0:
                self.bullet = None

        for enemy in self.enemies:
            enemy.move()
            if enemy.rect.top > HEIGHT:
                self.enemies.remove(enemy)

        if self.bullet:
            for enemy in self.enemies:
                if self.bullet.rect.colliderect(enemy.rect):
                    self.score += 10
                    self.enemies.remove(enemy)
                    self.bullet = None

        if any(enemy.rect.colliderect(self.player.rect) for enemy in self.enemies):
            return True

        return False

    def draw_elements(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player.image, self.player.rect)
        for enemy in self.enemies:
            self.screen.blit(enemy.image, enemy.rect)
        if self.bullet:
            self.screen.blit(self.bullet.image, self.bullet.rect)
        text_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text_surface, (WIDTH // 2 - 70, 10))
        pygame.display.flip()

    def save_score(self):
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO scores (score) VALUES (%s)"
        val = (self.score,)
        cursor.execute(sql, val)
        self.db_connection.commit()
        cursor.close()

    def load_score(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM scores ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
            self.score = result[1]
        else:
            self.score = 0
        cursor.close()

    def run(self):
        self.load_score()
        running = True
        enemy_spawn_delay = 1000
        last_enemy_spawn_time = pygame.time.get_ticks()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            current_time = pygame.time.get_ticks()
            if current_time - last_enemy_spawn_time > enemy_spawn_delay:
                self.spawn_enemy()
                last_enemy_spawn_time = current_time

            self.handle_input()
            if self.update_game_state():
                self.save_score()
                running = False
            self.draw_elements()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if _name_ == "_main_":
    game = Game()
    game.run()
#This code establishes a connection to the MySQL database, saves the score to the database when the game ends, and loads the score from the database when the game starts. Replace "yourusername" and "yourpassword" with your MySQL username and password, respectively
