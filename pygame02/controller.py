import pygame
class Controller():
    def __init__():
        return
    def run(app):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    app.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        app.running = False
 