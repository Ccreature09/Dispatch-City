import pygame

TILE_IMAGES = {}

def load_assets(tile_size):

    global TILE_IMAGES

    def load_sprite(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, (tile_size, tile_size))

    TILE_IMAGES["POLICE"] = load_sprite("assets/tiles/police_tile.png")
    TILE_IMAGES["WATER"] = load_sprite("assets/tiles/water_tile.png")
    TILE_IMAGES["ROAD"] = load_sprite("assets/tiles/water_tile.png")
    TILE_IMAGES["GRASS"] = load_sprite("assets/tiles/grass_tile.png")


    return TILE_IMAGES
