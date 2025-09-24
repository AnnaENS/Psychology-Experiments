from expyriment import design, control, stimuli
from expyriment.misc import geometry

control.defaults.initialise_delay = 0
control.defaults.window_mode = True
control.defaults.fast_quit = True

exp = design.Experiment(name="Two Squares")
control.initialize(exp)

square_size = 50
separation = 200

left_pos = (-separation // 2, 0)
right_pos = (separation // 2, 0)

#red_square = stimuli.Rectangle(size=(square_size, square_size), colour=(255, 0, 0), position=left_pos)
#green_square = stimuli.Rectangle(size=(square_size, square_size), colour=(0, 255, 0), position=right_pos)

yellow_hexagon = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(6, 25), colour=(255, 255, 0), position=right_pos)
purple_triangle = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(3, 50), colour=(128, 0, 128), position=left_pos)

line_1 = stimuli.Line((-separation // 2, 20), (-separation // 2, 50), line_width=3)
line_2 = stimuli.Line((separation // 2, 20), (separation // 2, 50), line_width=3)

text_triangle = stimuli.TextLine("triangle", position=(-separation //2, 60))
text_hexagon = stimuli.TextLine("hexagon", position=(separation //2, 60))

control.start(subject_id=1)

#red_square.present(clear=True, update=False)
#green_square.present(clear=False, update=True)

purple_triangle.present(clear=True, update=False)
yellow_hexagon.present(clear=False, update=True)
text_triangle.present(clear=False, update=True)

bl = stimuli.BlankScreen()
purple_triangle.plot(bl)
yellow_hexagon.plot(bl)
line_1.plot(bl)
line_2.plot(bl)
text_triangle.plot(bl)
text_hexagon.plot(bl)
bl.present()

exp.keyboard.wait()

control.end()