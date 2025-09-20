from expyriment import design, control, stimuli
import time

control.defaults.initialise_delay = 0
control.defaults.window_mode = True
control.defaults.fast_quit = True

exp = design.Experiment(name="Two Squares")
control.initialize(exp)

square_size = 50
separation = 400

left_pos = (-separation // 2, 0)
right_pos = (0, 0)

# initial position
red_square = stimuli.Rectangle(size=(square_size, square_size), colour=(255, 0, 0), position=left_pos)
green_square = stimuli.Rectangle(size=(square_size, square_size), colour=(0, 255, 0), position=right_pos)

control.start(subject_id=1)

red_square.present(clear=True, update=False)
green_square.present(clear=True, update=True)

steps = 20
dx = (right_pos[0] - left_pos[0] - square_size) / steps
dy = (right_pos[1] - left_pos[1]) / steps

# red square moves till green square and stops
for _ in range(steps):
    red_square.move((dx, dy))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    time.sleep(0.05)

# green square moves the same distance
green_dx = dx 
green_dy = dy
for _ in range(steps):
    green_square.move((green_dx, green_dy))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    time.sleep(0.05)

red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)

# display for 1 second
time.sleep(1)
control.end()