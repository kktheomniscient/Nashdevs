# Asset paths
PLAYER_IMAGE_PATH = "assets/player.png"
ZOMBIE_IMAGE_PATH = "assets/zombie.png"
SPECIAL_ZOMBIE_IMAGE_PATH = "assets/special_zombie.png"

# --- Constants ---
WIDTH = 1280 #800
HEIGHT = 720 #600
FPS = 60
GRID_SPACING = 100
PLAYER_MAX_HEALTH = 100
PLAYER_START_AMMO = 20
HEALTH_PACK_AMOUNT = 25
AMMO_PACK_AMOUNT = 10
BULLET_SPEED = 15
BULLET_RANGE = 500

# Maze settings
MAZE_REGION_SIZE = 2000  
MAZE_CELL_SIZE = 200     
MAZE_FILL_PROB = 0.3     
DESTRUCTIBLE_PROB = 0.3  
DYNAMIC_PROB = 0.1       
SAFE_ZONE_MARGIN = 150   

# Colors
BLACK = (0, 0, 0)
DARK_RED = (100, 0, 0)
PLAYER_COLOR = (0, 200, 0)
ZOMBIE_COLOR = (150, 50, 50)
SPECIAL_ZOMBIE_COLOR = (255, 100, 0)
OBSTACLE_COLOR = (80, 80, 80)
DESTRUCTIBLE_COLOR = (150, 80, 80)
DYNAMIC_COLOR = (70, 130, 180)
GRID_COLOR = (40, 40, 60)
TEXT_COLOR = (240, 240, 240)

# Player settings
PLAYER_SIZE = 75
PLAYER_SPEED = 5

# Zombie settings
BASE_ZOMBIE_SIZE = 77
BASE_ZOMBIE_SPEED = 2.5
ZOMBIE_SIZE = BASE_ZOMBIE_SIZE
ZOMBIE_SPEED = BASE_ZOMBIE_SPEED
SPAWN_INTERVAL = 3000
MIN_SPAWN_DIST = 500
SPECIAL_ZOMBIE_PROXIMITY_RADIUS = 150  
SPECIAL_ZOMBIE_IMMOBILE_DURATION = 3000  
COLLISION_THRESHOLD = 35

# Level settings
LEVEL_DURATION = 30000
MINI_GAME_DURATION = 120000
DYNAMIC_OBSTACLE_INTERVAL = 2000
