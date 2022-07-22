from ursina import *
from player import Player
from block import Block
from settings import *

blocks = []

app = Ursina()
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