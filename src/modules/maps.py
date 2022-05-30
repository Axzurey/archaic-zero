colorNameConversion = {
    'backgroundColor': 'normal_bg',
    "backgroundColorHover":"hovered_bg",
    "backgroundColordisabled":"disabled_bg",
    'textColor': 'normal_text',
    "textColorHover":"hovered_text",
    "textColorDisabled":"selected_text",
    'borderColor': 'normal_border',
    'borderColorHover': 'hovered_border',
    'borderColorDisabled': 'disabled_border',
}

colorNameConversionInverse = {}

for key, value in colorNameConversion.items():
    colorNameConversionInverse[value] = key