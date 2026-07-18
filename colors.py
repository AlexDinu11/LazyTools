import math

HEX_CODE = {
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}

def tuple_to_list(tuple):
    copy = tuple
    list = []
    for i in copy:
        list.append(i)
    return list

def detect_type(color):
    if isinstance(color, str):
        color_type = "hex"
    elif isinstance(color, tuple):
        color_type = "tuple_rgb"
    else:
        color_type = "rgb"

    return color_type

def convert(current_value, target_format = "hex"):
    if target_format in ("rgb", "tuple_rgb"):
        if detect_type(current_value) == "rgb":
            return current_value
        elif detect_type(current_value) == "tuple_rgb":
            return tuple_to_list(current_value)

        rgb = []
        rgb_hex = []
        current_value = current_value.removeprefix("#").lower()
        for i in range(3):
            rgb_hex.append(current_value[i*2:i*2+2])

        for rgb_index in range(3):
            for i in range(2):
                if rgb_hex[rgb_index][i].isdigit():
                    deserialized = int(rgb_hex[rgb_index][i])
                else:
                    deserialized = HEX_CODE[rgb_hex[rgb_index][i]]

                if i == 0:
                    value = deserialized * 16
                else:
                    value = value + deserialized

            rgb.append(value)

        return rgb
    else:
        if isinstance(current_value, str):
            return current_value

        hex_color = "#"
        for i in current_value:
            if i // 16 > 9:
                hex_color = hex_color + HEX_CODE[i // 16]
            else:
                hex_color = hex_color + str(i // 16)
            if i % 16 > 9:
                hex_color = hex_color + HEX_CODE[i % 16]
            else:
                hex_color = hex_color + str(i % 16)

        return hex_color

def change_color(color, value1: int, value2: int = None, value3: int  = None):
    """Change a color either by lightening or darkening it (use 1 value) or change each RGB value of it (use at least 2 values)"""
    before = color
    color_type = detect_type(color)
    color = convert(color, "rgb")

    if value2 is None and value3 is None:
        for i, e in enumerate(color):
            color[i] = color[i] + value1
    else:
        changes = [value1, value2, value3]
        for i, e in enumerate(color):
            color[i] = max(0, min(e + changes[i], 255))

    color = convert(color, color_type)
    return color

def blend(color1, color2, ratio: float):
    color_type = detect_type(color1)
    color1 = convert(color1, "rgb")
    color2 = convert(color2, "rgb")
    if ratio > 1:
        ratio /= 100

    color = []
    for i in range(3):
        color.append(math.floor(color1[i] + (color2[i] - color1[i]) * ratio))

    color = convert(color, color_type)
    return color

def gradient(start, end, steps):
    gradient_list = []

    for i in range(steps):
        ratio = i / (steps - 1)
        gradient_list.append(blend(start, end, ratio))

    return gradient_list

print(detect_type((128, 256, 128)))
