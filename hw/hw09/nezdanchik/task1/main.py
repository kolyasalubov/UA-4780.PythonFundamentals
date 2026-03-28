import random

import pygame


WINDOW_WIDTH = 720
WINDOW_HEIGHT = 420
MAX_ATTEMPTS = 10
MIN_NUMBER = 1
MAX_NUMBER = 100

BG_COLOR = (245, 247, 250)
TEXT_COLOR = (34, 40, 49)
ACCENT_COLOR = (48, 121, 237)
SUCCESS_COLOR = (40, 167, 69)
ERROR_COLOR = (220, 53, 69)
INPUT_BG = (255, 255, 255)
INPUT_BORDER_ACTIVE = (48, 121, 237)
INPUT_BORDER_IDLE = (180, 188, 199)


def reset_game() -> dict[str, object]:
    return {
        "secret_number": random.randint(MIN_NUMBER, MAX_NUMBER),
        "attempts_used": 0,
        "input_text": "",
        "message": f"Guess a number from {MIN_NUMBER} to {MAX_NUMBER}",
        "message_color": TEXT_COLOR,
        "game_over": False,
        "won": False,
    }


def process_guess(state: dict[str, object]) -> None:
    if state["game_over"]:
        return

    input_text = str(state["input_text"]).strip()
    if not input_text:
        state["message"] = "Enter a number before pressing Enter"
        state["message_color"] = ERROR_COLOR
        return

    if not input_text.isdigit():
        state["message"] = "Only positive integers are allowed"
        state["message_color"] = ERROR_COLOR
        state["input_text"] = ""
        return

    guess = int(input_text)
    if not MIN_NUMBER <= guess <= MAX_NUMBER:
        state["message"] = f"Number must be between {MIN_NUMBER} and {MAX_NUMBER}"
        state["message_color"] = ERROR_COLOR
        state["input_text"] = ""
        return

    state["attempts_used"] = int(state["attempts_used"]) + 1
    secret_number = int(state["secret_number"])

    if guess == secret_number:
        state["message"] = (
            f"Correct! You guessed {secret_number} in {state['attempts_used']} tries."
        )
        state["message_color"] = SUCCESS_COLOR
        state["game_over"] = True
        state["won"] = True
    elif int(state["attempts_used"]) >= MAX_ATTEMPTS:
        state["message"] = (
            f"You lost. The number was {secret_number}. Press R to restart."
        )
        state["message_color"] = ERROR_COLOR
        state["game_over"] = True
    elif guess < secret_number:
        left = MAX_ATTEMPTS - int(state["attempts_used"])
        state["message"] = f"My number is greater. Attempts left: {left}"
        state["message_color"] = ACCENT_COLOR
    else:
        left = MAX_ATTEMPTS - int(state["attempts_used"])
        state["message"] = f"My number is smaller. Attempts left: {left}"
        state["message_color"] = ACCENT_COLOR

    state["input_text"] = ""


def draw_text(
    surface: pygame.Surface,
    text: str,
    font: pygame.font.Font,
    color: tuple[int, int, int],
    x: int,
    y: int,
) -> None:
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Guess the Number")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("arial", 34, bold=True)
    body_font = pygame.font.SysFont("arial", 24)
    small_font = pygame.font.SysFont("arial", 18)

    input_rect = pygame.Rect(40, 210, 220, 50)
    state = reset_game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and bool(state["game_over"]):
                    state = reset_game()
                elif event.key == pygame.K_RETURN:
                    process_guess(state)
                elif event.key == pygame.K_BACKSPACE:
                    state["input_text"] = str(state["input_text"])[:-1]
                elif not bool(state["game_over"]):
                    if event.unicode.isdigit() and len(str(state["input_text"])) < 3:
                        state["input_text"] = f"{state['input_text']}{event.unicode}"

        screen.fill(BG_COLOR)

        pygame.draw.rect(screen, INPUT_BG, input_rect, border_radius=12)
        pygame.draw.rect(
            screen,
            INPUT_BORDER_IDLE if bool(state["game_over"]) else INPUT_BORDER_ACTIVE,
            input_rect,
            width=2,
            border_radius=12,
        )

        draw_text(screen, "Guess the Number", title_font, TEXT_COLOR, 40, 35)
        draw_text(
            screen,
            f"Find a number from {MIN_NUMBER} to {MAX_NUMBER} in {MAX_ATTEMPTS} attempts.",
            body_font,
            TEXT_COLOR,
            40,
            95,
        )
        draw_text(
            screen,
            f"Attempts used: {state['attempts_used']} / {MAX_ATTEMPTS}",
            body_font,
            TEXT_COLOR,
            40,
            145,
        )
        draw_text(screen, str(state["input_text"]) or "_", body_font, TEXT_COLOR, 55, 222)
        draw_text(
            screen,
            str(state["message"]),
            body_font,
            tuple(state["message_color"]),
            40,
            290,
        )
        draw_text(
            screen,
            "Type digits, press Enter to submit, press R to start a new game.",
            small_font,
            TEXT_COLOR,
            40,
            355,
        )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
