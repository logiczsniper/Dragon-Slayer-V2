#Imports
import pygame as pg, sys
import time
import random

#Activate Pygame
pg.init()

#Useful definitions
tile_size = 80
MAPWIDTH = 14
MAPHEIGHT = 11
smallText = pg.font.Font('C:/Users/lczer/Desktop/Dragon Slayer V2/PressStart2P.ttf', 17)
largeText = pg.font.Font('C:/Users/lczer/Desktop/Dragon Slayer V2/PressStart2P.ttf', 55)
GAMEDISPLAY = pg.display.set_mode((MAPWIDTH * tile_size, MAPHEIGHT * tile_size))
event = pg.event.poll()
clock = pg.time.Clock()
FPS = 20

#Groups
all_sprites = pg.sprite.Group()
walls = pg.sprite.Group()
bats = pg.sprite.Group()
slimes = pg.sprite.Group()
character = pg.sprite.Group()
bullets = pg.sprite.Group()
friendly_one = pg.sprite.Group()
friendly_two = pg.sprite.Group()
deers = pg.sprite.Group()
wolves = pg.sprite.Group()
dragons = pg.sprite.Group()
fireballs = pg.sprite.Group()
starterdragon = pg.sprite.Group()
health = pg.sprite.Group()
healthbox = pg.sprite.Group()

#Screens
pause = False
death = False
victory = False
controls = False

#Basic Widths + Heights
display_width = 1120
display_height = 880

#Colours
black = (0, 0, 0)
gray = (50, 50, 50)
blue = (0, 206, 209)
hoverblue = (95, 158, 160)
royalblue = (0, 78, 204)
healthred = (175, 14, 14)
truegray = (127, 132, 140)


#Image Loader
def load_image(name):
    image = pg.image.load('Images/' + name + '.png').convert_alpha()
    return image

#Health Images
healthstatus = load_image('healthbar')
healthcontainer = load_image('healthcontainer')
healthboximg = load_image('healthupgrade')

#Animation Images
characterssheet = load_image('spritesheet')
magic = load_image('magic')
magictwo = load_image('magictwo')
fire = load_image('fireball')
standingsprite = load_image('standingsprite')
walkingsprite = load_image('walkingsprite')
mobsprite = load_image('batsprite')
slime = load_image('slimesheet')
deer = load_image('deer')
wolf = load_image('wolf')
dragon = load_image('dragonspritesheet')

#Smoke Images
smokeone = load_image('smokeone')
smoketwo = load_image('smoketwo')
smokethree = load_image('smokethree')
smokefour = load_image('smokefour')
smokefive = load_image('smokefive')
smokesix = load_image('smokesix')

#Intro Images
dragonstand = load_image('dragonstanding')

dragonhalf = load_image('dragonhalf')
dragonclosed = load_image('dragonclosed')
dragonopen = load_image('dragonopen')
son = load_image('son')
doorone = load_image('doorone')
doortwo = load_image('doortwo')
doorthree = load_image('doorthree')
doorfour = load_image('doorfour')
mage = load_image('mage')
firstpicture = load_image('firstpicture')
holdwand = load_image('holdwand')
standingspritetwo = load_image('standingspriteclosedeyes')

#Background Images
bgstart = load_image('bgstart')
trophy = load_image('trophy')
deathimg = load_image('death')
scroll = load_image('scroll')

#TileMap Images
LONGGRASS = load_image('grassytile')
STUMP = load_image('stumptile')
CAVEFLOOR = load_image('cavefloor')
PATHONE = load_image('horizontalpath')
PATHTWO = load_image('pathintersection')
PATHTHREE = load_image('verticalpath')
PATHFOUR = load_image('downintersection')
PATHFIVE = load_image('endtile')
PATHSIX = load_image('leftintersection')
PATHSEVEN = load_image('leftuppath')
PATHEIGHT = load_image('upintersection')
PATHNINE = load_image('uprightpath')
PATHTEN = load_image('downrightpath')
PATHELEVEN = load_image('rightintersection')
PATHTWELVE = load_image('tiles')
CAVEWALL = load_image('cavewall')
CAVEROCK = load_image('caverock')
WATER = load_image('watertile')
WATERTWO = load_image('waterbottom')
WATERTHREE = load_image('waterleft')
WATERFOUR = load_image('waterright')
WATERFIVE = load_image('waterbottomleftright')
WATERSIX = load_image('waterbottomright')
WATERSEVEN = load_image('waterbottomtopright')
WATEREIGHT = load_image('waterleftbottom')
WATERNINE = load_image('waterlefttop')
WATERTEN = load_image('waterlefttopbottom')
WATERELEVEN = load_image('watertop')
WATERTWELVE = load_image('watertopright')
WATERTHIRTEEN = load_image('waterleftright')
BRIDGE = load_image('bridgetile')
GRASS = load_image('grasstile')
HOUSE = load_image('housetile')
ROCK = load_image('rocktile')
ROCKTWO = load_image('rocktiletwo')
TREE = load_image('treetile')
STAIR = load_image('staircasetile')
CAVESTAIR = load_image('cavestair')
DARKTILE = load_image('darktile')
DARKTOP = load_image('darktop')
DARKLEFT = load_image('darkleft')
DARKRIGHT = load_image('darkright')
CAVEROCKTWO = load_image('caverocktwo')
CAVEWALLTWO = load_image('cavewalltwo')
SAND = load_image('sandtile')
SANDROCKS = load_image('sandrocks')
SANDSHROOMONE = load_image('sandshroomone')
SANDSHROOMTWO = load_image('sandshroomtwo')
SANDSHROOMTHREE = load_image('sandshroomthree')
SNOW = load_image('snowtile')
SNOWTWO = load_image('snowtwo')
SNOWTHREE = load_image('snowthree')
SNOWTREE = load_image('snowtree')
SNOWROCK = load_image('snowrock')
SNOWTRUNK = load_image('snowtrunk')
SNOWFOUR = load_image('snowfour')

#Sound loader
def load_sound(name):
    sound = pg.mixer.Sound('Sounds/' + name)
    return sound

#Songs
global songs
songs = ['Sounds/Adventure_Meme.ogg', 'Sounds/accident.ogg', 'Sounds/jatatap.ogg', 'Sounds/zizibum.ogg', 'Sounds/cave.ogg', 'Sounds/introsong.ogg']
pg.mixer.music.set_volume(0.215)

#Sound Effects
global buttonsound, deathsound, magicsound, walkingsound, walkingtwosound, hitsound, playerhitsound, pauseinsound, pauseoutsound, upgradesound
batsound = load_sound('bat.ogg')
buttonsound = load_sound('buttonsound.wav')
buttonhoversound = load_sound('overbuttonsound.wav')
deathsound = load_sound('death2.ogg')
deersound = load_sound('deer.ogg')
dragonsound = load_sound('dragon.ogg')
magicsound = load_sound('magicsound.wav')
slimesound = load_sound('slime.ogg')
walkingsound = load_sound('walkingsound.wav')
walkingtwosound = load_sound('walkingtwosound.wav')
wolfsound = load_sound('wolf.ogg')
hitsound = load_sound('hitsound.wav')
pauseinsound = load_sound('pausein.wav')
pauseoutsound = load_sound('pauseout.wav')
upgradesound = load_sound('healthsound.wav')
playerhitsound = load_sound('playerhit.wav')

#Volume for Sound Effects
walkingsound.set_volume(0.04)
walkingtwosound.set_volume(0.05)
buttonsound.set_volume(0.13)
buttonhoversound.set_volume(0.15)
magicsound.set_volume(0.15)
pauseinsound.set_volume(0.85)
pauseoutsound.set_volume(0.85)
upgradesound.set_volume(0.9)
playerhitsound.set_volume(0.2)
hitsound.set_volume(0.2)

#Tile association numbers
LLONGGRASS = 0
SSTUMP = 1
CCAVEFLOOR = 2
CCAVEWALL = 3
CCAVEROCK = 4
BWATER = 5
GGRASS = 6
BHOUSE = 7
BROCK = 8
GTREE = 9
DSTAIR = 10
PPATHONE = 11
PPATHTWO = 12
PPATHTHREE = 13
WWATERTWO = 14
WWATERTHREE = 15
WWATERFOUR = 16
WWATERFIVE = 17
RROCKTWO = 18
PPATHFOUR = 19
PPATHFIVE = 20
PPATHSIX = 21
PPATHSEVEN = 22
PPATHEIGHT = 23
PPATHNINE = 24
PPATHTEN = 25
WWATERSIX = 26
WWATERSEVEN = 27
WWATEREIGHT = 28
WWATERNINE = 29
BBRIDGE = 30
WWATERTEN = 31
WWATERELEVEN = 32
WWATERTWELVE = 33
WWATERTHIRTEEN = 34
CCAVESTAIR = 35
DDARKTILE = 36
DDARKTOP = 37
DDARKLEFT = 38
DDARKRIGHT = 39
CCAVEROCKTWO = 40
CCAVEWALLTWO = 41
SSAND = 42
SSNOW = 43
SSANDSHROOMONE = 44
SSANDSHROOMTWO = 45
SSANDSHROOMTHREE = 46
SSANDROCKS = 47
SSNOWTWO = 48
SSNOWTHREE = 49
SSNOWTREE = 50
SSNOWROCK = 51
SSNOWTRUNK = 52
SSNOWFOUR = 53
PPATHELEVEN = 54
PPATHTWELVE = 55

