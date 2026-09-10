import pygame
from typing import Optional
from entities.building_data import BUILDING_TYPES

def calculate_layout(win_w: int, win_h: int):
    left_w = int(win_w * 0.20)
    right_w = int(win_w * 0.25)
    main_w = win_w - left_w - right_w

    left_rect = pygame.Rect(0, 0, left_w, win_h)
    main_rect = pygame.Rect(left_w, 0, main_w, win_h)
    right_rect = pygame.Rect(left_w + main_w, 0, right_w, win_h)

    return left_rect, main_rect, right_rect

def draw_3_window_layout(screen: pygame.Surface, left_rect: pygame.Rect, main_rect: pygame.Rect, right_rect: pygame.Rect, rows, cols, hovered_cell: Optional[tuple[int,int]] = None, active_tool: Optional[str] = None, placed_buildings: Optional[dict] = None):

    left_panel = screen.subsurface(left_rect)
    main_panel = screen.subsurface(main_rect)
    right_panel = screen.subsurface(right_rect)

    left_panel.fill((30, 32, 40))
    main_panel.fill((250, 250, 250))   
    right_panel.fill((40, 32, 35))

    cell_size, offset_x, offset_y = get_grid_dimensions(main_rect, rows, cols)

    for r in range(rows):
        for c in range(cols):
            cell_rect = pygame.Rect(offset_x + c * cell_size, offset_y + r * cell_size, cell_size, cell_size)

            if hovered_cell == (c, r):
                pygame.draw.rect(main_panel, (90, 110, 140), cell_rect)
                pygame.draw.rect(main_panel, (140, 180, 240), cell_rect, 2)
            else:
                pygame.draw.rect(main_panel, (60, 60, 75), cell_rect, 1)

    if placed_buildings: # Dynamic resizing of building bounding box 
        for (c, r), b_entity in placed_buildings.items():
            b_entity.rect = pygame.Rect(offset_x + c * cell_size, offset_y + r * cell_size, cell_size, cell_size) 
            b_entity.draw(main_panel)

    draw_building_toolbar(left_panel, active_tool)

    pygame.draw.line(screen, (70, 70, 80), (left_rect.right, 0), (left_rect.right, screen.get_height()), 2)
    pygame.draw.line(screen, (70, 70, 80), (main_rect.right, 0), (main_rect.right, screen.get_height()), 2)

def get_grid_dimensions(main_rect: pygame.Rect, rows:int, cols: int):

    cell_size = min(main_rect.width // cols, main_rect.height // rows)
    grid_w = cell_size * cols
    grid_h = cell_size * rows

    offset_x = (main_rect.width - grid_w) // 2
    offset_y = (main_rect.height - grid_h) // 2

    return cell_size, offset_x, offset_y

def screen_to_grid(mouse_pos: tuple[int,int], main_rect: pygame.Rect, rows: int, cols: int):

    mx, my = mouse_pos
    cell_size, offset_x, offset_y = get_grid_dimensions(main_rect, rows, cols)

    grid_start_x = main_rect.x + offset_x
    grid_start_y = main_rect.y + offset_y

    rel_x = mx - grid_start_x
    rel_y = my - grid_start_y

    col = rel_x // cell_size
    row = rel_y // cell_size

    # Boundry check
    if 0 <= col < cols and 0 <= row < rows:
        return col, row

    return None

def get_toolbar_button_rects(left_rect: pygame.Rect) -> dict[str, pygame.Rect]:

    padding = 10
    btn_h = 40
    start_y = 50
    panel_w = left_rect.width

    tool_buttons = {}
    for idx, b_key in enumerate(BUILDING_TYPES.keys()):
        tool_buttons[b_key] = pygame.Rect(padding, start_y + idx * (btn_h + padding), panel_w - (padding * 2), btn_h)
    return tool_buttons

def draw_building_toolbar(left_panel: pygame.Surface, active_tool: Optional[str]):

    font = pygame.font.SysFont("arial", 14, bold=True)
    tool_buttons = get_toolbar_button_rects(left_panel.get_rect())

    for b_key, rect in tool_buttons.items():
        b_data = BUILDING_TYPES[b_key]
        is_selected = (b_key == active_tool)

        bg_color = (70, 90, 120) if is_selected else (45, 48, 60)
        border_color = (100, 190, 255) if is_selected else (70, 75, 90)

        pygame.draw.rect(left_panel, bg_color, rect, border_radius=4)
        pygame.draw.rect(left_panel, border_color, rect, width=2, border_radius=4) 

        tag_rect = pygame.Rect(rect.x + 8, rect.y + 10, 20, 20)
        pygame.draw.rect(left_panel, b_data.get("color", (200, 200, 200)), tag_rect, border_radius=3)

        label = font.render(f"{b_data['name']} (${b_data['cost']})", True, (240, 240, 240))
        left_panel.blit(label, (tag_rect.right + 10, rect.y + 11))
