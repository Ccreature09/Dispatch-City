BUILDING_TYPES = {
    "POLICE": {
        "name": "Police Station",
        "cost": 150,
        "radius": 1,              # 1 tile in all directions = 3x3 coverage
        "color": (59, 130, 246),  # Blue
        "type": "RADIUS"
    },
    "HOSPITAL": {
        "name": "Clinic",
        "cost": 300,
        "radius": 2,              # 2 tiles in all directions = 5x5 coverage
        "color": (239, 68, 68),   # Red
        "type": "RADIUS"
    },
    "KINDERGARTEN": {
        "name": "Kindergarten",
        "cost": 200,
        "capacity": 100,          # Serves up to 100 children
        "color": (245, 158, 11),  # Amber
        "type": "CAPACITY"
    },
    "ROAD": {
        "name": "Road",
        "cost": 50,
        "color": (255, 255, 255),
        "type": "ROAD"
        
        
    }
}