#All Tiles
tiles = {
    LLONGGRASS : LONGGRASS,
    SSTUMP : STUMP,
    CCAVEFLOOR : CAVEFLOOR,
    CCAVEWALL : CAVEWALL,
    CCAVEROCK : CAVEROCK,
    BWATER : WATER,
    GGRASS : GRASS,
    BHOUSE : HOUSE,
    BROCK : ROCK,
    GTREE : TREE,
    DSTAIR : STAIR,
    PPATHONE : PATHONE,
    PPATHTWO : PATHTWO,
    PPATHTHREE : PATHTHREE,
    WWATERTWO : WATERTWO,
    WWATERTHREE : WATERTHREE,
    WWATERFOUR : WATERFOUR,
    WWATERFIVE : WATERFIVE,
    RROCKTWO : ROCKTWO,
    PPATHFOUR : PATHFOUR,
    PPATHFIVE : PATHFIVE,
    PPATHSIX : PATHSIX,
    PPATHSEVEN : PATHSEVEN,
    PPATHEIGHT : PATHEIGHT,
    PPATHNINE : PATHNINE,
    PPATHTEN : PATHTEN,
    WWATERSIX : WATERSIX,
    WWATERSEVEN : WATERSEVEN,
    WWATEREIGHT : WATEREIGHT,
    WWATERNINE : WATERNINE,
    BBRIDGE : BRIDGE,
    WWATERTEN : WATERTEN,
    WWATERELEVEN : WATERELEVEN,
    WWATERTWELVE : WATERTWELVE,
    WWATERTHIRTEEN : WATERTHIRTEEN,
    CCAVESTAIR : CAVESTAIR,
    DDARKTILE : DARKTILE,
    DDARKTOP : DARKTOP,
    DDARKLEFT : DARKLEFT,
    DDARKRIGHT : DARKRIGHT,
    CCAVEROCKTWO : CAVEROCKTWO,
    CCAVEWALLTWO : CAVEWALLTWO,
    SSAND : SAND,
    SSNOW : SNOW,
    SSANDSHROOMONE : SANDSHROOMONE,
    SSANDSHROOMTWO : SANDSHROOMTWO,
    SSANDSHROOMTHREE : SANDSHROOMTHREE,
    SSANDROCKS : SANDROCKS,
    SSNOWTWO : SNOWTWO,
    SSNOWTHREE : SNOWTHREE,
    SSNOWTREE : SNOWTREE,
    SSNOWROCK : SNOWROCK,
    SSNOWTRUNK : SNOWTRUNK,
    SSNOWFOUR : SNOWFOUR,
    PPATHELEVEN : PATHELEVEN,
    PPATHTWELVE : PATHTWELVE
    }

#First Map
tilemapone = [
    [GTREE, WWATERTHREE, BWATER, WWATERFOUR, GTREE, RROCKTWO, PPATHTHREE, BROCK, GTREE, RROCKTWO, GTREE, BROCK, RROCKTWO, RROCKTWO],
    [WWATERNINE, BWATER, BWATER, BWATER, WWATERSEVEN, GGRASS, PPATHNINE, PPATHTWELVE, SSTUMP, GTREE, GGRASS, GTREE, SSTUMP, BROCK],
    [WWATEREIGHT, BWATER, WWATERTWO, WWATERSIX, LLONGGRASS, GGRASS, BHOUSE, PPATHTHREE, GGRASS, LLONGGRASS, GGRASS, LLONGGRASS, GTREE, BROCK],
    [RROCKTWO, WWATERFIVE, SSTUMP, GGRASS, GTREE, GGRASS, PPATHNINE, PPATHSIX, GGRASS, BHOUSE, GGRASS, BHOUSE, LLONGGRASS, RROCKTWO],
    [GGRASS, LLONGGRASS, BHOUSE, LLONGGRASS, GGRASS, BHOUSE, LLONGGRASS, PPATHTHREE, GGRASS, PPATHTHREE, LLONGGRASS, PPATHTHREE, BROCK, LLONGGRASS],
    [PPATHONE, PPATHONE, PPATHEIGHT, PPATHONE, PPATHFOUR, PPATHEIGHT, PPATHONE, PPATHTWO, PPATHONE, PPATHEIGHT, PPATHFOUR, PPATHEIGHT, PPATHONE, PPATHONE],
    [LLONGGRASS, GGRASS, SSTUMP, BHOUSE, PPATHTHREE, SSTUMP, LLONGGRASS, PPATHTHREE, GGRASS, LLONGGRASS, PPATHTHREE, GGRASS, LLONGGRASS, GGRASS],
    [RROCKTWO, GTREE, LLONGGRASS, PPATHNINE, PPATHSEVEN, GGRASS, GGRASS, PPATHTHREE, GGRASS, GGRASS, PPATHTHREE, BHOUSE, GTREE, GTREE],
    [BROCK, BROCK, GTREE, GGRASS, LLONGGRASS, GGRASS, GGRASS, PPATHTHREE, BHOUSE, LLONGGRASS, PPATHNINE, PPATHSEVEN, GGRASS, GTREE],
    [BROCK, BROCK, RROCKTWO, LLONGGRASS, GGRASS, GTREE, GTREE, PPATHELEVEN, PPATHSEVEN, GTREE, LLONGGRASS, GGRASS, LLONGGRASS, RROCKTWO],
    [RROCKTWO, BROCK, BROCK, RROCKTWO, GTREE, GTREE, GGRASS, PPATHTHREE, GTREE, GGRASS, GTREE, RROCKTWO, BROCK, BROCK]
]

#Second Map
tilemaptwo = [
    [GTREE, BROCK, WWATERTEN, WWATERELEVEN, WWATERELEVEN, WWATERTWELVE, GGRASS, GTREE, RROCKTWO, GTREE, BROCK, GTREE, RROCKTWO, BROCK],
    [RROCKTWO, GTREE, GTREE, WWATERTHREE, BWATER, WWATERSIX, GTREE, GGRASS, LLONGGRASS, GGRASS, GGRASS, LLONGGRASS, BROCK, BROCK],
    [RROCKTWO, GTREE, GGRASS, WWATEREIGHT, WWATERFOUR, GGRASS, LLONGGRASS, GGRASS, GGRASS, GGRASS, BROCK, GGRASS, GGRASS, RROCKTWO],
    [GTREE, LLONGGRASS, GGRASS, GGRASS, BBRIDGE, GGRASS, GGRASS, GGRASS, LLONGGRASS, GGRASS, GGRASS, GGRASS, RROCKTWO, GTREE],
    [RROCKTWO, GGRASS, GGRASS, GGRASS, WWATERTHIRTEEN, GGRASS, GGRASS, GGRASS, GTREE, GGRASS, RROCKTWO, LLONGGRASS, BROCK, GTREE],
    [GTREE, LLONGGRASS, GGRASS, WWATERNINE, WWATERFOUR, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GTREE],
    [DSTAIR, GGRASS, GGRASS, WWATERTHREE, WWATERFOUR, GGRASS, GTREE, GGRASS, GGRASS, GGRASS, GTREE, GGRASS, GTREE, GGRASS],
    [RROCKTWO, GTREE, WWATERNINE, BWATER, WWATERSIX, GGRASS, GGRASS, GGRASS, GGRASS, LLONGGRASS, GGRASS, BROCK, GGRASS, BROCK],
    [BROCK, GTREE, WWATERTHREE, WWATERSIX, GGRASS, GTREE, GGRASS, LLONGGRASS, GGRASS, GGRASS, GGRASS, BROCK, LLONGGRASS, GTREE],
    [RROCKTWO, WWATERNINE, WWATERFOUR, GTREE, LLONGGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, LLONGGRASS, GGRASS, BROCK, RROCKTWO],
    [WWATERNINE, BWATER, WWATERFOUR, RROCKTWO, GTREE, GTREE, GGRASS, GGRASS, RROCKTWO, BROCK, GTREE, GGRASS, BROCK, BROCK]
]

#Third Map
tilemapthree = [
    [GTREE, GTREE, GTREE, RROCKTWO, GTREE, GTREE, GTREE, GTREE, GTREE, RROCKTWO, GTREE, GTREE, BROCK, GTREE],
    [GTREE, GTREE, BROCK, GTREE, GTREE, LLONGGRASS, GGRASS, GGRASS, LLONGGRASS, LLONGGRASS, GTREE, GTREE, GTREE, GTREE],
    [RROCKTWO, GTREE, GTREE, GGRASS, GGRASS, LLONGGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GTREE, GTREE, GTREE],
    [GTREE, GTREE, LLONGGRASS, LLONGGRASS, GGRASS, GGRASS, GGRASS, LLONGGRASS, GGRASS, LLONGGRASS, GGRASS, BROCK, GTREE, RROCKTWO],
    [LLONGGRASS, GTREE, GGRASS, LLONGGRASS, GGRASS, GGRASS, LLONGGRASS, LLONGGRASS, GGRASS, GGRASS, BROCK, BROCK, RROCKTWO, LLONGGRASS],
    [GGRASS, LLONGGRASS, GGRASS, GGRASS, LLONGGRASS, GGRASS, GGRASS, GGRASS, GGRASS, LLONGGRASS, GGRASS, LLONGGRASS, BROCK, GGRASS],
    [GGRASS, LLONGGRASS, GGRASS, GGRASS, LLONGGRASS, LLONGGRASS, LLONGGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GTREE, LLONGGRASS],
    [BROCK, GGRASS, LLONGGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, LLONGGRASS, GTREE, GTREE, GTREE],
    [GTREE, GTREE, GGRASS, LLONGGRASS, GGRASS, LLONGGRASS, GGRASS, GGRASS, LLONGGRASS, GGRASS, GGRASS, BROCK, GTREE, BROCK],
    [RROCKTWO, GTREE, GTREE, GGRASS, RROCKTWO, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GTREE, GTREE, GTREE, GTREE],
    [GTREE, GTREE, GTREE, GTREE, GTREE, GTREE, GTREE, BROCK, BROCK, GTREE, GTREE, RROCKTWO, GTREE, GTREE]
]

