import pygal
from pygal.style import Style
from .models import BugTicket

"""
Style pygal chart for bugticket list
"""
custom_style = Style(
    font_family='googlefont:Lato',
    legend_font_size = 20,
    value_font_size = 20,
    tooltip_font_size = 40,
    major_label_font_size = 20,
    label_font_size = 20,
    value_label_font_size = 30,
    background='rgba(27, 143, 206, 0.17)',
    plot_background='transparent',
    foreground='#fff',
    foreground_strong='#fff',
    foreground_subtle='##1e6992',
    opacity='.8',
    opacity_hover='0',
    transition='400ms ease-in',
    colors=('#ff01c0', '#1eb13b')
    )
line_chart = pygal.Line(fill=True, legend_at_bottom=True, interpolate='cubic', style=custom_style, x_label_rotation=-20, legend_box_size=18)
line_chart.x_labels = 'today', 'last 7 days', 'lat fortnight', 'last 30 days'

"""Apply class methods to filter current & completed BugTicket chart data"""
line_chart.add('Active', [
     int(BugTicket.qs_active_bugs(0)),
     int(BugTicket.qs_active_bugs(7)),
     int(BugTicket.qs_active_bugs(14)),
     int(BugTicket.qs_active_bugs(30)),
         ], dots_size=6)
line_chart.add('Completed', [
     int(BugTicket.qs_complete_bugs(0)),
     int(BugTicket.qs_complete_bugs(7)),         
     int(BugTicket.qs_complete_bugs(14)),         
     int(BugTicket.qs_complete_bugs(30)),
         ], dots_size=6)
chart_data = line_chart.render_data_uri()    


"""
Pie chart for bug_types
"""
custom_pie_style = Style(
    font_family='googlefont:Lato',
    legend_font_size = 20,
    value_font_size = 20,
    tooltip_font_size = 30,
    major_label_font_size = 20,
    label_font_size = 20,
    value_label_font_size = 30,
    background='rgba(27, 143, 206, 0.17)',
    plot_background='transparent',
    foreground='#fff',
    foreground_strong='rgba(27, 143, 206, 0.17)',
    foreground_subtle='##1e6992',
    opacity='.8',
    opacity_hover='0',
    transition='400ms ease-in',
    )
"""Apply class methods to filter bug_types"""
pie_chart = pygal.Pie(style=custom_pie_style, legend_at_bottom=True, legend_box_size=18)
pie_chart.y_labels = 2, 4, 6, 8, 10
pie_chart.add('Functional', int(BugTicket.qs_by_bug_type('Functional')))
pie_chart.add('Communication', int(BugTicket.qs_by_bug_type('Communication')))
pie_chart.add('Syntax', int(BugTicket.qs_by_bug_type('Syntax')))
pie_chart.add('Error Notices', int(BugTicket.qs_by_bug_type('Error Notices')))
pie_chart.add('Calculation Errors', int(BugTicket.qs_by_bug_type('Calculation Errors')))
pie_chart.add('Flow Problems', int(BugTicket.qs_by_bug_type('Flow Problems')))
pie_chart_data = pie_chart.render_data_uri()  



"""
Bar Charts for top 3 most upvotes
"""
top_bugs = BugTicket.qs_by_no_upvotes(3)

bar_chart = pygal.HorizontalBar()
bar_chart.title = 'Bugs with the highest # of members upvotes (ie. get it sorted!)'
bar_chart.add(top_bugs[0].title, top_bugs[0].votes)
bar_chart.add(top_bugs[1].title, top_bugs[1].votes)
bar_chart.add(top_bugs[2].title, top_bugs[2].votes)

bar_chart_data = bar_chart.render_data_uri()