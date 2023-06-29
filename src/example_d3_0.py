import numpy as np

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.util.hex import axial_to_cartesian

output_file("hex_coords.html")

q = np.array([0,  0, 0, -1, -1,  1, 1])
r = np.array([0, -1, 1,  0,  1, -1, 0])

p = figure(width=400, height=400, toolbar_location=None, outline_line_color="white")

p.text([100], [100], text=['H'], text_baseline="middle", text_align="center", text_font_size="30px")
p.segment(x0=[100], x1=[200], y0=[100], y1=[100], color="black", line_width="3px", name="p1")
show(p)