#Fourth Map
tilemapfour = [
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, CCAVEWALLTWO, CCAVEWALL, CCAVEWALLTWO, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKRIGHT, CCAVEFLOOR, CCAVEFLOOR, CCAVEFLOOR, DDARKLEFT, DDARKTILE, DDARKTILE, DDARKTILE],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKRIGHT, CCAVEROCKTWO, CCAVEFLOOR, CCAVEFLOOR, DDARKLEFT, DDARKTILE, DDARKTILE, DDARKTILE],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKRIGHT, CCAVEFLOOR, CCAVEFLOOR, CCAVEFLOOR, DDARKLEFT, DDARKTILE, DDARKTILE, DDARKTILE],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, CCAVEWALLTWO, CCAVEWALL, CCAVEWALLTWO, CCAVEFLOOR, CCAVEFLOOR, CCAVEFLOOR, CCAVEWALL, CCAVEWALL, CCAVEWALLTWO, CCAVEWALL],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKRIGHT, CCAVEFLOOR, CCAVEFLOOR, CCAVEFLOOR, CCAVEROCKTWO, CCAVEFLOOR, CCAVEROCK, CCAVEFLOOR, CCAVEFLOOR, CCAVEFLOOR, CCAVESTAIR],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKRIGHT, CCAVEFLOOR, CCAVEROCK, CCAVEFLOOR, CCAVEFLOOR, CCAVEFLOOR, CCAVEFLOOR, CCAVEFLOOR, CCAVEROCK, CCAVEFLOOR, CCAVEROCK],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTOP, DDARKTOP, DDARKTOP, DDARKTOP, DDARKTOP, DDARKTOP, DDARKTOP, DDARKTOP, DDARKTOP, DDARKTOP],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE],
    [DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE, DDARKTILE]
]

#Fifth Map
tilemapfive = [
    [SSNOWTREE, SSNOWTREE, SSNOWROCK, SSNOWROCK, SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWROCK, SSNOWROCK, SSNOWTREE, SSNOWTREE, SSNOWTREE],
    [SSNOW, SSNOWTHREE, SSNOW, SSNOWTREE, SSNOW, SSNOWTRUNK, SSNOWTREE, SSNOW, SSNOW, SSNOWTREE, SSNOW, SSNOWTREE, SSNOW, SSNOW],
    [SSNOW, SSNOWROCK, SSNOW, SSNOWTREE, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOWTRUNK, SSNOWTHREE, SSNOWTRUNK, SSNOW, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOWTRUNK, SSNOW, SSNOW, SSNOWTWO, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOWTHREE],
    [SSNOWTWO, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOW, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOWTHREE, SSNOWROCK, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW],
    [SSNOWTRUNK, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOWTRUNK, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTRUNK, SSNOWTRUNK, SSNOWTWO, SSNOW],
    [SSNOWTHREE, SSNOWTRUNK, SSNOWROCK, SSNOWTRUNK, SSNOWTWO, SSNOWTREE, SSNOW, SSNOWTRUNK, SSNOW, SSNOWROCK, SSNOWROCK, SSNOW, SSNOW, SSNOWTHREE],
    [SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWTREE, SSNOWTREE, SSNOWROCK, SSNOWROCK, SSNOWTREE, SSNOW, SSNOWTREE, SSNOWTREE, SSNOWROCK]
]

#Sixth Map
tilemapsix = [
    [SSAND, SSAND, SSANDSHROOMONE, SSAND, SSAND, SSANDROCKS, SSANDROCKS, SSANDROCKS, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND],
    [SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSANDSHROOMTWO, SSANDROCKS, SSAND, SSANDSHROOMTHREE, SSANDSHROOMTWO, SSANDSHROOMONE, SSAND, SSANDSHROOMTHREE],
    [SSANDSHROOMTHREE, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSANDROCKS, SSAND, SSAND, SSAND, SSANDROCKS, SSAND, SSAND],
    [SSAND, SSANDROCKS, SSAND, SSAND, SSAND, SSAND, SSANDROCKS, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND],
    [SSAND, SSAND, SSAND, SSAND, SSANDSHROOMTHREE, SSAND, SSANDROCKS, SSANDSHROOMONE, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND],
    [SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSANDROCKS, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND],
    [SSAND, SSANDSHROOMTWO, SSAND, SSAND, SSAND, SSAND, SSANDSHROOMTHREE, SSANDROCKS, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND],
    [SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSANDROCKS, SSAND, SSAND, SSANDROCKS, SSAND, SSANDROCKS, SSAND],
    [SSAND, SSAND, SSANDSHROOMONE, SSANDROCKS, SSANDSHROOMTWO, SSAND, SSAND, SSAND, SSAND, SSAND, SSANDSHROOMTWO, SSAND, SSAND, SSANDSHROOMTHREE],
    [SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSANDROCKS, SSAND, SSAND, SSANDSHROOMONE, SSAND, SSAND, SSAND, SSAND],
    [SSANDSHROOMTHREE, SSAND, SSAND, SSAND, SSAND, SSAND, SSAND, SSANDROCKS, SSAND, SSAND, SSAND, SSANDSHROOMTHREE, SSAND, SSAND]
]

#Seventh Map
tilemapseven = [
    [SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWTREE, SSNOWTREE, SSNOWROCK, SSNOWROCK, SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWTREE, SSNOWTREE],
    [SSNOWTRUNK, SSNOW, SSNOWROCK, SSNOW, SSNOW, SSNOW, SSNOWTWO, SSNOWROCK, SSNOWROCK, SSNOWROCK, SSNOWTWO, SSNOW, SSNOW, SSNOWTRUNK],
    [SSNOW, SSNOWTRUNK, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOWTRUNK, SSNOW],
    [SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOWTRUNK, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOW, SSNOW, SSNOW],
    [SSNOWTHREE, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOWTWO, SSNOW],
    [SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOWTHREE, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE],
    [SSNOW, SSNOWROCK, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOW, SSNOW, SSNOWTRUNK, SSNOW, SSNOWTWO, SSNOWTHREE, SSNOW, SSNOW, SSNOWTHREE, SSNOW],
    [SSNOWTRUNK, SSNOWTREE, SSNOW, SSNOW, SSNOW, SSNOWROCK, SSNOW, SSNOW, SSNOWROCK, SSNOWROCK, SSNOW, SSNOW, SSNOW, SSNOW],
    [SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWTREE, SSNOWTREE, SSNOWTREE, SSNOWROCK, SSNOWROCK, SSNOWTREE, SSNOW, SSNOWTREE, SSNOWROCK, SSNOWTREE, SSNOWROCK]
]

#Eighth Map
tilemapeight = [
    [SSNOW, SSNOWTWO, SSNOW, SSNOWTHREE, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOWTWO, SSNOW],
    [SSNOWTWO, SSNOW, SSNOWTHREE, SSNOW, SSNOWTWO, SSNOWTWO, SSNOW, SSNOWTWO, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOWTWO],
    [SSNOW, SSNOW, SSNOWTHREE, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOWTHREE],
    [SSNOW, SSNOWTHREE, SSNOWTWO, SSNOW, SSNOW, SSNOWFOUR, SSNOWFOUR, SSNOWFOUR, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW],
    [SSNOWTHREE, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWFOUR, SSNOW, SSNOW, SSNOWFOUR, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOWFOUR, SSNOWFOUR, SSNOW, SSNOWFOUR, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWFOUR, SSNOW, SSNOWTWO, SSNOW, SSNOW],
    [SSNOW, SSNOW, SSNOWTWO, SSNOW, SSNOWTWO, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWFOUR, SSNOWTWO, SSNOW, SSNOW, SSNOW],
    [SSNOWTHREE, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWFOUR, SSNOWTWO, SSNOWTWO, SSNOW, SSNOW, SSNOWTHREE],
    [SSNOWTWO, SSNOWTHREE, SSNOW, SSNOWTWO, SSNOWTWO, SSNOWFOUR, SSNOWFOUR, SSNOWFOUR, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOWTWO],
    [SSNOW, SSNOWTWO, SSNOWTHREE, SSNOWFOUR, SSNOWFOUR, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOW, SSNOWTHREE, SSNOWTWO, SSNOW]
]

#Functions
def quitgame():
    pg.quit()
    quit()

def message_display(text, fontsize, timer, colour):
    largeText = pg.font.Font('PressStart2P.ttf', fontsize)
    TextSurf, TextRect = text_objects(text, largeText, colour)
    TextRect.center = ((display_width / 2), 820)
    GAMEDISPLAY.blit(scroll, (0, 740))
    GAMEDISPLAY.blit(TextSurf, TextRect)
    pg.display.update()
    time.sleep(timer - 3.9)

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def intro_images():
    displayBackground(tilemapone)
    GAMEDISPLAY.blit(son, (970, 640))

