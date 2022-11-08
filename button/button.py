import pygame
import sys

# pygame.init()
# screen = pygame.display.set_mode((800, 800))
# pygame.display.set_caption("Button!")
# main_font = pygame.font.SysFont("cambria", 50)


class Button():
    def __init__(self, image, x_pos, y_pos, text_input, main_font):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.main_font = main_font
        self.text_input = text_input
        self.text = self.main_font.render(self.text_input, True, "white")
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.main_font.render(self.text_input, True, "green")
        else:
            self.text = self.main_font.render(self.text_input, True, "white")

# button_surface = pygame.image.load("button.png")
# button_surface = pygame.transform.scale(button_surface, (400, 150))

# button = Button(button_surface, 400, 300, "Button")

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()
# 		if event.type == pygame.MOUSEBUTTONDOWN:
# 			button.checkForInput(pygame.mouse.get_pos())

# 	screen.fill("white")

# 	button.update()
# 	button.changeColor(pygame.mouse.get_pos())

# 	pygame.display.update()
