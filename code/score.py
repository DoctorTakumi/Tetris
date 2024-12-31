# score window - score and the amount of lines we have cleared

from settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING)) # fixing the score window at bottom right position
        self.display_surface = pygame.display.get_surface()
        
    def run(self):
        self.display_surface.blit (self.surface, self.rect)