import configparser
config = configparser.ConfigParser()
config.read('settings.ini')

FULLSCREEN = config.getboolean('window', 'fullscreen')
WIDTH = config.getint('window', 'resolution_width')
HEIGHT = config.getint('window', 'resolution_height')
FOV = config.getint('player', 'fov')
SHADERS = config.getboolean('window', 'shaders')