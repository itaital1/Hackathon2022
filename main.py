import pygame

from car import Car
from car import Vector

pygame.init()

pygame.display.set_caption('Rush Hour')

clock = pygame.time.Clock()

img_path = 'images/red_car.png'
car = Car(pygame.image.load(img_path), Vector(0.0, 0.0), 0.0, 4)
car.accelerate(Vector(1, 2))

screen = pygame.display.set_mode((800, 600))

running = True
while running:

    screen.fill((0, 0, 0))
    car.rotate(left=True)
    car.move()
    car.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draws the surface object to the screen.
    pygame.display.update()

    clock.tick(40)
