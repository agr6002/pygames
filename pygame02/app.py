import pygame
from model import Model
from view import View
from controller import Controller

class App(object):


    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
        """
        self.controller = Controller()
        self.view = View()
        self.model = Model(pygame)
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        #self.height = width // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()


    def run(self):
        """The mainloop
        """
        self.running = True
        while running:
            self.controller.run(self)
            self.view.run()
            self.model.run(self.screen, self.background)
####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(640, 400).run()