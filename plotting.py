from CapturingVideoWithCountours import df
from bokeh.plotting import output_file, show, figure
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.io import curdoc


# changing format of column to showing date as (year - month- day, hour-min-sec)
df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")

df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


# reading data from df column's
cds = ColumnDataSource(df)
curdoc().theme = 'dark_minimal'
p = figure(x_axis_type="datetime", height=300,
           width=800, title="Motion Graphs")
hover = HoverTool(
    tooltips=[("Start_string", "@Start_string"), ("End_string", "@End_string")])  # adding to tooltip values
p.add_tools(hover)

p.quad(left="Start", right="End", bottom=0, top=1,# plot as quadrant. Left side of quad will display "Start" column value and righ "End" column value.
       color="slategray", source=cds)   # source = cds means we are using columns from pandas (cds are our df)
p.yaxis.visible = False  # 
p.ygrid.grid_line_color = None  # 
output_file("Graph.html")
show(p)
