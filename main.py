import sys
import pygame
from ui.hud import calculate_layout, draw_3_window_layout, screen_to_grid, get_toolbar_button_rects, get_grid_dimensions
from ui.menu import draw_menu, get_button_rects
from entities.building import Building
from entities.building_data import BUILDING_TYPES
from assets import load_assets
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, STATE_MENU, STATE_PLAYING, DIFFICULTIES
from typing import Optional

def main():
    pygame.init()
    win_w, win_h = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)
    pygame.display.set_caption("Dispatch City Analysis")

    left_rect, main_rect, right_rect = calculate_layout(win_w, win_h)
    cell_size, _, _ = get_grid_dimensions(main_rect, 10, 10)
    load_assets(cell_size)
    clock = pygame.time.Clock()
    running = True
    current_state = STATE_MENU
    selected_difficulty = None  
    hovered_cell = None
    active_tool: Optional[str] = list(BUILDING_TYPES.keys())[0] # Sets default tool by converting dict to list and taking first element
    placed_buildings: dict[tuple[int,int], Building] = {}


    # Game Loop
    while running: 
        # 1. Process Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE: # Window resize
                win_w, win_h = event.w, event.h 
                screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)
                left_rect, main_rect, right_rect = calculate_layout(win_w, win_h)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left click
                if current_state == STATE_MENU: # Switches from Menu to Game
                    button_rects = get_button_rects(win_w, win_h)

                    for diff_key, rect, in button_rects.items():
                        if rect.collidepoint(event.pos):
                            selected_difficulty = diff_key
                            current_state = STATE_PLAYING

                elif current_state == STATE_PLAYING:
                    if left_rect.collidepoint(event.pos): # Sets active tool from left toolbar
                        rel_pos = (event.pos[0] - left_rect.x, event.pos[1] - left_rect.y)
                        tool_buttons = get_toolbar_button_rects(left_rect)
                        for b_key, btn_rect in tool_buttons.items():
                            if btn_rect.collidepoint(rel_pos):
                                active_tool = b_key

                    elif hovered_cell is not None and active_tool is not None: # places building onto grid
                        col, row = hovered_cell
                        cell_size, _, _ = get_grid_dimensions(main_rect, 10, 10)
                        placed_buildings[(col, row)] = Building(col, row, active_tool, cell_size)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Escape
                    current_state = STATE_MENU

        # 2. Update Game State
        if current_state == STATE_PLAYING:
            mouse_pos = pygame.mouse.get_pos()
            hovered_cell = screen_to_grid(mouse_pos, main_rect, 10, 10)
        else:
            hovered_cell = None

        # 3. Render / Draw
        if current_state == STATE_MENU:
            draw_menu(screen, win_w, win_h)
        elif current_state == STATE_PLAYING:
            draw_3_window_layout(screen, left_rect, main_rect, right_rect, 10, 10, hovered_cell, active_tool, placed_buildings)

        pygame.display.flip()
        clock.tick(FPS)
    # Clean exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()