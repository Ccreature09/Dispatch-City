import pygame

def calculate_layout(win_w: int, win_h: int):
    left_w = int(win_w * 0.20)
    right_w = int(win_w * 0.25)
    main_w = win_w - left_w - right_w

    left_rect = pygame.Rect(0, 0, left_w, win_h)
    main_rect = pygame.Rect(left_w, 0, main_w, win_h)
    right_rect = pygame.Rect(left_w + main_w, 0, right_w, win_h)

    return left_rect, main_rect, right_rect

def draw_3_window_layout(screen: pygame.Surface, left_rect: pygame.Rect, main_rect: pygame.Rect, right_rect: pygame.Rect):

    left_panel = screen.subsurface(left_rect)
    main_panel = screen.subsurface(main_rect)
    right_panel = screen.subsurface(right_rect)

    left_panel.fill((30, 32, 40))
    main_panel.fill((15, 15, 20))   
    right_panel.fill((40, 32, 35))

    pygame.draw.line(screen, (70, 70, 80), (left_rect.right, 0), (left_rect.right, screen.get_height()), 2)
    pygame.draw.line(screen, (70, 70, 80), (main_rect.right, 0), (main_rect.right, screen.get_height()), 2)



