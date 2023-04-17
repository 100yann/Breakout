import pygame

BACKGROUND = (255, 250, 250)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Breakout!")
        self.clock = pygame.time.Clock()
        self.player = pygame.image.load('images/minus.png')
        self.playerX = 600
        self.playerY = 500

        self.main()



    def main(self):
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

            self.screen.blit(self.player, (self.playerX, self.playerY))
            pygame.display.update()


    def move_player(self, pos_increment):
        self.playerX += pos_increment