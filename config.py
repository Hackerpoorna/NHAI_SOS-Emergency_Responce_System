# =========================================================
# NHAI SOS - APPLICATION CONFIGURATION
# =========================================================

# ---------------------------------------------------------
# APPLICATION
# ---------------------------------------------------------

APP_TITLE = "NHAI • Highway Emergency Surveillance"

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 850

MIN_WINDOW_WIDTH = 1200
MIN_WINDOW_HEIGHT = 750


# ---------------------------------------------------------
# THEME COLORS
# ---------------------------------------------------------

BACKGROUND_COLOR = "#080D14"

HEADER_COLOR = "#0D141D"

PANEL_COLOR = "#0D141D"

CARD_COLOR = "#111923"

TEXT_PRIMARY = "#E8EDF3"

TEXT_SECONDARY = "#AAB4C0"

TEXT_MUTED = "#7F8B99"

NHAI_YELLOW = "#F4C430"

SUCCESS_GREEN = "#48D597"

SOS_RED = "#C81E2A"

SOS_RED_HOVER = "#E52B38"

EMERGENCY_RED = "#FF3B30"

WARNING_ORANGE = "#FF9F1C"


# ---------------------------------------------------------
# ANDHRA PRADESH MAP
# ---------------------------------------------------------

ANDHRA_PRADESH_CENTER = (
    16.5062,
    80.6480
)

DEFAULT_MAP_ZOOM = 7

EMERGENCY_MAP_ZOOM = 12


# ---------------------------------------------------------
# NHAI HIGHWAYS
# ---------------------------------------------------------

HIGHWAYS = [
    {
        "name": "NH-16",
        "location": "Vijayawada",
        "latitude": 16.5062,
        "longitude": 80.6480,
        "status": "NORMAL"
    },

    {
        "name": "NH-16",
        "location": "Guntur",
        "latitude": 16.3067,
        "longitude": 80.4365,
        "status": "NORMAL"
    },

    {
        "name": "NH-16",
        "location": "Nellore",
        "latitude": 14.4426,
        "longitude": 79.9865,
        "status": "MONITORING"
    },

    {
        "name": "NH-16",
        "location": "Visakhapatnam",
        "latitude": 17.6868,
        "longitude": 83.2185,
        "status": "NORMAL"
    },

    {
        "name": "NH-44",
        "location": "Kurnool",
        "latitude": 15.8281,
        "longitude": 78.0373,
        "status": "ROAD WORK"
    },

    {
        "name": "NH-40",
        "location": "Kadapa",
        "latitude": 14.4673,
        "longitude": 78.8242,
        "status": "MONITORING"
    }
]


# ---------------------------------------------------------
# EMERGENCY TYPES
# ---------------------------------------------------------

EMERGENCY_TYPES = [

    {
        "type": "VEHICLE ACCIDENT",
        "response": "AMBULANCE",
        "symbol": "🚑"
    },

    {
        "type": "ACCIDENT WITH FIRE",
        "response": "FIRE",
        "symbol": "🚒"
    },

    {
        "type": "MEDICAL EMERGENCY",
        "response": "AMBULANCE",
        "symbol": "🚑"
    },

    {
        "type": "VEHICLE BREAKDOWN",
        "response": "PATROL",
        "symbol": "🚓"
    },

    {
        "type": "ROAD OBSTRUCTION",
        "response": "HIGHWAY RESPONSE",
        "symbol": "🚧"
    },

    {
        "type": "FIRE EMERGENCY",
        "response": "FIRE",
        "symbol": "🚒"
    },

    {
        "type": "MULTIPLE VEHICLE COLLISION",
        "response": "AMBULANCE",
        "symbol": "🚑"
    },

    {
        "type": "HAZARDOUS ROAD CONDITION",
        "response": "PATROL",
        "symbol": "🚓"
    },

    {
        "type": "VEHICLE FIRE",
        "response": "FIRE",
        "symbol": "🚒"
    },

    {
        "type": "MEDICAL ASSISTANCE REQUIRED",
        "response": "AMBULANCE",
        "symbol": "🚑"
    }
]


# ---------------------------------------------------------
# EMERGENCY RESPONSE SETTINGS
# ---------------------------------------------------------

SOS_DELAY_SECONDS = 5

MAX_INCIDENT_HISTORY = 100

DEFAULT_INCIDENT_STATUS = "DISPATCH INITIATED"

RESPONSE_STATUS = "UNIT EN ROUTE"

ARRIVED_STATUS = "RESPONSE UNIT ARRIVED"


# ---------------------------------------------------------
# RESPONSE SPEED SIMULATION
# ---------------------------------------------------------

AMBULANCE_SPEED = 60

FIRE_SPEED = 50

PATROL_SPEED = 70


# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------

DATABASE_NAME = "nhai_sos.db"


# ---------------------------------------------------------
# SYSTEM STATUS
# ---------------------------------------------------------

SYSTEM_STATUS = "SYSTEM ONLINE"

DEFAULT_HIGHWAY_STATUS = "NORMAL"