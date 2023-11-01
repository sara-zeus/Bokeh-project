from bokeh.io import output_file
from bokeh.plotting import figure, show

output_file("output_file_test.html", title="Empty Bokeh Figure")

fig = figure(
    background_fill_color="gray",
    background_fill_alpha=0.5,
    border_fill_color="blue",
    border_fill_alpha=0.25,
    height=300,  # Use 'height' instead of 'plot_height'
    width=500,  # Use 'width' instead of 'plot_width'
    x_axis_label="X Label",
    x_axis_type="datetime",
    x_axis_location="above",
    x_range=("2018-01-01", "2018-06-30"),
    y_axis_label="Y Label",
    y_axis_type="linear",
    y_axis_location="left",
    y_range=(0, 100),
    title="Example Figure",
    title_location="right",
    toolbar_location="below",
    tools="save",
)

# now want to make some changes to the figure
# Removing the gridline color
fig.grid.grid_line_color = None

show(fig)
