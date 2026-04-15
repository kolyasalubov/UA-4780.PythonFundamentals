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

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY),
                                      pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        COORD_X = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT]:
        COORD_X = COORD_X + DELTA_STEP
    if keys[pygame.K_UP]:
        COORD_Y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN]:
        COORD_Y = COORD_Y + DELTA_STEP

    # Restrictions to avoid going beyond the screen.
    # for X axis
    if COORD_X < 0:
        COORD_X = 0
    if COORD_X > WIDTH_DISPLAY - WIDTH_RECTANGLE:
        COORD_X = WIDTH_DISPLAY - WIDTH_RECTANGLE

    # for Y axis
    if COORD_Y < 0:
        COORD_Y = 0
    if COORD_Y > HEIGHT_DISPLAY - HEIGHT_RECTANGLE:
        COORD_Y = HEIGHT_DISPLAY - HEIGHT_RECTANGLE

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)

