import pygame

pygame.init()

# Set up the screen
screen = pygame.display.set_mode([500, 500])
white = (255, 255, 255)
screen.fill(white)

# Define colors
color1 = (255, 100, 70)
color2 = (120, 180, 60)
color3 = (60, 190, 100)
color4 = (170, 100, 255)
color5 = (123, 50, 100)
color6 = (0, 0, 0)

# Circle class
class Circle:
    def __init__(self, color, position, radius, width=0):
        self.color = color
        self.position = position
        self.radius = radius
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.width)

    def grow(self, amount):
        self.radius += amount
        self.draw()

# Initial circle setup
position = (300, 300)
radius = 50
wid = 2
pygame.draw.circle(screen, color3, position, radius, wid)
pygame.display.update()

blueCircle = Circle(color4, position, radius + 60)
redCircle = Circle(color2, position, radius + 40)
yellowCircle = Circle(color1, position, radius, 5)
greenCircle = Circle(color5, position, 20)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            blueCircle.grow(2)
            redCircle.grow(2)
            yellowCircle.grow(2)
            greenCircle.grow(2)
            pygame.display.update()

        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            blackCircle = Circle(color6, pos, 5)
            blackCircle.draw()
            pygame.display.update()

        elif event.type == pygame.QUIT:
            running = False

pygame.quit()