def more_images():
    GAMEDISPLAY.blit(mage, (855, 640))
    GAMEDISPLAY.blit(firstpicture, (928, 640))
    
def display_image(image, x, y, timer):
        GAMEDISPLAY.blit(image, (x, y))
        pg.display.update()
        time.sleep(timer)

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(GAMEDISPLAY, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            buttonsound.play()
            action()
    else:
        pg.draw.rect(GAMEDISPLAY, ic, (x, y, w, h))
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    GAMEDISPLAY.blit(textSurf, textRect)

def displayBackground(mapnumber):
    walls.empty()
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            GAMEDISPLAY.blit(tiles[mapnumber[row][column]], [column * tile_size, row * tile_size])
            if tiles[mapnumber[row][column]] == HOUSE:
                Wall((column * 80, row * 80), 80, 80, HOUSE)
            if tiles[mapnumber[row][column]] == TREE:
                Wall((column * 80, row * 80), 80, 80, TREE)
            if tiles[mapnumber[row][column]] == ROCK:
                Wall((column * 80, row * 80), 80, 80, ROCK)
            if tiles[mapnumber[row][column]] == ROCKTWO:
                Wall((column * 80, row * 80), 80, 80, ROCKTWO)
            if tiles[mapnumber[row][column]] == WATER:
                Wall((column * 80, row * 80), 80, 80, WATER)
            if tiles[mapnumber[row][column]] == WATERTWO:
                Wall((column * 80, row * 80), 80, 80, WATERTWO)
            if tiles[mapnumber[row][column]] == WATERTHREE:
                Wall((column * 80, row * 80), 80, 80, WATERTHREE)
            if tiles[mapnumber[row][column]] == WATERFOUR:
                Wall((column * 80, row * 80), 80, 80, WATERFOUR)
            if tiles[mapnumber[row][column]] == WATERFIVE:
                Wall((column * 80, row * 80), 80, 80, WATERFIVE)
            if tiles[mapnumber[row][column]] == WATERSIX:
                Wall((column * 80, row * 80), 80, 80, WATERSIX)
            if tiles[mapnumber[row][column]] == WATERSEVEN:
                Wall((column * 80, row * 80), 80, 80, WATERSEVEN)
            if tiles[mapnumber[row][column]] == WATEREIGHT:
                Wall((column * 80, row * 80), 80, 80, WATEREIGHT)
            if tiles[mapnumber[row][column]] == WATERNINE:
                Wall((column * 80, row * 80), 80, 80, WATERNINE)
            if tiles[mapnumber[row][column]] == WATERTEN:
                Wall((column * 80, row * 80), 80, 80, WATERTEN)
            if tiles[mapnumber[row][column]] == WATERELEVEN:
                Wall((column * 80, row * 80), 80, 80, WATERELEVEN)
            if tiles[mapnumber[row][column]] == WATERTWELVE:
                Wall((column * 80, row * 80), 80, 80, WATERTWELVE)
            if tiles[mapnumber[row][column]] == WATERTHIRTEEN:
                Wall((column * 80, row * 80), 80, 80, WATERTHIRTEEN)
            if tiles[mapnumber[row][column]] == CAVEWALL:
                Wall((column * 80, row * 80), 80, 80, CAVEWALL)
            if tiles[mapnumber[row][column]] == CAVEWALLTWO:
                Wall((column * 80, row * 80), 80, 80, CAVEWALLTWO)
            if tiles[mapnumber[row][column]] == DARKTOP:
                Wall((column * 80, row * 80), 80, 80, DARKTOP)
            if tiles[mapnumber[row][column]] == DARKLEFT:
                Wall((column * 80, row * 80), 80, 80, DARKLEFT)
            if tiles[mapnumber[row][column]] == DARKRIGHT:
                Wall((column * 80, row * 80), 80, 80, DARKRIGHT)
            if tiles[mapnumber[row][column]] == CAVEROCK:
                Wall((column * 80, row * 80), 80, 80, CAVEROCK)
            if tiles[mapnumber[row][column]] == CAVEROCKTWO:
                Wall((column * 80, row * 80), 80, 80, CAVEROCKTWO)
            if tiles[mapnumber[row][column]] == SNOWTREE:
                Wall((column * 80, row * 80), 80, 80, SNOWTREE)
            if tiles[mapnumber[row][column]] == SNOWROCK:
                Wall((column * 80, row * 80), 80, 80, SNOWROCK)

#Projectile Classes
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, direct, levelone):
        self.groups = all_sprites, bullets 
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = magic
        self.rect = self.image.get_rect()
        self.rect.x = x + 15
        self.rect.y = y + 30
        self.direction = direct
        self.spawn_time = pg.time.get_ticks()
        if levelone == True:
            self.image = magic
        else:
            self.image = magictwo
        
    def update(self):
        if self.direction == 'left':
            self.rect.x -= 8

        if self.direction == 'right':
            self.rect.x += 8

        if self.direction == 'up':
            self.rect.y -= 8

        if self.direction == 'down':
            self.rect.y += 8
        
        if pg.time.get_ticks() - self.spawn_time > 1150 or self.rect.y < 0 or self.rect.y > display_height or self.rect.x < 0 or self.rect.x > display_width:
            self.kill()

class Fireball(pg.sprite.Sprite):
    def __init__(self, x, y, direct):
        self.groups = all_sprites, fireballs 
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = fire
        self.rect = self.image.get_rect()
        self.rect.x = x + 15
        self.rect.y = y + 30
        self.direction = direct
        self.spawn_time = pg.time.get_ticks()
        
    def update(self):
        if self.direction == 'left':
            self.rect.x -= 8

        if self.direction == 'right':
            self.rect.x += 8

        if self.direction == 'up':
            self.rect.y -= 8

        if self.direction == 'down':
            self.rect.y += 8
        
        if pg.time.get_ticks() - self.spawn_time > 1175 or self.rect.y < 0 or self.rect.y > display_height or self.rect.x < 0 or self.rect.x > display_width:
            self.kill()

#Misc Classes
class Wall(pg.sprite.Sprite):
    def __init__(self, wallpos, w, h, image):
        self.groups = all_sprites, walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = wallpos
        self.rect.width = w
        self.rect.width = h

class SceneBase:

    def __init__(self):
        self.next = self

    def ProcessInput(self):
        pass
    
    def Update(self):
        pass
    
    def Render(self, screen):
        pass
    
    def SwitchToScene(self, next_scene):
        self.next = next_scene
        bullets.empty()
        
    def Terminate(self):
        self.SwitchToScene(None)

#Walking Villager
class FriendlySpriteTwo(pg.sprite.Sprite):
    def __init__(self, position):
        self.groups = all_sprites, friendly_two
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sheet = walkingsprite
        self.sheet.set_clip(pg.Rect(57, 0, 40, 52))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0: (6, 52, 41, 53), 1: (58, 52, 39, 53), 2: (111, 52, 39, 53)}
        self.right_states = {0: (1, 105, 41, 52), 1: (55, 105, 39, 52), 2: (108, 105, 39, 52)}
        self.up_states = {0: (6, 157, 36, 53), 1: (58, 157, 38, 53), 2: (112, 157, 36, 53)}
        self.down_states = {0: (4, 0, 43, 52), 1: (57, 0, 40, 52), 2: (108, 0, 41, 52)}
        self.direction = 'down'
        self.convonum = 0
        self.quest = False
        self.completed = False

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pg.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pg.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction, playerrect):

        if not self.rect.colliderect(playerrect):
            if direction == 'up':
                self.clip(self.up_states)
                self.rect.y -= 3
            if direction == 'down':
                self.clip(self.down_states)
                self.rect.y += 1

            if direction == 'stand_up':
                self.clip(self.down_states[1])
            if direction == 'stand_down':
                self.clip(self.up_states[1])
            
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, direction, playersrect, events, playerquest, firespeed):
        
        self.update('down', playersrect)
        for wall in walls:
            if self.rect.colliderect(wall.rect):    
                if direction == 'up':
                    self.rect.top = wall.rect.bottom
                    self.direction = 'down'
                if direction == 'down':
                    self.rect.bottom = wall.rect.top
                    self.direction = 'up'

        for characterone in character:
            if events.type == pg.MOUSEBUTTONDOWN and self.rect.colliderect(playersrect):
                self.msgtimer = 3.9
                if playerquest == 5:
                    message_display('Are you okay? I heard the news...', 18, 8, black)
                elif self.completed == True:
                    message_display('What do you want?', 19, 6.5, black)
                elif playerquest == 11 and self.quest == True:
                    self.completed = True
                    message_display('Thanks! Here is an upgraded wand! Faster fire rate!', 16, 6.5, black)
                    upgradesound.play()
                else:
                    if self.convonum == 0:
                        message_display('Those stupid slimes!', 19, 5.5, black)
                        self.convonum += 1
                    elif self.convonum == 1:
                        message_display('Go the the eastern plains and kill them-', 17, 7.6, black)
                        self.convonum += 1
                    elif self.convonum == 2:
                        self.quest = True
                        message_display('If you succeed I will give you an award!', 17, 6.5, black)
                        self.convonum += 1
                    elif self.convonum == 3:
                        message_display('What are you doing? Go out and kill the slimes!', 17, 6, black)
                
            elif self.rect.colliderect(playersrect):
                self.msgtimer = 3.91
                message_display('Click the mouse to talk!', 20, self.msgtimer, black)

