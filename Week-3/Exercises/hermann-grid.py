from expyriment import design, control, stimuli

def show_hermann_grid(
    square_size=60,
    space=20,
    rows=6,
    cols=8,
    square_color=(0, 0, 0),
    background_color=(255, 255, 255)
):
    control.defaults.initialise_delay = 0
    control.defaults.window_mode = True
    control.defaults.fast_quit = True

    exp = design.Experiment(name="Hermann Grid", background_colour=background_color)
    control.initialize(exp)
    control.set_develop_mode()

    grid_w = cols * square_size + (cols - 1) * space
    grid_h = rows * square_size + (rows - 1) * space

    start_x = -grid_w // 2 + square_size // 2
    start_y = -grid_h // 2 + square_size // 2

    squares = []
    for i in range(rows):
        for j in range(cols):
            x = start_x + j * (square_size + space)
            y = start_y + i * (square_size + space)
            square = stimuli.Rectangle(size=(square_size, square_size), colour=square_color, position=(x, y))
            squares.append(square)

    control.start(subject_id=1)

    for idx, square in enumerate(squares):
        if idx == 0:
            square.present(clear=True, update=False)
        elif idx == len(squares) - 1:
            square.present(clear=False, update=True)
        else:
            square.present(clear=False, update=False)

    exp.keyboard.wait()
    control.end()

show_hermann_grid(
    square_size=60,
    space=20,
    rows=6,
    cols=8,
    square_color=(0, 0, 0),
    background_color=(255, 255, 255)
)