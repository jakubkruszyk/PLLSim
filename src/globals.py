REFRESH_RATE = 0.02
DATA_POINTS_NUM = 100

START_BUTTON_COLOR = "#36b500"
STOP_BUTTON_COLOR = "#b50000"

MAX_SPEED = 100
MIN_SPEED = 10
DEFAULT_SPEED = 60

MAX_PHASE = 10
MIN_PHASE = -10
DEFAULT_PHASE = 2

MAX_STEP = 20
MIN_STEP = 1
DEFAULT_STEP = 5

MAX_LAG_COUNTER = 20
MIN_LAG_COUNTER = 5
DEFAULT_LAG_COUNTER = 5

MAX_SUM_COUNTER = 40
MIN_SUM_COUNTER = 5
DEFAULT_SUM_COUNTER = 9

MAX_INPUT_PERIOD = 40
MIN_INPUT_PERIOD = 5
DEFAULT_INPUT_PERIOD = 20

MAX_LOCAL_PERIOD = 40
MIN_LOCAL_PERIOD = 5
DEFAULT_LOCAL_PERIOD = 19

PRESETS = {
    "Lagging": {
        "phase": 2,
        "step": 5,
        "lag_counter": 5,
        "sum_counter": 9,
        "input_period": 20,
        "local_period": 19
    },
    "Leading": {
        "phase": -2,
        "step": 5,
        "lag_counter": 5,
        "sum_counter": 9,
        "input_period": 19,
        "local_period": 20
    },
    "Equal": {
        "phase": 2,
        "step": 5,
        "lag_counter": 5,
        "sum_counter": 9,
        "input_period": 20,
        "local_period": 20
    }
}
