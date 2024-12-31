from settings import *
from sys import exit

# components
from game import Game # from game.py importing Game class
from score import Score # from score.py importing Score class
from preview import Preview # from preview.py importing Preview class

class Main:
    def __init__(self):
        
        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")
        
        # components - classes from modules (different components)
        self.game = Game()
        self.score = Score()
        self.preview = Preview()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            # display
            self.display_surface.fill(GRAY)
            
            # components
            self.game.run()
            self.score.run()
            self.preview.run()
            
            # updating the game
            pygame.display.update()
            self.clock.tick()
        
if __name__ == '__main__':
    main = Main()
    main.run()