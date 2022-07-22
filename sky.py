from ursina import *
from ursina.shaders import unlit_shader

class Sky(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=render, name='sky', model='sky_dome', texture='sky_default', scale=9900, shader=unlit_shader)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.world_position = camera.world_position