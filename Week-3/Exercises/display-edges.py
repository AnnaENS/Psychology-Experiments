from expyriment import design, control, stimuli
import time

control.defaults.initialise_delay = 0
control.defaults.window_mode = True
control.defaults.fast_quit = True

exp = design.Experiment(name="Four Squares")
control.initialize(exp)

control.set_develop_mode()

width, height = exp.screen.size

square_size = 0.05 * width

bl_pos = (-width // 2 + square_size // 2, -height // 2 + square_size // 2)
tl_pos = (-width // 2 + square_size // 2, height //2 - square_size // 2)
tr_pos = (width // 2 - square_size // 2, height // 2 - square_size // 2)
br_pos = (width // 2 - square_size // 2, -height // 2 + square_size // 2)


# initial position
bl_square = stimuli.Rectangle(size=(square_size, square_size), colour=(255, 0, 0), position=bl_pos, line_width=1)
tl_square = stimuli.Rectangle(size=(square_size, square_size), colour=(255, 0, 0), position=tl_pos, line_width=1)
tr_square = stimuli.Rectangle(size=(square_size, square_size), colour=(255, 0, 0), position=tr_pos, line_width=1)
br_square = stimuli.Rectangle(size=(square_size, square_size), colour=(255, 0, 0), position=br_pos, line_width=1)

control.start(subject_id=1)

bl_square.present(clear=True, update=False)
tl_square.present(clear=False, update=False)
tr_square.present(clear=False, update=False)
br_square.present(clear=False, update=True)


# display for 1 second
#time.sleep(1)

exp.keyboard.wait()
control.end()