#Class for the Player!
class Hero(pg.sprite.Sprite):
    def __init__(self, position):
        self.groups = all_sprites, character
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sheet = characterssheet
        self.sheet.set_clip(pg.Rect(55, 0, 47, 52))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.collisionrect = pg.Rect(self.rect.x, self.rect.y + 35, self.rect.width, 17)
        self.location = None
        self.frame = 0
        self.left_states = {0: (1, 52, 45, 53), 1: (54, 52, 44, 53), 2: (106, 52, 45, 53)}
        self.right_states = {0: (7, 105, 44, 52), 1: (59, 105, 44, 52), 2: (112, 105, 44, 52)}
        self.up_states = {0: (8, 157, 43, 53), 1: (61, 157, 42, 53), 2: (113, 157, 43, 53)}
        self.down_states = {0: (3, 0, 44, 52), 1: (55, 0, 47, 52), 2: (108, 0, 46, 52)}
        self.direction = 'down'
        self.last_shot = 0
        self.questlvl = 0
        self.firespeed = 550
        self.wand = 0
        self.health = 900
        self.healthlvl = 0

    def get_location(self):
        return self.location

    def lower_health(self, value):
        playerhitsound.play()
        self.health -= (value + 5)
        
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pg.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pg.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):

        
        if self.questlvl > 3:
            if direction == 'left':
                self.clip(self.left_states)
                self.rect.x -= 7.8
                self.collisionrect.x -= 7.8
            if direction == 'right':
                self.clip(self.right_states)
                self.rect.x += 7.8
                self.collisionrect.x += 7.8
            if direction == 'up':
                self.clip(self.up_states)
                self.rect.y -= 7.8
                self.collisionrect.y -= 7.8
            if direction == 'down':
                self.clip(self.down_states)
                self.rect.y += 7.8
                self.collisionrect.y += 7.8

            if direction == 'stand_left':
                self.clip(self.left_states[1])
            if direction == 'stand_right':
                self.clip(self.right_states[1])
            if direction == 'stand_up':
                self.clip(self.down_states[1])
            if direction == 'stand_down':
                self.clip(self.up_states[1])
            
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event, direction):
        for wall in walls:
            if self.collisionrect.colliderect(wall.rect):
                if direction == 'left':
                    self.collisionrect.left = wall.rect.right
                    self.rect.left = self.collisionrect.left
                if direction == 'right':
                    self.collisionrect.right = wall.rect.left
                    self.rect.right = self.collisionrect.right
                if direction == 'up':
                    self.collisionrect.top = wall.rect.bottom
                    self.rect.top = self.collisionrect.top - 35
                if direction == 'down':
                    self.collisionrect.bottom = wall.rect.top
                    self.rect.bottom = wall.rect.top
        
        if event.type == pg.QUIT:
            quitgame()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                walkingsound.play()
            elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                walkingtwosound.play()
            if event.key == pg.K_LEFT:
                self.update('left')
                self.direction = 'left'
                    
            if event.key == pg.K_RIGHT:
                self.update('right')
                self.direction = 'right'

            if event.key == pg.K_UP:
                self.update('up')
                self.direction = 'up'
                
            if event.key == pg.K_DOWN:
                self.update('down')
                self.direction = 'down'
                
        if event.type == pg.KEYUP:
            walkingsound.stop()
            walkingtwosound.stop()
            if event.key == pg.K_LEFT:
                self.update('stand_left')            
            if event.key == pg.K_RIGHT:
                self.update('stand_right')
            if event.key == pg.K_UP:
                self.update('stand_down')
            if event.key == pg.K_DOWN:
                self.update('stand_up')

    def shoot(self):
        if self.wand == 0:
            bullet = Bullet(self.rect.x, self.rect.y, self.direction, True)
        else:
            bullet = Bullet(self.rect.x, self.rect.y, self.direction, False)

    def setLocation(self, location):
        self.location = location

#Health Classes
class Healthbar(pg.sprite.Sprite):
    def __init__(self, playerhealth, position):
        self.groups = all_sprites, health
        pg.sprite.Sprite.__init__(self, self.groups)
        self.health = playerhealth
        self.image = healthstatus
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.upgradeonce = False
        
    def lower(self, value):
        self.rect.x -= (value * 5)

    def upgrade(self):
        self.rect.x += 28

class HealthBox(pg.sprite.Sprite):
    def __init__(self, position, mode):
        self.groups = all_sprites, healthbox
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = healthboximg
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.mode = mode

    def healthupgrade(self):
        mode = 1
        self.kill()

#Super class for all Enemy Mobs
class EnemyMob(pg.sprite.Sprite):
    def __init__(self):
        pass

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pg.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pg.Rect(clipped_rect))
        return clipped_rect

    def handle_event(self, event, direction, playerrect):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if direction == 'left':
                    self.rect.left = wall.rect.right
                if direction == 'right':
                    self.rect.right = wall.rect.left
                if direction == 'up':
                    self.rect.top = wall.rect.bottom
                if direction == 'down':
                    self.rect.bottom = wall.rect.top

        if self.rect.centery > playerrect.centery and not self.rect.top < playerrect.bottom:
            self.update('up')
            self.direction = 'up'
        elif self.rect.centerx < playerrect.centerx and not self.rect.right > playerrect.left:
            self.update('right')
            self.direction = 'right'
        elif self.rect.centery < playerrect.centery and not self.rect.bottom > playerrect.top:
            self.update('down')
            self.direction = 'down'
        elif self.rect.centerx >= playerrect.centerx and not self.rect.left < playerrect.right:
            self.update('left')
            self.direction = 'left'

        if pg.sprite.spritecollideany(self, bullets, collided = None) != None:
            self.health -= 0.1
            hitsound.play()
        if self.health <= 0:
            if self.deathsound < 2:
                deathsound.play()
                self.deathsound += 1
            self.kill()

    def update(self, direction):

        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= self.movespeed
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += self.movespeed
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= self.movespeed
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += self.movespeed

        if direction == 'stand_down':
            self.clip(self.up_states[1])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

#Inheritance of Enemy Mobs
class Bat(EnemyMob):
    def __init__(self, position, facing):
        self.group = bats
        self.groups = all_sprites, bats
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sheet = mobsprite
        self.sheet.set_clip(pg.Rect(126, 11, 58, 30))
        self.frame = 0
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.left_states = {0: (70, 193, 34, 42), 1: (134, 203, 34, 30), 2: (198, 203, 30, 42)}
        self.right_states = {0: (76, 65, 34, 42), 1: (140, 75, 34, 30), 2: (208, 75, 30, 42)}
        self.up_states = {0: (64, 137, 54, 44), 1: (126, 139, 58, 26), 2: (188, 129, 62, 40)}
        self.down_states = {0: (64, 9, 54, 44), 1: (126, 11, 58, 30), 2: (188, 1, 62, 42)}
        self.direction = facing
        self.movespeed = 1.85
        self.direction = 'down'
        self.health = 0.3
        self.sound = batsound
        self.deathsound = 0

class Slime(EnemyMob):
    def __init__(self, position, facing):
        self.group = slimes
        self.groups = all_sprites, slimes
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sheet = slime
        self.sheet.set_clip(pg.Rect(173, 33, 28, 26))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0: (47, 97, 26, 27), 1: (111, 97, 24, 28), 2: (175, 95, 24, 30)}
        self.right_states = {0: (47, 161, 24, 28), 1: (111, 159, 24, 30), 2: (237, 161, 26, 27)}
        self.up_states = {0: (45, 225, 28, 28), 1: (109, 223, 28, 30), 2: (237, 225, 30, 28)}
        self.down_states = {0: (45, 33, 28, 28), 1: (109, 31, 28, 30), 2: (235, 33, 30, 28)}
        self.direction = facing
        self.movespeed = 1.65
        self.direction = 'down'
        self.health = 0.15
        self.sound = slimesound
        self.deathsound = 0

class Deer(EnemyMob):
    def __init__(self, position, facing):
        self.group = deers
        self.groups = all_sprites, deers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sheet = deer
        self.sheet.set_clip(pg.Rect(78, 0, 36, 64))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0: (0, 66, 62, 62), 1: (66, 68, 62, 60), 2: (128, 70, 64, 58)}
        self.right_states = {0: (2, 130, 62, 62), 1: (66, 132, 62, 60), 2: (130, 134, 62, 58)}
        self.up_states = {0: (18, 196, 30, 62), 1: (82, 194, 30, 62), 2: (146, 196, 30, 60)}
        self.down_states = {0: (14, 2, 36, 62), 1: (78, 0, 36, 64), 2: (142, 4, 36, 60)}
        self.direction = facing
        self.movespeed = 1.75
        self.direction = 'down'
        self.health = 0.8
        self.sound = deersound
        self.deathsound = 0

class Wolf(EnemyMob):
    def __init__(self, position, facing):
        self.group = wolves
        self.groups = all_sprites, wolves
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sheet = wolf
        self.sheet.set_clip(pg.Rect(26, 8, 46, 86))
        self.frame = 0
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.left_states = {0: (96, 128, 88, 60), 1: (194, 126, 92, 60), 2: (290, 128, 88, 58)}
        self.right_states = {0: (6, 226, 88, 58), 1: (98, 224, 92, 60), 2: (200, 226, 88, 60)}
        self.up_states = {0: (124, 300, 42, 84), 1: (220, 296, 42, 86), 2: (316, 300, 42, 84)}
        self.down_states = {0: (122, 14, 46, 80), 1: (218, 8, 46, 86), 2: (314, 14, 46, 80)}
        self.direction = facing
        self.movespeed = 1.45
        self.direction = 'down'
        self.health = 1.3
        self.sound = wolfsound
        self.deathsound = 0

