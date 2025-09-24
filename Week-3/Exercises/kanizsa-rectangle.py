from expyriment import design, control, stimuli

def show_kanizsa_rectangle(aspect_ratio=2.0, rect_scale=0.25, circle_scale=0.05):
    control.defaults.initialise_delay = 0
    control.defaults.window_mode = True
    control.defaults.fast_quit = True

    exp = design.Experiment(name="Kanizsa Rectangle", background_colour=(128, 128, 128))
    control.initialize(exp)
    control.set_develop_mode()

    width, height = exp.screen.size

    rect_width = rect_scale * width
    rect_height = rect_width / aspect_ratio

    circle_radius = circle_scale * width

    rect_pos = (0, 0)

    bl_pos_circle = (-rect_width // 2 + rect_pos[0], -rect_height // 2 + rect_pos[1])
    tl_pos_circle = (-rect_width // 2 + rect_pos[0], rect_height // 2 + rect_pos[1])
    tr_pos_circle = (rect_width // 2 + rect_pos[0], rect_height // 2 + rect_pos[1])
    br_pos_circle = (rect_width // 2 + rect_pos[0], -rect_height // 2 + rect_pos[1])

    rectangle = stimuli.Rectangle(size=(rect_width, rect_height), colour=(128, 128, 128), position=rect_pos)
    bl_circle = stimuli.Circle(radius=circle_radius, position=bl_pos_circle, colour=(255,255,255))
    tl_circle = stimuli.Circle(radius=circle_radius, position=tl_pos_circle, colour=(0,0,0))
    tr_circle = stimuli.Circle(radius=circle_radius, position=tr_pos_circle, colour=(0,0,0))
    br_circle = stimuli.Circle(radius=circle_radius, position=br_pos_circle, colour=(255,255,255))

    control.start(subject_id=1)

    bl_circle.present(clear=True, update=False)
    tl_circle.present(clear=False, update=False)
    tr_circle.present(clear=False, update=False)
    br_circle.present(clear=False, update=False)
    rectangle.present(clear=False, update=True)

    exp.keyboard.wait()
    control.end()

show_kanizsa_rectangle(aspect_ratio=2.0, rect_scale=0.7, circle_scale=0.07)
