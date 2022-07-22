from panda3d.core import DirectionalLight
from ursina import Entity

class SunLight(Entity):
    def __init__(self, direction, resolution):
        super().__init__()

        dlight = DirectionalLight("sun")
        dlight.setShadowCaster(True, resolution, resolution)

        lens = dlight.getLens()
        lens.setNearFar(-80, 40)
        lens.setFilmSize((60, 60))

        self.dlnp = render.attachNewNode(dlight)
        self.dlnp.lookAt(direction)
        render.setLight(self.dlnp)