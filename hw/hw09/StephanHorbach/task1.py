import pygame
from random import randint

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Colors - Black & Orange theme
BLACK       = (0,   0,   0)
DARK_BG     = (18,  18,  18)
CARD_BG     = (30,  30,  30)
ORANGE      = (255, 140, 0)
ORANGE_DARK = (200, 100, 0)
ORANGE_GLOW = (255, 180, 50)
WHITE       = (255, 255, 255)
GRAY        = (120, 120, 120)
LIGHT_GRAY  = (180, 180, 180)
GREEN       = (0,   210, 100)
RED         = (220, 50,  50)

# Fonts
font_large  = pygame.font.SysFont("Arial", 34, bold=True)
font_medium = pygame.font.SysFont("Arial", 26)
font_small  = pygame.font.SysFont("Arial", 20)

# Game state
secret_number = randint(1, 100)
max_tries     = 10
tries_left    = max_tries
user_input    = ""
message       = ""
message_color = WHITE
game_over     = False
won           = False

clock = pygame.time.Clock()

def draw_text(text, font, color, x, y, center=True):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.centerx = x
        rect.y = y
    else:
        rect.x = x
        rect.y = y
    screen.blit(surface, rect)

def draw_rounded_rect(surface, color, rect, radius=10, border=0, border_color=None):
    pygame.draw.rect(surface, color, rect, border_radius=radius)
    if border and border_color:
        pygame.draw.rect(surface, border_color, rect, border, border_radius=radius)

# Main game loop
running = True
while running:

    # Background
    screen.fill(DARK_BG)

    # Top orange accent bar
    pygame.draw.rect(screen, ORANGE, (0, 0, WIDTH, 5))

    # Card background
    card = pygame.Rect(40, 20, WIDTH - 80, HEIGHT - 40)
    draw_rounded_rect(screen, CARD_BG, card, radius=14)
    draw_rounded_rect(screen, CARD_BG, card, radius=14,
                      border=2, border_color=ORANGE_DARK)

    # Title with orange accent
    draw_text("NUMBER GUESSING GAME", font_large, ORANGE, WIDTH // 2, 35)

    # Divider line
    pygame.draw.line(screen, ORANGE_DARK, (80, 80), (WIDTH - 80, 80), 1)

    # Instructions
    draw_text("Guess a number between 1 and 100", font_small, LIGHT_GRAY, WIDTH // 2, 90)

    # Tries left
    tries_color = ORANGE if tries_left > 3 else RED
    draw_text(f"Tries left: {tries_left} / {max_tries}", font_medium, tries_color, WIDTH // 2, 118)

    # Progress bar (tries)
    bar_w = 300
    bar_x = (WIDTH - bar_w) // 2
    bar_y = 152
    pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_w, 8), border_radius=4)
    fill_w = int(bar_w * (tries_left / max_tries))
    fill_color = ORANGE if tries_left > 3 else RED
    if fill_w > 0:
        pygame.draw.rect(screen, fill_color, (bar_x, bar_y, fill_w, 8), border_radius=4)

    # Input box
    input_box = pygame.Rect(175, 172, 250, 46)
    draw_rounded_rect(screen, BLACK, input_box, radius=8,
                      border=2, border_color=ORANGE)
    draw_text(user_input if user_input else "Type your guess...",
              font_medium,
              WHITE if user_input else GRAY,
              WIDTH // 2, 180)

    # Enter button
    btn = pygame.Rect(225, 230, 150, 42)
    if not game_over:
        draw_rounded_rect(screen, ORANGE, btn, radius=8)
        draw_rounded_rect(screen, ORANGE, btn, radius=8,
                          border=2, border_color=ORANGE_GLOW)
        draw_text("ENTER", font_medium, BLACK, WIDTH // 2, 238)

    # Feedback message
    if message:
        draw_text(message, font_small, message_color, WIDTH // 2, 285)

    # Bottom divider
    pygame.draw.line(screen, ORANGE_DARK, (80, 308), (WIDTH - 80, 308), 1)

    # Game over messages
    if game_over:
        if won:
            draw_text("Congratulations! You guessed it!", font_medium, GREEN, WIDTH // 2, 318)
        else:
            draw_text(f"Out of tries! The number was {secret_number}.", font_small, RED, WIDTH // 2, 318)
        draw_text("Press R to play again", font_small, ORANGE, WIDTH // 2, 350)

    # Bottom orange accent bar
    pygame.draw.rect(screen, ORANGE, (0, HEIGHT - 5, WIDTH, 5))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                secret_number = randint(1, 100)
                tries_left    = max_tries
                user_input    = ""
                message       = ""
                game_over     = False
                won           = False

            elif not game_over:
                if event.key == pygame.K_RETURN:
                    if user_input.strip().isdigit():
                        guess = int(user_input.strip())
                        tries_left -= 1
                        if guess == secret_number:
                            message       = f"Yes! The number is {secret_number}!"
                            message_color = GREEN
                            game_over     = True
                            won           = True
                        elif tries_left == 0:
                            game_over     = True
                            message       = ""
                        elif guess < secret_number:
                            message       = f"{guess} is too low! Try higher ⬆"
                            message_color = ORANGE_GLOW
                        else:
                            message       = f"{guess} is too high! Try lower ⬇"
                            message_color = ORANGE_GLOW
                        user_input = ""
                    else:
                        message       = "Please enter a valid number!"
                        message_color = RED

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.unicode.isdigit() and len(user_input) < 3:
                    user_input += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if btn.collidepoint(event.pos):
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN,
                                                     key=pygame.K_RETURN,
                                                     unicode="\r",
                                                     mod=0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()