from CapturingVideoWithCountours import df
from bokeh.plotting import output_file, show, figure
import pandas
p = figure(x_axis_type="datetime", height=300,
           width=800, title="Motion Graphs")
p.quad(left=df["Start"], right=df["End"], bottom=0, top=1,
       color="blue") 
p.yaxis.visible = False 
p.ygrid.grid_line_color = None  
output_file("Graph.html")
show(p)
