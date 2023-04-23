import pygame
import random

BACKGROUND = (255, 250, 250)
BLACK = (0, 0, 0)
COLORS = ['red', 'orange', 'yellow', 'green']
options = [-0.5, 0.5]
blocks = []
block_width = int(1280/14)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Breakout!")
        self.clock = pygame.time.Clock()
        self.player = pygame.image.load('images/minus.png')
        self.playerX, self.playerY = 600, 550
        self.ball = pygame.image.load('images/ball.png')
        self.ballX, self.ballY = random.randint(400,900), 600
        self.velX = random.choice(options)
        self.velY = -0.5
        self.bounds = self.screen.get_rect()
        self.main()



    def main(self):
        running = True
        for index, color in enumerate(COLORS):
            self.create_blocks(index*50+200) # Create 4 different lines of blocks

        print(len(blocks[42:]), blocks[42:])
        while running:
            self.screen.fill(BACKGROUND)
            self.draw_blocks()


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
            self.detect_block_collision()
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
            print('game over')
            pygame.quit()
    
    def check_collision(self):
        self.player_rect = pygame.Rect(self.playerX, 675, 260, 50)
        self.ball_rect = self.ball.get_rect()
        self.ball_rect.topleft = (self.ballX, self.ballY)
        collision = self.player_rect.colliderect(self.ball_rect)
        if collision:
            # self.velX *= -1
            self.velY *= -1

    def create_blocks(self, y):
        for x in range(14):
            rect = pygame.Rect(x*block_width, y, block_width, 50)
            blocks.append(rect)

    def draw_blocks(self):
        for index, rect in enumerate(blocks):
            if rect == '-':
                pass
            else:
                if index > len(blocks) - 15:
                    color = COLORS[3]
                elif index > len(blocks) - 29:
                    color = COLORS[2]
                elif index > len(blocks) - 43:
                    color = COLORS[1]
                else:
                    color = COLORS[0]
                pygame.draw.rect(self.screen, color, rect)
                for i in range(4):
                    pygame.draw.rect(self.screen, (0,0,0), (blocks[index][0]-i, blocks[index][1] - i, block_width, 50), 1)
        
    def detect_block_collision(self):
        for index, rect in enumerate(blocks):
            if rect == '-':
                pass
            else:
                collide = pygame.Rect.colliderect(self.ball_rect, rect)
                if collide:
                    self.velY *= -1
                    blocks[index] = '-'
                    self.increase_speed(self.velY)
                    break

    def increase_speed(self, Y):
        if Y > 0:
            if "-" in blocks[:14]:
                self.velY = 1
                self.velX = 1
            elif "-" in blocks[14:28]:
                self.velY = 0.85
                self.velX = 0.85
            elif "-" in blocks[28:42]:
                self.velY = 0.75
                self.velX = 0.75
            elif "-" in blocks[42:]:
                self.velY = 0.65
                self.velX = 0.65
        else:
            if "-" in blocks[:14]:
                self.velY = -1
                self.velX = -1
            elif "-" in blocks[14:28]:
                self.velY = -0.85
                self.velX = -0.85
            elif "-" in blocks[28:42]:
                self.velY = -0.75
                self.velX = -0.75
            elif "-" in blocks[42:]:
                self.velY = -0.65
                self.velX = -0.65
        

            
            


