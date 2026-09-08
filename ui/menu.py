import pygame
from config import MENU_TITLE_SIZE_MULTIPLIER, MENU_SUBTITLE_SIZE_MULTIPLIER, MENU_TITLE_COLOR, MENU_SUBTITLE_COLOR

def draw_menu_header(screen: pygame.Surface, win_w: int, win_h: int):

    title_size = int(win_h * MENU_TITLE_SIZE_MULTIPLIER)
    subtitle_size = int(win_h * MENU_SUBTITLE_SIZE_MULTIPLIER)

    font_title = pygame.font.SysFont("arial", title_size, bold=True)
    font_subtitle = pygame.font.SysFont("arial", subtitle_size)

    title_surface = font_title.render("DISPATCH CITY", True, MENU_TITLE_COLOR)
    subtitle_surface = font_subtitle.render("Select difficulty to start", True, MENU_SUBTITLE_COLOR)

    title_x = (win_w // 2) - (title_surface.get_width() // 2)
    title_y = int(win_h * 0.20)

    subtitle_x = (win_w // 2) - (subtitle_surface.get_width() // 2)
    subtitle_y = int(win_h * 0.28)

    screen.blit(title_surface, (title_x, title_y))
    screen.blit(subtitle_surface, (subtitle_x, subtitle_y))

def get_button_rects(win_w: int, win_h: int):

    btn_w = int(win_w * 0.25)
    btn_h = int(win_h * 0.08)
    spacing = int(win_h * 0.03)
    start_y = int(win_h * 0.38)

    center_x = (win_w // 2) - (btn_w // 2)

    buttons = {}

    for idx, key in enumerate(["EASY", "MEDIUM", "HARD"]):
        btn_y = start_y + idx * (btn_h + spacing)
        buttons[key] = pygame.Rect(center_x, btn_y, btn_w, btn_h)

    return buttons

def draw_menu(screen: pygame.Surface, win_w:int, win_h:int):
    screen.fill((20,22,28))

    draw_menu_header(screen, win_w, win_h)
    button_rects = get_button_rects(win_w, win_h)
    mouse_pos = pygame.mouse.get_pos()
    font_btn = pygame.font.SysFont("arial", int(win_h * 0.035), bold=True)

    for key, rect in button_rects.items():
        is_hovered = rect.collidepoint(mouse_pos)

        btn_color = (60,130,210) if is_hovered else (45, 50, 65)

        pygame.draw.rect(screen, btn_color, rect, border_radius=6)

        text_surf = font_btn.render(key, True, (255, 255, 255))
        text_x = rect.x + (rect.width - text_surf.get_width()) // 2
        text_y = rect.y + (rect.height - text_surf.get_height()) // 2
        screen.blit(text_surf, (text_x,text_y))

    return button_rects
