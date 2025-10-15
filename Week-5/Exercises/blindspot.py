from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_LEFT, K_RIGHT, K_UP, K_DOWN

# experiment setup
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["eye", "key", "radius", "x", "y"])
control.set_develop_mode()
control.initialize(exp)

def make_circle(radius, pos=(0,0)):
    c = stimuli.Circle(radius, position=pos, anti_aliasing=10)
    c.preload()
    return c

def make_fix(size=(150,150), width=10, pos=(0,0)):
    fx = stimuli.FixCross(size=size, line_width=width, position=pos)
    fx.preload()
    return fx

def show(fx, circ):
    exp.screen.clear()
    fx.present(clear=False, update=False)
    circ.present(clear=False, update=False)
    exp.screen.update()

def instructions(side):
    if side == "left":
        which_eye = "right"
        fix_side = "left"
    else:
        which_eye = "left"
        fix_side = "right"
    msg = (
        f"Cover your {which_eye} eye.\n"
        f"Keep looking at the {fix_side} cross.\n\n"
        "Use the arrow keys to move the circle around.\n"
        "Press 1 to make it smaller, 2 to make it bigger.\n"
        "Try to find the spot where it disappears.\n\n"
        "When you’re done, press SPACE."
    )
    stimuli.TextScreen("Blind Spot Task", msg).present()
    exp.keyboard.wait()

def run_trial(side="left"):
    fx_pos = (-300, 0) if side == "left" else (300, 0)
    fix = make_fix(pos=fx_pos)

    radius = 75
    circ = make_circle(radius)
    step = 10
    size_step = 10
    min_r = 5
    show(fix, circ)

    SPACE = ord(' ')
    SMALLER = ord('1')
    BIGGER = ord('2')
    keys = [K_LEFT, K_RIGHT, K_UP, K_DOWN, SMALLER, BIGGER, SPACE]

    while True:
        key, _ = exp.keyboard.wait(keys=keys)

        if key == K_LEFT:
            circ.move((-step, 0))
            exp.data.add([side, "left", radius, circ.position[0], circ.position[1]])
        elif key == K_RIGHT:
            circ.move((step, 0))
            exp.data.add([side, "right", radius, circ.position[0], circ.position[1]])
        elif key == K_UP:
            circ.move((0, step))
            exp.data.add([side, "up", radius, circ.position[0], circ.position[1]])
        elif key == K_DOWN:
            circ.move((0, -step))
            exp.data.add([side, "down", radius, circ.position[0], circ.position[1]])
        elif key == SMALLER:
            radius = max(min_r, radius - size_step)
            circ = make_circle(radius, pos=circ.position)
            exp.data.add([side, "smaller", radius, circ.position[0], circ.position[1]])
        elif key == BIGGER:
            radius += size_step
            circ = make_circle(radius, pos=circ.position)
            exp.data.add([side, "bigger", radius, circ.position[0], circ.position[1]])
        elif key == SPACE:
            exp.data.add([side, "end", radius, circ.position[0], circ.position[1]])
            break

        show(fix, circ)

# main flow
control.start(subject_id=1)

stimuli.TextScreen("Blind Spot", "There will be two short trials (left and right).\nPress any key to start.").present()
exp.keyboard.wait()

instructions("left")
run_trial("left")

instructions("right")
run_trial("right")

stimuli.TextScreen("Done", "Press any key to quit.").present()
exp.keyboard.wait()
control.end()
