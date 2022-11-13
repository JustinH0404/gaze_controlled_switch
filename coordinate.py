from screeninfo import get_monitors
import datetime as dt
import mouse

# assuming single monitor
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height

GAZE_THRESHOLD = 500 # 500 ms
offset_x = 0
offset_y = 0
dot_r = 20

signal_deltas = {"left": 123, "right": 123, "up": 123, "down": 123} # pix / signal
# NEED TO INPUT VALUES IN DICT FROM CALIBRATION (could return a dict)
min_x = offset_x + 50
min_y = offset_y + 50
max_x = screen_width - 50
max_y = screen_height - 50

last_x = min_x
last_y = min_y
curr_x = min_x
curr_y = min_y
last_move_time = dt.datetime.now()

# start at top left
def signal_to_coord(eog__x, eog_y):
    # left = ;
    # up = ;
    if left:
        curr_x += eog_x * signal_deltas['left']
    else:
        curr_x += eog_x * signal_deltas['right']

    if up:
        curr_y += eog_y * signal_deltas['up']
    else:
        curr_y -= eog_y * signal_deltas['down']

# need to determine eye_x, eye_y from signal -> coordinate function
def window_switch(eye_x, eye_y):
    prev_x, prev_y = mouse.get_position()
    mouse.move(eye_x, eye_y, absolute=True, duration=0)
    mouse.click('left')
    mouse.move(prev_x, prev_y, absolute=True, duration=0)


while True: # infinite loop during tracking - CHANGE LATER
    # TODO: need to take in a signal
    move = last_x != curr_x or last_y != curr_y
    # TODO: within a threshold (need to account for drifting)
    # TODO: check boundaries
    if move:
        last_move_time = dt.datetime.now()
    else:
        now = dt.datetime.now()
        time_diff = now - last_move_time
        if time_diff.total_seconds() * 1000 >= GAZE_THRESHOLD:
            window_switch(curr_x, curr_y)

    signal_to_coord(sig_x, sig_y)
