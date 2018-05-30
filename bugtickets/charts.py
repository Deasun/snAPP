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
Apply class methods to filter current & completed BugTicket chart data
"""
line_chart.add('Active', [
     int(BugTicket.qs_active_bugs(0)),
     int(BugTicket.qs_active_bugs(7)),
     int(BugTicket.qs_active_bugs(30)),
         ], dots_size=6)
line_chart.add('Completed', [
     int(BugTicket.qs_complete_bugs(0)),
     int(BugTicket.qs_complete_bugs(7)),         
     int(BugTicket.qs_complete_bugs(30)),
         ], dots_size=6)
chart_data = line_chart.render_data_uri()    


"""
Half-Pie chart for bug_types
"""
pie_chart = pygal.Pie(half_pie=True)
pie_chart.title = 'Bug Reports Received'
pie_chart.add('Functional', int(BugTicket.qs_by_bug_type('Functional')))
pie_chart.add('Communication', int(BugTicket.qs_by_bug_type('Communication')))
pie_chart.add('Syntax', int(BugTicket.qs_by_bug_type('Syntax')))
pie_chart.add('Error Notices', int(BugTicket.qs_by_bug_type('Error Notices')))
pie_chart.add('Calculation Errors', int(BugTicket.qs_by_bug_type('Calculation Errors')))
pie_chart.add('Flow Problems', int(BugTicket.qs_by_bug_type('Flow Problems')))
pie_chart_data = pie_chart.render_data_uri()  


