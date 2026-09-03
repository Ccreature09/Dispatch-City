SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Game States
STATE_MENU = "MENU"
STATE_PLAYING = "PLAYING"

# Difficulty Settings
DIFFICULTIES = {
    "EASY": {"budget_multiplier": -1, "ambiguous_handbook": False},
    "MEDIUM": {"budget_multiplier": 1.5, "ambiguous_handbook": False},
    "HARD": {"budget_multiplier": 1, "ambiguous_handbook": True}
}

MENU_TITLE_SIZE_MULTIPLIER = 0.06
MENU_SUBTITLE_SIZE_MULTIPLIER = 0.03

# Color
MENU_TITLE_COLOR = (240, 240, 240)
MENU_SUBTITLE_COLOR = (160, 160, 170)