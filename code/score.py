# score window - score and the amount of lines we have cleared

from settings import *
from os import path

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING)) # fixing the score window at bottom right position
        self.display_surface = pygame.display.get_surface()
        
        # font
        graphics_dir = path.join(path.dirname(__file__), '..', 'graphics')
        self.font = pygame.font.Font(path.join(graphics_dir, 'Russo_One.ttf'), 30)
        
        # increment
        self.increment_height = self.surface.get_height() / 3
        
    def display_text(self, pos, text):
        text_surface = self.font.render(text, True, 'white')
        text_rext = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface, text_rext)
      
    def run(self):
        
        self.surface.fill(GRAY)
        for i, text in enumerate(['Score', 'Level', 'Lines']):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x,y), text)
        
        self.display_surface.blit (self.surface, self.rect)