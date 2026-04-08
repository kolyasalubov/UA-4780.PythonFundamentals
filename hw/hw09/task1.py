import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Вгадай число (1-100)")
font = pygame.font.SysFont("Arial", 32)
small_font = pygame.font.SysFont("Arial", 24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

secret_number = random.randint(1, 100)
attempts = 10
user_text = ""
message = "Введіть число та натисніть Enter"
game_over = False

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:
                if user_text:
                    guess = int(user_text)
                    attempts -= 1
                    
                    if guess == secret_number:
                        message = f"Вітаю! Ти вгадав: {secret_number}!"
                        game_over = True
                    elif attempts == 0:
                        message = f"Програш! Число було: {secret_number}"
                        game_over = True
                    elif guess < secret_number:
                        message = "Більше!"
                    else:
                        message = "Менше!"
                    
                    user_text = "" 
            
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                if event.unicode.isdigit() and len(user_text) < 3:
                    user_text += event.unicode


    msg_surface = font.render(message, True, BLACK)
    screen.blit(msg_surface, (50, 100))

    # Виводимо те, що вводить користувач
    input_label = font.render("Ваше число: " + user_text, True, RED)
    screen.blit(input_label, (50, 200))

    attempts_label = small_font.render(f"Залишилося спроб: {attempts}", True, BLACK)
    screen.blit(attempts_label, (50, 300))

    if game_over:
        restart_msg = small_font.render("Закрийте вікно, щоб вийти", True, BLACK)
        screen.blit(restart_msg, (50, 400))

    pygame.display.flip() 

pygame.quit()