class Dragon(EnemyMob):
    def __init__(self, position, facing, mode):
        self.group = dragons
        self.groups = all_sprites, dragons
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sheet = dragon
        self.sheet.set_clip(pg.Rect(126, 11, 58, 30))
        self.frame = 0
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.left_states = {0: (0, 97, 97, 98), 1: (97, 97, 98, 98), 2: (195, 97, 94, 98)}
        self.right_states = {0: (0, 195, 97, 97), 1: (97, 195, 98, 97), 2: (198, 195, 94, 97)}
        self.up_states = {0: (3, 293, 94, 97), 1: (101, 292, 94, 97), 2: (198, 292, 94, 97)}
        self.down_states = {0: (3, 0, 94, 97), 1: (101, 0, 94, 97), 2: (198, 0, 94, 97)}
        self.direction = facing
        self.movespeed = 1.05
        self.direction = 'down'
        self.health = 3.3
        self.sound = dragonsound
        self.deathsound = 0

    def fire(self, playerrect):
        if self.health > 0 and playerrect.centerx >= self.rect.left and playerrect.centerx <= self.rect.right or playerrect.centery >= self.rect.top and playerrect.centery <= self.rect.bottom:
            Fireball(self.rect.centerx, self.rect.centery, self.direction)

    def anger(self):
        if self.health > 0 and self.health < 0.5:
            self.movespeed = 3.7
            Fireball(self.rect.centerx, self.rect.centery, self.direction)

#Dragon for Intro
class Startdragon(EnemyMob):
    def __init__(self, position, facing, mode):
        self.group = starterdragon
        self.groups = all_sprites, starterdragon
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sheet = dragon
        self.sheet.set_clip(pg.Rect(126, 11, 58, 30))
        self.frame = 0
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.left_states = {0: (0, 97, 97, 98), 1: (97, 97, 98, 98), 2: (195, 97, 94, 98)}
        self.right_states = {0: (0, 195, 97, 97), 1: (97, 195, 98, 97), 2: (198, 195, 94, 97)}
        self.up_states = {0: (3, 293, 94, 97), 1: (101, 292, 94, 97), 2: (198, 292, 94, 97)}
        self.down_states = {0: (3, 0, 94, 97), 1: (101, 0, 94, 97), 2: (198, 0, 94, 97)}
        self.direction = facing
        self.movespeed = 1.1
        self.direction = 'down'
        self.health = 2.8
        self.mode = mode
        self.sound = dragonsound
        
    def movement(self):
        if self.mode == 2:
            self.direction = 'left'

#Standing Villager              
class FriendlySpriteOne(pg.sprite.Sprite):
    def __init__(self):
        self.groups = all_sprites, friendly_one
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = standingsprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (498, 238)
        self.msgtimer = 3.9

    def handle_event(self, playersrect, events, girldir, playerquest):
        for characterone in character:
            if events.type == pg.MOUSEBUTTONDOWN and self.rect.colliderect(playersrect):
                self.msgtimer = 3.9
                if playerquest == 5:
                    message_display('I am so sorry...', 19, 6, black)
                else:
                    message_display('Hey! Rumour has it there is something up north...', 17, 6, black)
                
            elif self.rect.colliderect(playersrect):
                self.msgtimer = 3.91
                message_display('Click the mouse to talk!', 20, self.msgtimer, black)

        if girldir == 'up':
            self.image = standingspritetwo
        else:
            self.image = standingsprite

#Map classes
class GameSceneOne(SceneBase, Hero):
    def __init__(self):
        SceneBase.__init__(self)

    def Render(self, screen, x, y):
        displayBackground(tilemapone)

class GameSceneTwo(SceneBase, Hero):
    def __init__(self):
        SceneBase.__init__(self)

    def Render(self, screen, x, y):
        displayBackground(tilemaptwo)

class GameSceneThree(SceneBase, Hero):
    def __init__(self):
        SceneBase.__init__(self)

    def Render(self, screen, x, y):
        displayBackground(tilemapthree)

class GameSceneFour(SceneBase, Hero):
    def __init__(self):
        SceneBase.__init__(self)

    def Render(self, screen, x, y):
        displayBackground(tilemapfour)

class GameSceneFive(SceneBase, Hero):
    def __init__(self):
        SceneBase.__init__(self)

    def Render(self, screen, x, y):
        displayBackground(tilemapfive)

class GameSceneSix(SceneBase, Hero):
    def __init__(self):
        SceneBase.__init__(self)
        
    def Render(self, screen, x, y):
        displayBackground(tilemapsix)

class GameSceneSeven(SceneBase, Hero):
    def __init__(self):
        SceneBase.__init__(self)

    def Render(self, screen, x, y):
        displayBackground(tilemapseven)

class GameSceneEight(SceneBase, Hero):
    def __init__(self):
        SceneBase.__init__(self)

    def Render(self, screen, x, y):
        displayBackground(tilemapeight)

