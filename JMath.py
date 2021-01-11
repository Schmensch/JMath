class JMath:
    class trapeze:

        @staticmethod
        def surface(middle_line: float, height: float):
            return middle_line * height

        @staticmethod
        def height_or_middle_line(middle_line_or_height: float, surface: float):
            return surface / middle_line_or_height

        @staticmethod
        def middle_line(first_line: float, second_line: float):
            return (first_line + second_line) / 2

    class parallelogram:

        @staticmethod
        def surface(base_line: float, height: float):
            return base_line * height

        @staticmethod
        def height_or_base_line(base_line_or_height: float, surface: float):
            return surface / base_line_or_height

    class triangle:

        @staticmethod
        def surface(base_line: float, height: float):
            return (base_line * height) / 2

        @staticmethod
        def height_or_base_line(base_line_or_height: float, surface: float):
            return surface / base_line_or_height

    class rectangle:

        @staticmethod
        def surface(top_or_bottom: float, right_or_left: float):
            return top_or_bottom * right_or_left

        @staticmethod
        def side(surface: float, other_side: float):
            return surface / other_side
