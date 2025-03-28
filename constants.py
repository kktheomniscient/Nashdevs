# constants.py

# Asset paths
PLAYER_IMAGE_PATH = "assets/player.png"
EXKNIFE_IMAGE = "assets/exknife.png"         # Extended arm asset for knife attack
GUN_COMPANION = "assets/survivor_idle.png"
ZOMBIE_IMAGE_PATH = "assets/zombie.png"
SPECIAL_ZOMBIE_IMAGE_PATH = "assets/special_zombie.png"
HEALTH_KIT_IMAGE = "assets/hk.png"             # Health kit asset
AMMO_KIT_IMAGE = "assets/ammo.png"             # Ammo kit asset
PLAYER_PISTOL_IMAGE_PATH = "assets/player_pistol.png"
PLAYER_SHOTGUN_IMAGE_PATH = "assets/player_shotgun.png"
PLAYER_AKM_IMAGE_PATH = "assets/player_akm.png"
PISTOL_IMAGE_PATH = "assets/pistol.png"
SHOTGUN_IMAGE_PATH = "assets/shotgun.png"
AKM_IMAGE_PATH = "assets/akm.png"
KNIFE_IMAGE_PATH = "assets/knife.png"
# --- Constants ---
WIDTH = 1280      # Window width
HEIGHT = 720      # Window height
FPS = 60
GRID_SPACING = 100

PLAYER_MAX_HEALTH = 100
PLAYER_START_AMMO = 20
HEALTH_PACK_AMOUNT = 25
AMMO_PACK_AMOUNT = 10

BULLET_SPEED = 15
BULLET_RANGE = 500
BULLET_COLOR = (255, 255, 0)

# Maze and level settings (as per original)
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
PLAYER_SPEED = 10

# Zombie settings
BASE_ZOMBIE_SIZE = 77
BASE_ZOMBIE_SPEED = 2.3
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
