import sys
import pygame
from ui.hud import calculate_layout, draw_3_window_layout
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()

    # Track active window dimensions locally
    win_w, win_h = SCREEN_WIDTH, SCREEN_HEIGHT
    
    screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)
    pygame.display.set_caption("Dispatch City Analysis")

    left_rect, main_rect, right_rect = calculate_layout(win_w, win_h)

    clock = pygame.time.Clock()

    # Game Loop
    running = True
    while running:
        # 1. Process Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                win_w, win_h = event.w, event.h
                screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)
                left_rect, main_rect, right_rect = calculate_layout(win_w, win_h)

        # 2. Update Game State

        # 3. Render / Draw
        draw_3_window_layout(screen, left_rect, main_rect, right_rect)
        pygame.display.flip()
        clock.tick(FPS)

    # Clean exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()