#Main GAME LOOP    
def game_loop(startx, starty, startone, starttwo, starting_scene):
    global pause, controls
    active_scene = starting_scene
    x = startx
    y = starty
    player = Hero((x, y))
    friendlymobtwo = FriendlySpriteTwo((startone, starttwo))
    batone = Bat((400, 400), 'left')
    battwo = Bat((240, 500), 'right')
    batthree = Bat((700, 400), 'up')
    slimeone = Slime((320, 320), 'down')
    slimetwo = Slime((640, 160), 'down')
    slimethree = Slime((650, 400), 'down')
    slimefour = Slime((880, 580), 'down')
    slimefive = Slime((400, 650), 'down')
    deerone = Deer((500, 500), 'down')
    deertwo = Deer((400, 500), 'down')
    deerthree = Deer((600, 500), 'down')
    wolfone = Wolf((500, 400), 'down')
    wolftwo = Wolf((600, 400), 'down')
    wolfthree = Wolf((500, 700), 'down')
    wolffour = Wolf((540, 200), 'down')
    dragonone = Dragon((600, 400), 'down', 1)
    dragontwo = Startdragon((1150, 400), 'left', 2)
    healthbar = Healthbar(player.health, (-28, 22))
    boxofhealth = HealthBox((570, 175), 0)
    player.setLocation('town')
    batplayed = 0
    slimeplayed = 0
    deerplayed = 0
    dragonplayed = 0
    wolfplayed = 0
    upgradepotential = True

    while active_scene != None:
        
        #Slime death detection
        if slimes.sprites() == []:
            player.questlvl = 11
            
        pressed_keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitgame()
                active_scene.Terminate()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and player.questlvl > 7:
                    now = pg.time.get_ticks()
                    if now - player.last_shot > player.firespeed:
                        player.last_shot = now
                        magicsound.play()
                        player.shoot()
                if event.key == pg.K_ESCAPE:
                    pause = True
                    game_pause(player.questlvl, player.wand, player.healthlvl)

        #Walls for intro    
        if player.questlvl <= 7 and player.get_location() == 'town':
            if player.collisionrect.right > 1120:
                player.collisionrect.right = 1120
                player.rect.right = player.collisionrect.right
            if player.collisionrect.left < 0:
                player.collisionrect.left = 0
                player.rect.left = player.collisionrect.left
            if player.collisionrect.top - 35 < 0:
                player.collisionrect.top = 35
                player.rect.top = player.collisionrect.top - 35
            if player.collisionrect.bottom > 880:
                player.collisionrect.bottom = 880
                player.rect.bottom = 880
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[1])
            pg.mixer.music.play(-1)
            
        elif player.rect.top < 0 and player.get_location() == 'town':
            active_scene.SwitchToScene(GameSceneTwo())
            player.collisionrect.x = 505
            player.collisionrect.y = 845
            player.rect.x = player.collisionrect.x
            player.rect.y = player.collisionrect.y - 35
            print('switching to north river')
            player.setLocation('northriver')
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[1])
            pg.mixer.music.play(-1)
            
        #Map switching detection
        if player.rect.bottom > display_height and player.get_location() == 'northriver':
            active_scene.SwitchToScene(GameSceneOne())
            player.collisionrect.x = 505
            player.rect.y = 0
            player.rect.x = player.collisionrect.x
            player.collisionrect.y = player.rect.y + 35
            print('switching to town')
            player.setLocation('town')
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[0])
            pg.mixer.music.play(-1)

        if player.rect.right > display_width and player.get_location() == 'town':
            active_scene.SwitchToScene(GameSceneThree())
            player.collisionrect.x = 1
            player.rect.x = player.collisionrect.x
            print('switching to east plains')
            player.setLocation('eastplains')
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[2])
            pg.mixer.music.play(-1)
                                              

        if player.rect.left < 0 and player.get_location() == 'eastplains':
            active_scene.SwitchToScene(GameSceneOne())
            player.collisionrect.x = 1072
            player.rect.x = player.collisionrect.x
            print('switching to town')
            player.setLocation('town')
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[0])
            pg.mixer.music.play(-1)

        if player.rect.left < 0 and player.get_location() == 'town':
            active_scene.SwitchToScene(GameSceneFive())
            player.collisionrect.x = 1072
            player.rect.x = player.collisionrect.x
            print('switching to dragonone')
            player.setLocation('dragonone')
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[3])
            pg.mixer.music.play(-1)

        if player.rect.right > 1120 and player.get_location() == 'dragonone':
            active_scene.SwitchToScene(GameSceneOne())
            player.collisionrect.x = 1
            if player.collisionrect.y <= 560 and player.collisionrect.y >= 320:
                pass

            else:
                player.collisionrect.y = 430
                player.rect.y = player.collisionrect.y - 35
                
            player.rect.x = player.collisionrect.x
            print('switching to town')
            player.setLocation('town')
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[0])
            pg.mixer.music.play(-1)

        if player.rect.bottom > display_height and player.get_location() == 'town':
            active_scene.SwitchToScene(GameSceneSix())
            player.collisionrect.x = 505
            player.rect.y = 0
            player.rect.x = player.collisionrect.x
            player.collisionrect.y = player.rect.y + 35
            print('switching to desert')
            player.setLocation('desert')
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[2])
            pg.mixer.music.play(-1)

        if player.collisionrect.top - 35 < 0 and player.get_location() == 'desert':
            active_scene.SwitchToScene(GameSceneOne())
            player.collisionrect.x = 505
            player.collisionrect.y = 845
            player.rect.x = player.collisionrect.x
            player.rect.y = player.collisionrect.y - 35
            print('switching to town')
            player.setLocation('town')
            pg.mixer.music.stop()
            pg.mixer.music.load(songs[0])
            pg.mixer.music.play(-1)

        if player.collisionrect.left < 0 and player.get_location() == 'dragonone':
            active_scene.SwitchToScene(GameSceneSeven())
            player.collisionrect.x = 1072
            player.rect.x = player.collisionrect.x
            print('switching to dragon entrance')
            player.setLocation('dragonentrance')

        if player.collisionrect.right > 1120 and player.get_location() == 'dragonentrance':
            active_scene.SwitchToScene(GameSceneFive())
            player.collisionrect.x = 1
            player.rect.x = player.collisionrect.x
            print('switching to dragonone')
            player.setLocation('dragonone')

        if player.collisionrect.left < 0 and player.get_location() == 'dragonentrance':
            active_scene.SwitchToScene(GameSceneEight())
            player.collisionrect.x = 1072
            player.rect.x = player.collisionrect.x
            print('switching to dragon cave')
            player.setLocation('dragoncave')

        #Award for quest
        if friendlymobtwo.completed == True:
            player.firespeed = 150
            player.wand = 1

        #Son display
        if player.get_location() == 'town':
            GAMEDISPLAY.blit(son, (970, 640))
            
        #Bossfight Walls
        if player.get_location() == 'dragoncave':
            if player.collisionrect.right > 1120:
                player.collisionrect.right = 1120
                player.rect.right = player.collisionrect.right
            if player.collisionrect.left < 0:
                player.collisionrect.left = 0
                player.rect.left = player.collisionrect.left
            if player.collisionrect.top - 35 < 0:
                player.collisionrect.top = 35
                player.rect.top = player.collisionrect.top - 35
            if player.collisionrect.bottom > 880:
                player.collisionrect.bottom = 880
                player.rect.bottom = 880

        #Staircase detection heart cave
        if player.collisionrect.left < 50 and player.get_location() == 'northriver':
            active_scene.SwitchToScene(GameSceneFour())
            player.collisionrect.x = 1000
            player.collisionrect.y = 500
            player.rect.x = player.collisionrect.x
            player.rect.y = player.collisionrect.y - 35
            print('switching to heart cave')
            player.setLocation('heartcave')

        if player.collisionrect.right > 1090 and player.get_location() == 'heartcave':
            active_scene.SwitchToScene(GameSceneTwo())
            player.collisionrect.x = 81
            player.collisionrect.y = 500
            player.rect.x = player.collisionrect.x
            player.rect.y = player.collisionrect.y - 35
            print('switching to north river')
            player.setLocation('northriver')

        #Desert Wandering Warning!
        if player.collisionrect.left > 1120 or player.collisionrect.right < 0 or player.collisionrect.top > 880 and player.get_location() == 'desert':
            warningtimer = 4.9
            message_display('Warning! Do not get lost!', 23, warningtimer, black)
        else:
            warningtimer = 3.9

        #Class in-game-loop operations
        player.handle_event(event, player.direction)
        active_scene.Render(GAMEDISPLAY, x, y)
        active_scene = active_scene.next
        bullets.update()
        bullets.draw(GAMEDISPLAY)
        fireballs.update()
        fireballs.draw(GAMEDISPLAY)
        
        #Intro

        starterdragon.draw(GAMEDISPLAY)
        
        if player.questlvl == 0:
            
            dragontwo.update('left')
            dragontwo.movement()
            if dragontwo.rect.x < 550 and dragontwo.rect.x > 540:
                player.questlvl = 1

        if player.questlvl == 1:
            message_display('Dragon: This world will crack under my wraith!', 20, 7, black)
            dragontwo.sound.play()
            player.questlvl = 2

        if player.questlvl == 2:
            dragontwo.movespeed = 5
            player.questlvl = 3
            
        dragontwo.update('left')
        dragontwo.movement()
            
        if dragontwo.rect.right < 0 and player.questlvl == 3:
            dragontwo.kill()
            player.questlvl = 4

        if player.questlvl == 4:
            message_display('Explore the town!', 23, 6.6, black)
            player.questlvl = 5

        if player.get_location() == 'town':
            GAMEDISPLAY.blit(son, (970, 640))

        if player.questlvl == 5:
            if player.collisionrect.left > 925 and player.collisionrect.top > 650 and player.collisionrect.bottom < 740:
                message_display('You: My son! The dragon must have done this!', 17, 8, black)
                intro_images()
                
                smoke = [smokeone, smoketwo, smokethree, smokefour, smokefive, smokesix]
                for smo in smoke:
                    intro_images()
                    GAMEDISPLAY.blit(smo, (855, 640))
                    GAMEDISPLAY.blit(firstpicture, (928, 640))
                    pg.display.update()
                    time.sleep(0.11)
                    if smo == smoke[5]:
                        player.questlvl = 6
                        
        if player.questlvl == 6:
            intro_images()
            more_images()
            message_display('You: A mage! Can you revive him?', 21, 8, black)
            intro_images()
            more_images()
            message_display('Mage: I can not. The dragon took your son;', 22, 8, black)
            intro_images()
            more_images()
            message_display('Mage: It is your destiny to defeat him!', 24, 8, black)
            intro_images()
            more_images()
            message_display('Mage: Take this wand. Avenge your son! (SPACE to fire)', 17, 8, black)
            player.questlvl = 7

        if player.questlvl == 7:
            smoke = [smokeone, smoketwo, smokethree, smokefour, smokefive, smokesix]
            for smo in smoke:
                intro_images()
                GAMEDISPLAY.blit(smo, (855, 640))
                GAMEDISPLAY.blit(firstpicture, (928, 640))
                pg.display.update()
                time.sleep(0.11)
                if smo == smoke[5]:
                    player.questlvl = 8

        if player.questlvl == 8:
            intro_images()
            GAMEDISPLAY.blit(holdwand, (928, 640))
            pg.display.update()
            time.sleep(3)
            displayBackground(tilemapone)
            player.questlvl = 9
            
        #Death
        if healthbar.rect.right <= 0:
            death()
            
        #Friendly Mob One
        if player.get_location() == 'town' and player.questlvl > 4:
            friendly_one.draw(GAMEDISPLAY)
            FriendlySpriteOne().handle_event(player.collisionrect, event, friendlymobtwo.direction, player.questlvl)

        #Friendly Mob Two
        if player.get_location() == 'town' and player.questlvl > 4:
            friendly_two.draw(GAMEDISPLAY)
            friendlymobtwo.handle_event(friendlymobtwo.direction, player.collisionrect, event, player.questlvl, player.firespeed)
            friendlymobtwo.update(friendlymobtwo.direction, player.collisionrect)

        #Bats in north river
        if player.get_location() == 'northriver':
            bats.draw(GAMEDISPLAY)
            
            batone.handle_event(event, batone.direction, player.collisionrect)
            batone.update(batone.direction)
            battwo.handle_event(event, battwo.direction, player.collisionrect)
            battwo.update(battwo.direction)
            batthree.handle_event(event, batthree.direction, player.collisionrect)
            batthree.update(batthree.direction)

            if bats.sprites() != [] and batplayed < 2:
                batone.sound.play()
                batplayed += 1

        #Slimes in east plains
        if player.get_location() == 'eastplains':
            slimes.draw(GAMEDISPLAY)
            
            slimeone.handle_event(event, slimeone.direction, player.collisionrect)
            slimeone.update(slimeone.direction)
            slimetwo.handle_event(event, slimetwo.direction, player.collisionrect)
            slimetwo.update(slimetwo.direction)
            slimethree.handle_event(event, slimethree.direction, player.collisionrect)
            slimethree.update(slimethree.direction)
            slimefour.handle_event(event, slimefour.direction, player.collisionrect)
            slimefour.update(slimefour.direction)
            slimefive.handle_event(event, slimefive.direction, player.collisionrect)
            slimefive.update(slimefive.direction)

            if slimes.sprites() != [] and slimeplayed < 2:
                slimeone.sound.play()
                slimeplayed += 1

        #Deer in west one
        if player.get_location() == 'dragonone':
            deers.draw(GAMEDISPLAY)

            deerone.handle_event(event, deerone.direction, player.collisionrect)
            deerone.update(deerone.direction)
            deertwo.handle_event(event, deertwo.direction, player.collisionrect)
            deertwo.update(deertwo.direction)
            deerthree.handle_event(event, deerthree.direction, player.collisionrect)
            deerthree.update(deerthree.direction)

            if deers.sprites() != [] and deerplayed < 2:
                deerone.sound.play()
                deerplayed += 1

        #Wolves in west two
        if player.get_location() == 'dragonentrance':
            wolves.draw(GAMEDISPLAY)

            wolfone.handle_event(event, wolfone.direction, player.collisionrect)
            wolfone.update(wolfone.direction)
            wolftwo.handle_event(event, wolftwo.direction, player.collisionrect)
            wolftwo.update(wolftwo.direction)
            wolfthree.handle_event(event, wolfthree.direction, player.collisionrect)
            wolfthree.update(wolfthree.direction)
            wolffour.handle_event(event, wolffour.direction, player.collisionrect)
            wolffour.update(wolffour.direction)

            if wolves.sprites() != [] and wolfplayed < 2:
                wolfone.sound.play()
                wolfplayed += 1

        #Boss
        if player.get_location() == 'dragoncave':
            dragons.draw(GAMEDISPLAY)

            dragonone.handle_event(event, dragonone.direction, player.collisionrect)
            dragonone.update(dragonone.direction)
            if dragonone.health > 0:
                dragonone.fire(player.collisionrect)
                dragonone.anger()
            else:
                fireballs.empty()
            if dragons.sprites() == []:
                victory()
            if dragons.sprites() != [] and dragonplayed < 4:
                dragonone.sound.play()
                dragonplayed += 1

        #Damage Dealer / Checker / Display
            
        health.draw(GAMEDISPLAY)

        if player.get_location() == 'heartcave':
            healthbox.draw(GAMEDISPLAY)

        if boxofhealth.rect.colliderect(player.collisionrect) == True and player.get_location() == 'heartcave':
            boxofhealth.healthupgrade()
            boxofhealth.mode = 1
            if player.questlvl <= 11 and upgradepotential == True:
                boxofhealth.kill()
                healthbar.upgrade()
                upgradesound.play()
                player.healthlvl = 1
                player.questlvl = 12
                upgradepotential = False
                
        if boxofhealth.mode == 0:
            GAMEDISPLAY.blit(healthcontainer, (-28, 10))
        elif boxofhealth.mode == 1:
            GAMEDISPLAY.blit(healthcontainer, (0, 10))

        if player.get_location() == 'town':
            pass
        else:
            if pg.sprite.groupcollide(character, fireballs, False, True, collided = None) and player.get_location() == 'dragoncave':
                player.lower_health(0.8)
                healthbar.lower(0.8)

            elif pg.sprite.groupcollide(character, bats, False, False, collided = None) and player.get_location() == 'northriver': 
                player.lower_health(0.4)
                healthbar.lower(0.4)

            elif pg.sprite.groupcollide(character, slimes, False, False, collided = None) and player.get_location() == 'eastplains': 
                player.lower_health(0.35)
                healthbar.lower(0.35)

            elif pg.sprite.groupcollide(character, deers, False, False, collided = None) and player.get_location() == 'dragonone': 
                player.lower_health(0.5)
                healthbar.lower(0.5)

            elif pg.sprite.groupcollide(character, wolves, False, False, collided = None) and player.get_location() == 'dragonentrance':
                player.lower_health(0.75)
                healthbar.lower(0.75)

            if pg.sprite.groupcollide(character, dragons, False, False, collided = None) and player.get_location() == 'dragoncave':
                player.lower_health(1)
                healthbar.lower(1)

        #Final operations in while loop 
        GAMEDISPLAY.blit(player.image, player.rect)
        pg.display.update()
        clock.tick(FPS)

