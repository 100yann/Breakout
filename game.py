import pygame




class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Breakout!")
        self.clock = pygame.time.Clock()
        self.main()


    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False