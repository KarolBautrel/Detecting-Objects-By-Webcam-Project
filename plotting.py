from CapturingVideoWithCountours import df
from bokeh.plotting import output_file, show, figure
import pandas
p = figure(x_axis_type="datetime", height=300,
           width=800, title="Motion Graphs")
# ustawienie wykresu w formie quadrantow. lewy bok to start a prawy to end czyli koniec
p.quad(left=df["Start"], right=df["End"], bottom=0, top=1,
       color="blue")  # bottom zostawiamy 0 a top 1
p.yaxis.visible = False  # wylaczenie widzialnosci wartosci osi y
p.ygrid.grid_line_color = None  # wylaczenie siatki y
output_file("Graph.html")
show(p)
