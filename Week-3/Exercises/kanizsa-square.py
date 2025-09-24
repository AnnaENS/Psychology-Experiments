from expyriment import design, control, stimuli
import time

control.defaults.initialise_delay = 0
control.defaults.window_mode = True
control.defaults.fast_quit = True

#exp = design.Experiment(name="Kanizsa Squares")
exp = design.Experiment(name="Kanizsa Squares", background_colour=(128, 128, 128))
control.initialize(exp)

control.set_develop_mode()

width, height = exp.screen.size

square_size = 0.25 * width

circle_radius = 0.05 * width

bl_pos_circle = (-square_size//2, -square_size//2)
tl_pos_circle = (-square_size // 2, square_size // 2)
tr_pos_circle = (square_size // 2, square_size // 2)
br_pos_circle = (square_size // 2, -square_size // 2)


# initial position
square = stimuli.Rectangle(size=(square_size, square_size), colour=(128, 128, 128), position=(0,0))

bl_circle = stimuli.Circle(radius=circle_radius, position=bl_pos_circle, colour=(255,255,255))
tl_circle = stimuli.Circle(radius=circle_radius, position=tl_pos_circle, colour=(0,0,0))
tr_circle = stimuli.Circle(radius=circle_radius, position=tr_pos_circle, colour=(0,0,0))
br_circle = stimuli.Circle(radius=circle_radius, position=br_pos_circle, colour=(255,255,255))

control.start(subject_id=1)

bl_circle.present(clear=True, update=False)
tl_circle.present(clear=False, update=False)
tr_circle.present(clear=False, update=False)
br_circle.present(clear=False, update=False)
square.present(clear=False, update=True)

# display for 1 second
#time.sleep(1)

exp.keyboard.wait()
control.end()