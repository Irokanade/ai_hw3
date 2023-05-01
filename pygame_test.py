import pygame  
import os 

class Game:
    def __init__(self):
        # screen dimensions
        screen_width = 640*0.75
        screen_height = 750*0.75
        # flag to know if game menu has been showed
        self.menu_showed = False
        # flag to set game loop
        self.running = True
        # base folder for program resources
        self.resources = "res"
 
        # initialize game window
        pygame.display.init()
        # initialize font for text
        pygame.font.init()

        # create game window
        self.screen = pygame.display.set_mode([screen_width, screen_height])

        # title of window
        window_title = "Chess"
        # set window caption
        pygame.display.set_caption(window_title)

        # get location of game icon
        icon_src = os.path.join(self.resources, "game_icon.png")
        # load game icon
        icon = pygame.image.load(icon_src)
        # set game icon
        pygame.display.set_icon(icon)
        # update display
        pygame.display.flip()
        # set game clock
        self.clock = pygame.time.Clock()

    def startGame(self):
        self.clock.tick(5)

        done = False  
  
        while not done:  
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    done = True  
            pygame.display.flip() 


game = Game()
game.startGame()