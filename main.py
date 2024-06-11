import pygame

# Inicializace pygame

pygame.init()


#Vytvoření obrazovky
x = 50
y = 50
width = 1500
height = 750
vel = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Naše první hra")

player = pygame.Rect((300,250,50,50))

# Hlavní herní cyklus
lets_continue = True

while lets_continue:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    pygame.display.update()

    for event in pygame.event.get():
        print(event)
        
        
        if event.type == pygame.QUIT:
            lets_continue = False

#Ukončení hry
pygame.quit()