import pygame

from GameObject import GameObject
from player import player

class Game:
  
    def __init__(self):
        self.width = 800
        self.height = 800
        self.white_colour = (255, 255, 255)
        
        self.game_window = pygame.display.set_mode((self.width, self.height))
        
        # Loading the game assets
        #  using different values and image paths
        self.background = GameObject(0, 0, self.width, self.height, 'image_assets/BACKGROUND_LVL_1.png')
        self.portal = GameObject(350, 40, 60, 60, 'image_assets/portal_end_lvl.png')
        
        self.player = player(360, 700 , 50 , 50, 'image_assets/player.png', 10)
        
        self.clock = pygame.time.Clock()
        
        
    def draw_objects(self):
        self.game_window.fill(self.white_colour)
        
        # showng the images on screen
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.portal.image, (self.portal.x, self.portal.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        

        pygame.display.update()
        
        
    def run_game_loop(self):
        player_direction = 0
        while True:
            # handle events
            events = pygame.event.get()
            for event in events:
                # If there's a QUIT event, break the loop and exit the method
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        #move player up
                        player_direction = -0.5
                    elif event.key == pygame.K_DOWN:
                        #move player down
                        player_direction = 0.5
                elif event.type == pygame.KEYUP:
                    player_direction  = 0 
           
            #execute logic
            self.player.move(player_direction, self.height)
            
            #update display      
            self.draw_objects()
            
            self.clock.tick(60)