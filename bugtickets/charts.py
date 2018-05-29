import pygal
from pygal.style import Style

"""
Style pygal chart for view
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
