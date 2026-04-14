

import pygame
import random

#
pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CASINO")

#
GREEN = (0, 71, 49)      
GOLD = (255, 215, 0)          
RED = (180, 0, 0)       
BLACK = (20, 20, 20)    
IVORY = (255, 255, 240)       
GRAY = (60, 60, 60) 

#
game_status = "START"   # START, PLAY, WIN, LOSE
number = random.randint(1, 100)
attempt = 1
MAX_ATTEMPTS = 10
user_input = ""
history = []

#
font_title = pygame.font.SysFont("Georgia", 50, True)
font_basic = pygame.font.SysFont("Georgia", 25, True)
font_small = pygame.font.SysFont("Georgia", 16)

#
clock = pygame.time.Clock()
running = True

#
while running: 

    #   
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False
    
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_clicked = True

    #
    screen.fill(GREEN)

    ######
    #
    if game_status == "START":
        
        #
        game_name = font_title.render("LUCKY NUMBER", True, GOLD)
        x_game_name = (WIDTH / 2) - (game_name.get_width() / 2)
        screen.blit(game_name, [x_game_name, 150])

        #
        btn_start = pygame.Rect(150, 300, 200, 60)
        pygame.draw.rect(screen, RED, btn_start, border_radius=10)
        pygame.draw.rect(screen, GOLD, btn_start, 5, border_radius=10)
        
        txt_start = font_basic.render("PLAY", True, IVORY)
        screen.blit(txt_start, [150 + (200 / 2 - txt_start.get_width() / 2), 315])

        #?
        btn_exit = pygame.Rect(150, 380, 200, 60)
        pygame.draw.rect(screen, BLACK, btn_exit, border_radius=10)
        pygame.draw.rect(screen, GOLD, btn_exit, 2, border_radius=10)

        txt_exit = font_basic.render("EXIT GAME", True, IVORY)
        screen.blit(txt_exit, (150 + (200 - txt_exit.get_width()) / 2, 395))

        #
        if mouse_clicked:
            if btn_start.collidepoint(mouse_pos):
                game_status = "PLAY"
                number = random.randint(1, 100)
                attempt = 1
                history = []
                user_input = ""
                hint = "GUESS A NUMBER (1-100)"
                pygame.time.delay(150)
            elif btn_exit.collidepoint(mouse_pos):
                running = False
    
    #
    elif game_status == "PLAY":
        
        #
        pygame.draw.rect(screen, BLACK, (0, 0, 120, HEIGHT))
        pygame.draw.line(screen, GOLD, (120, 0), (120, HEIGHT), 3)
        screen.blit(font_small.render("HISTORY:", True, GOLD), (15, 20))
        for i, h in enumerate(history[-10:]):
            h_txt = font_small.render(f"#{i+1}: {h}", True, IVORY)
            screen.blit(h_txt, (20, 50 + i * 25))
        
        #
        hint_txt = font_basic.render(hint, True, GOLD)
        screen.blit(hint_txt, [140 + ((500 - 140) - hint_txt.get_width()) / 2, 50])

        #
        stat_attempt = font_basic.render(f"Attempts: {attempt}/{MAX_ATTEMPTS}", True, IVORY)
        screen.blit(stat_attempt, (220, 100))

        #
        input_rect = pygame.Rect(210, 160, 160, 60)
        pygame.draw.rect(screen, IVORY, input_rect, border_radius=5)
        pygame.draw.rect(screen, GOLD, input_rect, 5, border_radius=5)
        input_txt = font_title.render(user_input, True, BLACK)
        screen.blit(input_txt, (210 + (160 - input_txt.get_width()) / 2, 165))

        #
        keys_btns = {
            "1": pygame.Rect(160, 250, 80, 50), "2": pygame.Rect(250, 250, 80, 50), "3": pygame.Rect(340, 250, 80, 50),
            "4": pygame.Rect(160, 310, 80, 50), "5": pygame.Rect(250, 310, 80, 50), "6": pygame.Rect(340, 310, 80, 50),
            "7": pygame.Rect(160, 370, 80, 50), "8": pygame.Rect(250, 370, 80, 50), "9": pygame.Rect(340, 370, 80, 50),
            "C": pygame.Rect(160, 430, 80, 50), "0": pygame.Rect(250, 430, 80, 50), "OK": pygame.Rect(340, 430, 80, 50)
        }

        #
        for text, rect in keys_btns.items():
            
            #
            color = BLACK if text in ["C", "OK"] else GRAY
            
            #
            pygame.draw.rect(screen, color, rect, border_radius=10)
            pygame.draw.rect(screen, GOLD, rect, 2, border_radius=10)
            
            #
            txt_btn = font_basic.render(text, True, IVORY)
            screen.blit(txt_btn, (rect.x + (rect.width - txt_btn.get_width()) / 2, rect.y + 12))

            #
            if mouse_clicked and rect.collidepoint(mouse_pos):
                if text == "C":
                    user_input = ""
                elif text == "OK" and user_input:
                    val = int(user_input)
                    
                    history.append(val)
                    
                    if val == number: 
                        game_status = "WIN"
                    elif attempt >= MAX_ATTEMPTS: 
                        game_status = "LOSE"

                    else:
                        attempt += 1 
                        if val < number: 
                            hint = f"{val} IS TOO LOW"
                        else: 
                            hint = f"{val} IS TOO HIGH"

                    user_input = ""

                elif len(user_input) < 3 and text not in ["C", "OK"]:
                    user_input += text
                pygame.time.delay(150)

        #?
        restart_rect = pygame.Rect(250, 490, 80, 50) 
        pygame.draw.rect(screen, RED, restart_rect, border_radius=5)
        pygame.draw.rect(screen, GOLD, restart_rect, 2, border_radius=5)
            
        rest_txt = font_small.render("RESTART", True, IVORY)
        screen.blit(rest_txt, (restart_rect.x + (80 - rest_txt.get_width()) / 2, restart_rect.y + 15))

        #
        if mouse_clicked and restart_rect.collidepoint(mouse_pos):
            game_status = "PLAY"
            number = random.randint(1, 100) 
            attempt = 1                     
            history = []                    
            user_input = ""                 
            hint = "NEW GAME STARTED!"      
            pygame.time.delay(150)            
    
    #
    elif game_status in ["WIN", "LOSE"]:
        msg = "CONGRATS!" if game_status == "WIN" else "GAME OVER"
        msg_color = GOLD if game_status == "WIN" else RED
        
        #
        res_surf = font_title.render(msg, True, msg_color)
        screen.blit(res_surf, (WIDTH / 2 - res_surf.get_width() / 2, 180))
        
        #
        info_surf = font_basic.render(f"Number was: {number}", True, IVORY)
        screen.blit(info_surf, (WIDTH / 2 - info_surf.get_width() / 2, 260))

        #
        back_rect = pygame.Rect(150, 380, 200, 60)
        pygame.draw.rect(screen, RED, back_rect, border_radius=10)
        pygame.draw.rect(screen, GOLD, back_rect, 2, border_radius=10)
        back_txt = font_basic.render("MENU", True, IVORY)
        screen.blit(back_txt, (150 + (200 - back_txt.get_width()) / 2, 395))
        
        #
        if mouse_clicked and back_rect.collidepoint(mouse_pos):
            game_status = "START"
            pygame.time.delay(150)

    ######
    #
    pygame.display.update()
    clock.tick(60)

#
pygame.quit()