#Get out of controls screen
def get_out():
    global controls
    controls = False
    game_start()

#Controls Screen
def game_controls():

    controls = True
    while controls:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitgame()
                
        GAMEDISPLAY.fill(black)
        
        TextSurf, TextRect = text_objects('Game Controls', largeText, gray)
        TextRect.center = ((display_width / 2), (display_height / 5))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('Use arrow keys to move!', smallText, gray)
        TextRect.center = ((display_width / 2), ((display_height / 3.5) + 75))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('Click mouse to engage with villagers!', smallText, gray)
        TextRect.center = ((display_width / 2), ((display_height / 3.5) + 150))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('Hit escape to view progress, pause or for a tip!', smallText, gray)
        TextRect.center = ((display_width / 2), ((display_height / 3.5) + 225))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        button('Back', 500, 230, 100, 50, blue, hoverblue, get_out)

        pg.display.update()

      
#Start Screen
def game_start():

    start = True
    while start:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitgame()
                
        GAMEDISPLAY.blit(bgstart, (0, 0))

        TextSurf, TextRect = text_objects('Dragon Slayer', largeText, black)
        TextRect.center = ((display_width / 2), (display_height / 5))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        button('Play!', 180, 230, 150, 50, blue, hoverblue, game_intro)
        button(' Quit!', 840, 230, 150, 50, blue, hoverblue, quitgame)
        button('Controls!', 500, 230, 160, 50, blue, hoverblue, game_controls)

        pg.display.update()

#Victory Screen
def victory():

    victory = True
    while victory:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitgame()

        GAMEDISPLAY.fill(black)
        GAMEDISPLAY.blit(trophy, ((display_width / 2) - 109.5, display_height / 2))

        TextSurf, TextRect = text_objects('VICTORY', largeText, gray)
        TextRect.center = ((display_width / 2), (display_height / 5))
        GAMEDISPLAY.blit(TextSurf, TextRect)
        button(' Quit!', (display_width / 2) - 50, (display_height / 2) - 60, 100, 50, blue, hoverblue, quitgame)

        pg.display.update()

#Unpause function
def unpause():
    pauseoutsound.play()
    global pause
    pause = False
    
#Pause Screen
def game_pause(playerlvl, wandlvl, healthlvl):
    pauseinsound.play()

    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitgame()
                
        GAMEDISPLAY.fill(black)
        
        TextSurf, TextRect = text_objects('Game Paused', largeText, gray)
        TextRect.center = ((display_width / 2), (display_height / 5))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('Player Quest Level: ' + str(playerlvl) + '/12', smallText, gray)
        TextRect.center = ((display_width / 2), ((display_height / 3.5) + 75))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('Player Wand Level: ' + str(wandlvl) + '/1', smallText, gray)
        TextRect.center = ((display_width / 2), ((display_height / 3.5) + 150))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects('Player Health Level: ' + str(healthlvl) + '/1', smallText, gray)
        TextRect.center = ((display_width / 2), ((display_height / 3.5) + 225))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        if playerlvl <= 7:
            TextSurf, TextRect = text_objects('Tip: What is in that corner', smallText, gray)
            TextRect.center = ((display_width / 2), ((display_height / 3.5) + 300))
            GAMEDISPLAY.blit(TextSurf, TextRect)

        elif wandlvl != 1 or healthlvl != 1:
            TextSurf, TextRect = text_objects('Tip: Villagers may assist you in your quest', smallText, gray)
            TextRect.center = ((display_width / 2), ((display_height / 3.5) + 300))
            GAMEDISPLAY.blit(TextSurf, TextRect)

        elif wandlvl == 1 and healthlvl == 1:
            TextSurf, TextRect = text_objects('Tip: The dragon went west', smallText, gray)
            TextRect.center = ((display_width / 2), ((display_height / 3.5) + 300))
            GAMEDISPLAY.blit(TextSurf, TextRect)

        button('Resume', 180, 230, 100, 50, blue, hoverblue, unpause)
        button(' Quit', 840, 230, 100, 50, blue, hoverblue, quitgame)

        pg.display.update()

#Death Screen
def death():

    death = True
    while death:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitgame()

        GAMEDISPLAY.fill(black)
        GAMEDISPLAY.blit(deathimg, ((display_width / 2) - 100, display_height / 2))

        TextSurf, TextRect = text_objects('You Died', largeText, gray)
        TextRect.center = ((display_width / 2), (display_height / 5))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        button(' Quit!', (display_width / 2) - 65, (display_height / 2) - 80, 100, 50, blue, hoverblue, quitgame)

        pg.display.update()
        
#Game introduction
def game_intro():
    pg.mixer.music.stop()
    intro = True
    
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitgame()

        display_image(dragonclosed, 0, 0, 1.5)
        display_image(dragonhalf, 0, 0, 0.05)
        display_image(dragonopen, 0, 0, 1.2)
        GAMEDISPLAY.fill(black)
        display_image(doorone, 430, 546, 1.2)
        display_image(doortwo, 430, 546, 0.7)
        display_image(doorthree, 430, 546, 0.7)
        display_image(doorfour, 430, 546, 0.5)
        GAMEDISPLAY.fill(black)

        time.sleep(1.8)
        
        
        game_loop(650, 260, 900, 410, GameSceneOne())
        intro = False

#Icon image
pg.display.set_icon(holdwand)

#Initiation
pg.mixer.music.load(songs[5])
pg.mixer.music.play(-1)
game_start()

    
