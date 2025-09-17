# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.defaults.initialise_delay = 0 # No countdown
control.defaults.window_mode = True # Not full-screen
control.defaults.fast_quit = True # No goodbye message

exp = design.Experiment(name = "Square")

control.initialize(exp)

square = stimuli.Rectangle(size=(50,50), coulour=(0, 0, 255))

fixation = stimuli.FixCross()

control.start(subject_id=1)

square.present(clear=True, update=True)

fixation.present(clear=True, update=True)

exp.clock.wait(1000)

square.present(clear=True, update=True)

exp.keyboard.wait()

control.end()
