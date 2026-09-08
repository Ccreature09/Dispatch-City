import sys
import pygame
from ui.hud import calculate_layout, draw_3_window_layout
from ui.menu import draw_menu, get_button_rects
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, STATE_MENU, STATE_PLAYING, DIFFICULTIES

def main():
    pygame.init()
    win_w, win_h = SCREEN_WIDTH, SCREEN_HEIGHT
    
    screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)
    pygame.display.set_caption("Dispatch City Analysis")

    left_rect, main_rect, right_rect = calculate_layout(win_w, win_h)

    clock = pygame.time.Clock()

    # Game Loop
    running = True
    current_state = STATE_MENU
    selected_difficulty = None  
    while running:
        # 1. Process Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                win_w, win_h = event.w, event.h 
                screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)
                left_rect, main_rect, right_rect = calculate_layout(win_w, win_h)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_state == STATE_MENU:
                    button_rects = get_button_rects(win_w, win_h)

                    for diff_key, rect, in button_rects.items():
                        if rect.collidepoint(event.pos):
                            selected_difficulty = diff_key
                            current_state = STATE_PLAYING

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_state = STATE_MENU


        # 2. Update Game State

        # 3. Render / Draw
        if current_state == STATE_MENU:
            draw_menu(screen, win_w, win_h)
        elif current_state == STATE_PLAYING:
            draw_3_window_layout(screen, left_rect, main_rect, right_rect, 10, 10)


        pygame.display.flip()
        clock.tick(FPS)
    # Clean exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()