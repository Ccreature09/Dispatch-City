import pygame
from entities.building_data import BUILDING_TYPES
from assets import TILE_IMAGES

class Building:
    def __init__(self, col, row, building_key, tile_size):
        self.col = col
        self.row = row
        self.key = building_key
        
        # Load properties directly from data dictionary
        data = BUILDING_TYPES[building_key]
        self.name = data["name"]
        self.cost = data["cost"]
        self.color = data.get("color", (255, 255, 255))
        self.category = data["type"]
        self.radius = data.get("radius", 0)
        self.capacity = data.get("capacity", 0)

        # 1. Fetch sprite image from pre-loaded TILE_IMAGES dictionary
        self.sprite = TILE_IMAGES.get(building_key)

        # Pygame spatial rectangle
        self.rect = pygame.Rect(
            col * tile_size, 
            row * tile_size, 
            tile_size, 
            tile_size
        )

    def draw(self, surface):
        """Draws building sprite image, with fallback to colored box."""
        if self.sprite:
            surface.blit(self.sprite, self.rect)
        else:
            padding_rect = self.rect.inflate(-8, -8)
            pygame.draw.rect(surface, self.color, padding_rect)

   