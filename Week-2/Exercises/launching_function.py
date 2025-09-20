from expyriment import design, control, stimuli
import time

def launching_event(exp, temporal_gap=0, spatial_gap=0, speed=1):
    square_size = 50
    separation = 400

    left_pos = (-separation // 2, 0)
    right_pos = (0 + spatial_gap, 0)

    red_square = stimuli.Rectangle(size=(square_size, square_size), colour=(255, 0, 0), position=left_pos)
    green_square = stimuli.Rectangle(size=(square_size, square_size), colour=(0, 255, 0), position=right_pos)

    red_square.present(clear=True, update=False)
    green_square.present(clear=True, update=True)
    exp.clock.wait(1000)

    steps = 20
    dx = (right_pos[0] - left_pos[0] - square_size) / steps
    dy = (right_pos[1] - left_pos[1]) / steps

    # red square moves till green square and stops
    for _ in range(steps):
        red_square.move((dx, dy))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
        time.sleep(0.05)

    # optional temporal gap before green moves
    if temporal_gap > 0:
        exp.clock.wait(temporal_gap)

    # green square moves the same distance
    green_steps = int(steps / speed)
    green_dx = dx * speed
    green_dy = dy * speed
    for _ in range(green_steps):
        green_square.move((green_dx, green_dy))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
        time.sleep(0.05)

    # display for 1 second
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1000)

if __name__ == "__main__":
    control.defaults.initialise_delay = 0
    control.defaults.window_mode = True
    control.defaults.fast_quit = True

    exp = design.Experiment(name="Launching Function")
    control.initialize(exp)
    control.start(subject_id=1)

    # Michottean launching
    launching_event(exp, temporal_gap=0, spatial_gap=0, speed=1)
    
    # launching with a temporal gap
    launching_event(exp, temporal_gap=2000, spatial_gap=0, speed=1)

    # launching with a spatial gap
    launching_event(exp, temporal_gap=0, spatial_gap=50, speed=1)

    # triggering
    launching_event(exp, temporal_gap=0, spatial_gap=0, speed=3)

    time.sleep(1)
    control.end()