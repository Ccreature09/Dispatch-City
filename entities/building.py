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

        # Fetch sprite image from TILE_IMAGES dictionary
        self.sprite = TILE_IMAGES.get(building_key)

        self.rect = pygame.Rect(
            col * tile_size, 
            row * tile_size, 
            tile_size, 
            tile_size
        )

    def draw(self, surface: pygame.Surface):
        """Draws building sprite image, with fallback to colored box."""
        sprite = TILE_IMAGES.get(self.key)
        if sprite:
            scaled_sprite = pygame.transform.scale(sprite, (self.rect.width, self.rect.height)) # How does it work
            surface.blit(scaled_sprite, self.rect)
        else:
            padding_rect = self.rect.inflate(-8, -8)
            pygame.draw.rect(surface, self.color, padding_rect)

   