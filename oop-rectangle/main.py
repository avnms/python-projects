import arcade


COLOR_PALETTE = [
    arcade.color.BLACK,
    arcade.color.LIGHT_GRAY,
    arcade.color.LIGHT_CRIMSON,
    arcade.color.LIGHT_BLUE,
    arcade.color.LIGHT_CORAL,
    arcade.color.LIGHT_CYAN,
    arcade.color.LIGHT_GREEN,
    arcade.color.LIGHT_YELLOW,
    arcade.color.LIGHT_PASTEL_PURPLE,
    arcade.color.LIGHT_SALMON,
    arcade.color.LIGHT_TAUPE,
    arcade.color.LIGHT_SLATE_GRAY,
]


class Rectangle:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        pen_color: tuple = COLOR_PALETTE[0],
        fill_color: tuple = COLOR_PALETTE[1],
        dir_x: int = 1,
        dir_y: int = 1,
        speed_x: int = 1,
        speed_y: int = 1,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pen_color = pen_color
        self.fill_color = fill_color
        self.dir_x = 1 if dir_x > 0 else -1
        self.dir_y = 1 if dir_y > 0 else -1
        self.speed_x = speed_x
        self.speed_y = speed_y

    def set_pen_color(self, color: tuple) -> Rectangle:
        self.pen_color = color
        return self

    def set_fill_color(self, color: tuple) -> Rectangle:
        self.fill_color = color
        return self

    def draw(self):
        arcade.draw_xywh_rectangle_filled(
            self.x,
            self.y,
            self.width,
            self.height,
            self.fill_color,
        )

        arcade.draw_xywh_rectangle_outline(
            self.x,
            self.y,
            self.width,
            self.height,
            self.pen_color,
            3,
        )
