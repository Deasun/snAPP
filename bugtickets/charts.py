import pygal
from pygal.style import Style
from .models import BugTicket

"""
Style pygal chart for bugticket list
"""
custom_style = Style(
    font_family='googlefont:Anton',
    legend_font_size = 30,
    value_font_size = 20,
    tooltip_font_size = 30,
    major_label_font_size = 20,
    label_font_size = 20,
    value_label_font_size = 30,
    background='transparent',
    plot_background='transparent',
    foreground='#fff',
    foreground_strong='#fff',
    foreground_subtle='##1e6992',
    opacity='.6',
    opacity_hover='.9',
    transition='400ms ease-in',
    colors=('#ff01c0', '#1eb13b')
    )
line_chart = pygal.Line(fill=True, interpolate='cubic', style=custom_style, legend_at_bottom=True, x_label_rotation=-20)
line_chart.x_labels = 'today', 'last 7 days', 'last 30 days'

"""
Class methods to filer Active & Complete BugTicket chart data
"""
line_chart.add('Started', [
     int(BugTicket.qs_today_active_bugs()),
     int(BugTicket.qs_7_day_active_bugs()),
     int(BugTicket.qs_30_day_active_bugs()),
         ], dots_size=6)
line_chart.add('Completed', [
     int(BugTicket.qs_today_complete_bugs()),
     int(BugTicket.qs_7_day_complete_bugs()),         
     int(BugTicket.qs_30_day_complete_bugs()),
         ], dots_size=6)
chart_data = line_chart.render_data_uri()    
