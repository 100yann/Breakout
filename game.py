import pygame
import random

BACKGROUND = (255, 250, 250)
BLACK = (0, 0, 0)
options = [0.5, -0.5]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Breakout!")
        self.clock = pygame.time.Clock()
        self.player = pygame.image.load('images/minus.png')
        self.playerX, self.playerY = 600, 550
        self.ball = pygame.image.load('images/ball.png')
        self.ballX, self.ballY = random.randint(400,700), 200
        self.velX = random.choice(options)
        self.velY = -0.5
        self.bounds = self.screen.get_rect()
        self.main()



    def main(self):
        print(self.bounds.bottom)
        running = True
        while running:
            self.screen.fill(BACKGROUND)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                                  
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.move_player(-1)
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.move_player(1)

            self.screen.blit(self.ball, (self.ballX, self.ballY))
            self.screen.blit(self.player, (self.playerX, self.playerY))

            self.move_ball()
            self.check_collision()
            pygame.display.update()


    def move_player(self, pos_increment):
        self.playerX += pos_increment

    def move_ball(self):
        self.ballX -= self.velX
        self.ballY += self.velY
        if self.ballX < self.bounds.left or self.ballX > self.bounds.right:
            self.velX *= -1
        if self.ballY < self.bounds.top:
            self.velY *= -1
        if self.ballY > 720:
            self.velX = 0
            self.velY = 0
    
    def check_collision(self):
        self.player_rect = pygame.Rect(self.playerX, 675, 260, 50)
        self.ball_rect = self.ball.get_rect()
        self.ball_rect.topleft = (self.ballX, self.ballY)
        collision = self.player_rect.colliderect(self.ball_rect)
        if collision:
            self.velX *= -1
            self.velY *= -1

            
        

            
            


