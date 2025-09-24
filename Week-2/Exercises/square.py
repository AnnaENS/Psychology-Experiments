# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.defaults.initialise_delay = 0
control.defaults.window_mode = True
control.defaults.fast_quit = True

exp = design.Experiment(name = "Square")

control.initialize(exp)

square = stimuli.Rectangle(size=(50,50), colour=(0, 0, 255))

fixation = stimuli.FixCross()

control.start(subject_id=1)

square.present(clear=True, update=False)
fixation.present(clear=False, update=True)
exp.clock.wait(1000)

square.present(clear=True, update=True)

exp.keyboard.wait()

control.end()
