import pygame

pygame.init()
window = pygame.display.set_mode(((1500, 750)))
pygame.display.set_caption(("First Game"))

x, y = 50, 50
width, height = 40, 60
vel = 5

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
   
pygame.quit()