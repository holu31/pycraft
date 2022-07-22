from ursina import *

class Block(Button):
    def __init__(self, position=(0, 0, 0), texture='textures/blocks/dirt'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color = color.light_gray,
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                block = Block(position=self.position + mouse.normal)
            elif key == 'left mouse down':
                destroy(self)