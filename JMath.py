class trapeze:

    def surface(middle_line: float, height: float):
        return middle_line * height

    def height_or_middle_line(middle_line_or_height: float, surface: float):
        return surface / middle_line_or_height

    def middle_line(first_line: float, second_line: float):
        return (first_line + second_line) / 2


class parallelogram:

    def surface(base_line: float, height: float):
        return base_line * height

    def height_or_base_line(base_line_or_height: float, surface: float):
        return surface / base_line_or_height


class triangle:

    def surface(base_line: float, height: float):
        return (base_line * height) / 2

    def height_or_base_line(base_line_or_height: float, surface: float):
        return surface / base_line_or_height


class rectangle:

    def surface(top_or_bottom: float, right_or_left: float):
        return top_or_bottom * right_or_left

    def side(surface: float, other_side: float):
        return surface / other_side
