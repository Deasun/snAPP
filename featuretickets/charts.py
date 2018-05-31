import pygal
from pygal.style import Style
from .models import FeatureTicket

"""
Style pygal chart for featureticket list
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

"""Apply class methods to filter current & completed FeatureTicket chart data"""
line_chart.add('Active', [
     int(FeatureTicket.qs_active_features(0)),
     int(FeatureTicket.qs_active_features(7)),
     int(FeatureTicket.qs_active_features(30)),
         ], dots_size=6)
line_chart.add('Completed', [
     int(FeatureTicket.qs_complete_features(0)),
     int(FeatureTicket.qs_complete_features(7)),         
     int(FeatureTicket.qs_complete_features(30)),
         ], dots_size=6)
chart_data = line_chart.render_data_uri()    


"""
Half-Pie chart for feature_types
"""
custom_pie_style = Style(
    font_family='googlefont:Anton',
    legend_font_size = 20,
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
    )
"""Apply class methods to filter feature_types"""
pie_chart = pygal.Pie(half_pie=True, style=custom_pie_style, legend_at_top=True, legend_box_size=18)
pie_chart.title = 'Feature Reports Received'
pie_chart.add('Functional', int(FeatureTicket.qs_by_feature_type('Functional')))
pie_chart.add('Communication', int(FeatureTicket.qs_by_feature_type('Communication')))
pie_chart.add('Syntax', int(FeatureTicket.qs_by_feature_type('Syntax')))
pie_chart.add('Error Notices', int(FeatureTicket.qs_by_feature_type('Error Notices')))
pie_chart.add('Calculation Errors', int(FeatureTicket.qs_by_feature_type('Calculation Errors')))
pie_chart.add('Flow Problems', int(FeatureTicket.qs_by_feature_type('Flow Problems')))
pie_chart_data = pie_chart.render_data_uri()  
