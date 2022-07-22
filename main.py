from ursina import *
from player import Player
from block import Block
from sky import Sky
from sun import SunLight
from settings import *

blocks = []

app = Ursina()
sun = SunLight(direction = (-0.7, -0.9, 0.5), resolution = 2048)
ambient = AmbientLight(color = Vec4(0.5, 0.55, 0.66, 0) * 0.75)
render.setShaderAuto()
sky = Sky(texture='sky0')
window.fullscreen = FULLSCREEN
window.size = (WIDTH,HEIGHT)
window.fps_counter.enabled = False
window.title = 'RuMine'
window.exit_button.visible = False

for x in range(16):
    for z in range(16):
        blocks.append(Block((x, 0, z)))

player = Player()

app.run()