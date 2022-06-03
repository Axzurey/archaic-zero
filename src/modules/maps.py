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

miscNameConversion = {
    'shape': 'shape',
    'cornerRadius': 'shape_corner_radius',
    'borderWidth': 'border_width',
    'shadowWidth': 'shadow_width',
    'textAlignH': 'text_horiz_alignment',
    'textAlignV': 'text_vert_alignment',
}

miscNameConversionInverse = {}

for key, value in miscNameConversion.items():
    miscNameConversionInverse[value] = key

fontNameConversion = {
    'font': 'name',
    'fontSize': 'size'
}

fontNameConversionInverse = {}

for key, value in fontNameConversion.items():
    fontNameConversionInverse[value] = key