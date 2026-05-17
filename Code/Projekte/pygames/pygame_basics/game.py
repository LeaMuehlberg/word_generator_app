import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
running = True
dt = 0
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    pygame.draw.circle(screen, "yellow", position, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        position.y -= 300 * dt
    if keys[pygame.K_s]:
        position.y += 300 * dt
    if keys[pygame.K_d]:
        position.x += 300 * dt
    if keys[pygame.K_a]:
        position.x -= 300 * dt
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()