import pygame

TILE_IMAGES = {}

def load_assets(tile_size: int):

    global TILE_IMAGES

    def load_sprite(path: str):
        try:
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (tile_size, tile_size))
        except pygame.error:
            # Fallback if image path does not exist yet
            return None

    TILE_IMAGES["POLICE"] = load_sprite("assets/tiles/police_tile.png")
    TILE_IMAGES["HOSPITAL"] = load_sprite("assets/tiles/hospital_tile.png")
    TILE_IMAGES["KINDERGARTEN"] = load_sprite("assets/tiles/kindergarten_tile.png")

    TILE_IMAGES["WATER"] = load_sprite("assets/tiles/water_tile.png")
    TILE_IMAGES["ROAD"] = load_sprite("assets/tiles/road_tiles/road_tile_horizontal.png")
    TILE_IMAGES["GRASS"] = load_sprite("assets/tiles/grass_tile.png")

    return TILE_IMAGES