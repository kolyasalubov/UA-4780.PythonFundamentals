import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Task 2: Обмеження руху")

rect_width, rect_height = 50, 50
x = WIDTH // 2
y = HEIGHT // 2
speed = 5

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    if x < 0:
        x = 0
    elif x > WIDTH - rect_width:
        x = WIDTH - rect_width

    if y < 0:
        y = 0
    elif y > HEIGHT - rect_height:
        y = HEIGHT - rect_height
    
    # ---------------------------------

    pygame.draw.rect(screen, (0, 255, 0), (x, y, rect_width, rect_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()