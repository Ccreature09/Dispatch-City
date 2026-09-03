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

